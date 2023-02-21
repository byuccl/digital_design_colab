# @title Install Interactive Simulation
def altair_sim():
    dataframe = vcd2dataframe("/content/tmp_code/logs/vlt_dump.vcd")
    dataframe1 = dataframe
    df_max = 0
    for i in dataframe:
        if df_max < max(dataframe[i]):
            df_max = max(dataframe[i])
    import altair as alt
    import pandas as pd
    import numpy as np
    from vega_datasets import data

    length_df = 0
    for i in dataframe:
        if len(dataframe[i]) > length_df:
            length_df = len(dataframe[i])

    def make_waveform(dataframe):
        length_df = 0
        for i in dataframe:

            if len(dataframe[i]) > length_df:
                length_df = len(dataframe[i])

        source = pd.DataFrame(dataframe, index=pd.RangeIndex(length_df, name="x"))
        source = source.reset_index().melt("x", var_name="signals", value_name="y")
        scales = alt.selection_interval(bind="scales")

        multi_mouseover = alt.selection_multi(on="mouseover", toggle=True, empty="none")

        selection = alt.selection_multi(fields=["signals"], bind="legend")

        # Create a selection that chooses the nearest point & selects based on x-value
        nearest = alt.selection(
            type="multi", nearest=True, on="mouseover", fields=["x"], empty="none"
        )

        # The basic line
        line = (
            alt.Chart(source)
            .mark_line(interpolate="step-after")
            .encode(x="x:Q", y="y:Q", color="signals:N")
        )

        # Transparent selectors across the chart. This is what tells us
        # the x-value of the cursor
        selectors = (
            alt.Chart(source)
            .mark_point()
            .encode(
                x="x:Q",
                opacity=alt.value(0),
            )
            .add_selection(nearest, scales)
        )

        # Draw points on the line, and highlight based on selection
        points = line.mark_point().encode(
            opacity=alt.condition(nearest, alt.value(1), alt.value(0))
        )

        # Draw text labels near the points, and highlight based on selection
        text = line.mark_text(align="left", dx=5, dy=-5).encode(
            text=alt.condition(nearest, "y:Q", alt.value(""))
        )

        # Draw a rule at the location of the selection
        rules = (
            alt.Chart(source)
            .mark_rule(color="black")
            .encode(
                x="x:Q",
            )
            .transform_filter(nearest)
        )

        # Put the five layers into a chart and bind the data
        waveform = (
            alt.layer(line, selectors, points, rules, text)
            .encode(
                alt.X(scale=alt.Scale(domain=(0, length_df))),
                alt.Y(scale=alt.Scale(domain=(0, df_max + 1))),
                opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
            )
            .properties(width=600, height=400)
            .add_selection(selection)
        )

        histogram = (
            alt.Chart(source)
            .mark_bar()
            .encode(
                alt.X("y", scale=alt.Scale(domain=(0, df_max + 1))),
                y="signals",
                color="signals:N",
            )
            .transform_filter(nearest)
            .properties(width=600, height=200)
        )
        text = histogram.mark_text(align="left", baseline="middle", dx=3).encode(
            text="y:Q"
        )
        histogram = histogram + text
        return waveform, histogram

    waveform1, histogram1 = make_waveform(dataframe1)
    return waveform1, histogram1

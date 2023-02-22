def create_expanded_button(description, button_style, width="auto", tooltip=""):
    return Button(
        description=description,
        button_style=button_style,
        layout=Layout(height="auto", width=width),
        tooltip=tooltip,
    )


def create_frq_int(list, index, q_width=500, max_=11111111):
    qlist = list[index]
    grid = GridspecLayout(1, 3, width=(str(250 + q_width) + "px"))
    grid[0, 0] = create_expanded_button(qlist[0], "info", str(q_width) + "px")
    grid[0, 1] = widgets.BoundedIntText(
        min=(-1 * max_), max=max_, layout=Layout(width="100px")
    )
    tooltip = f"Q%d" % index
    grid[0, 2] = create_expanded_button("Check", "info", tooltip=tooltip)
    return grid


frqdict = {"Q0": ["Convert this binary number to decimal: 10110", 22]}
frq_1 = create_frq_int(frquestions, 0, 400)
frqs = {"Q0": frq_1}


def frq_check(key):
    grid = frqs[key]
    qlist = frqdict[key]
    print(frqdict[key])
    print(grid[0, 1].value)
    print()
    if grid[0, 1].value == qlist[1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq(self):
    key = self.tooltip
    frq_check(key)


frq_1[0, 2].on_click(check_frq)

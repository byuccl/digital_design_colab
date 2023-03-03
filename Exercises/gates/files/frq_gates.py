import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText, IntSlider


def create_expanded_button(description, button_style, width="auto", tooltip=""):
    """
    Returns a button object. These button objects are the building blocks of a widget.
    The button object is used for both interactive buttons and formatting squares.
    Parameters
    ------
    Description: String
        This is the text that will appear inside the button
    Button_Style: String
        Style determines the color of the button, there are 5 built-in styles, 'primary' (blue), 'success' (green), 'info'(light blue), 'warning' (orange). and 'danger' (red).
        Custom colors are supported by IPython but not by this function. You can use buttonObj.style.button_color = 'custom_color' to set a custom color.
    Width: String
        Provide a width in pixels (px) for the button
    Tooltip: String
        Tooltip is the string that appears when you hover over the button. This is used to store the dictionary key to store with question it is linked to.
    """
    return Button(
        description=description,
        button_style=button_style,
        layout=Layout(height="auto", width=width),
        tooltip=tooltip,
    )


def create_frq_int(list, index, q_width=500, max_=11111111):
    """
    Returns a grid object made up of 2 buttons and a Bounded Integer text widget.
    This widget is for questions with an answer that is an integer
    Parameters
    --------
    list: dictionary of lists
        The dictionary holds an array. The key is generated from the index and stored in tooltip.
        The first element in the list is the question, the second is the answer.
    Index: Integer
        The question number, starting at 0.
    q_width: Integer
        The width of the question. Longer questions may need larger widths to prevent scrolling.
    max:
        The maximum value of the integer box. The minimum is set to the inverse of the maximum
    """
    tooltip = f"Q%d" % index
    qlist = list[tooltip]
    grid = GridspecLayout(1, 3, width=(str(250 + q_width) + "px"))
    grid[0, 0] = create_expanded_button(qlist[0], "info", str(q_width) + "px")
    grid[0, 1] = widgets.BoundedIntText(
        min=(-1 * max_), max=max_, layout=Layout(width="100px")
    )
    grid[0, 2] = create_expanded_button("Check", "info", tooltip=tooltip)
    return grid


def create_frq_string(list, index, q_width=500):
    """
    Returns a grid object made up of 2 buttons and a Text widget
    This widget is designed for a question that has a string as the answer
    Parameters
    --------
    list: dictionary of lists
        The dictionary holds an array. The key is generated from the index and stored in tooltip.
        The first element in the list is the question, the second is the answer.
    Index: Integer
        The question number, starting at 0.
    q_width: Integer
        The width of the question. Longer questions may need larger widths to prevent scrolling.
    """
    tooltip = f"Q%d" % index
    qlist = list[tooltip]
    grid = GridspecLayout(1, 3, width=(str(250 + q_width) + "px"))
    grid[0, 0] = create_expanded_button(qlist[0], "info", str(q_width) + "px")
    grid[0, 1] = widgets.Text(
        placeholder="Answer",
        layout=Layout(width="100px"),
    )
    grid[0, 2] = create_expanded_button("Check", "info", tooltip=tooltip)
    return grid


"""
The dictionary that holds the questions and the answers.
Answers can be String or Int type. This does change the function used to create the grid object as shown
The key is Q + Question Index. 
"""
frquestions = {"Q1": ["What is the output of this set of gates?", "1"]}

# Define your FRQs here
frq_1 = create_frq_int(frquestions, 0)


frqs = {
    "Q1": frq_1,
}


def frq_check(key):
    grid = frqs[key]
    qlist = frquestions[key]
    if grid[0, 1].value == qlist[1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq(self):
    key = self.tooltip
    frq_check(key)


frq_1[0, 2].on_click(check_frq)
# frq_2[0, 2].on_click(check_frq)
# frq_3[0, 2].on_click(check_frq)
# frq_4[0, 2].on_click(check_frq)
# frq_5[0, 2].on_click(check_frq)
# frq_6[0, 2].on_click(check_frq)
# frq_7[0, 2].on_click(check_frq)
# frq_8[0, 2].on_click(check_frq)
# frq_9[0, 2].on_click(check_frq)
# frq_10[0, 2].on_click(check_frq)
# frq_11[0, 2].on_click(check_frq)
# frq_12[0, 2].on_click(check_frq)

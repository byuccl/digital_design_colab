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
"""
frquestions = {
    "Q0": ["Convert this binary number to decimal: 10110", 22],
    "Q1": ["Convert this binary number to decimal: 10001", 17],
    "Q2": ["Convert this binary number to decimal: 101011", 43],
    "Q3": ["Convert this decimal number to binary: 9", 1001],
    "Q4": ["Convert this decimal number to binary: 21", 10101],
    "Q5": ["Convert this decimal number to binary: 63", 111111],
    "Q6": ["Convert this hexadecimal number to decimal: A3E", 2622],
    "Q7": ["Convert this hexadecimal number to binary: 5B", 1011011],
    "Q8": ["Convert this hexadecimal number to binary: C9", 11001001],
    "Q9": ["Convert this decimal number to hexadecimal: 137", 89],
    "Q10": ["Convert this binary number to hexadecimal: 10000011 ", 83],
    "Q11": ["Convert this binary number to hexadecimal: 1011111011101111", "BEEF"],
}
frq_1 = create_frq_int(frquestions, 0, 400)

frq_2 = create_frq_int(frquestions, 1, 400)

frq_3 = create_frq_int(frquestions, 2, 400)

frq_4 = create_frq_int(frquestions, 3, 400)

frq_5 = create_frq_int(frquestions, 4, 400)

frq_6 = create_frq_int(frquestions, 5, 400)
frq_7 = create_frq_int(frquestions, 6, 400)
frq_8 = create_frq_int(frquestions, 7, 400)

frq_9 = create_frq_int(frquestions, 8, 400)
frq_10 = create_frq_int(frquestions, 9, 400)


frq_11 = create_frq_int(frquestions, 10, 400)

frq_12 = create_frq_string(frquestions, 11, 400)


frqs = {
    "Q0": frq_1,
    "Q1": frq_2,
    "Q2": frq_3,
    "Q3": frq_4,
    "Q4": frq_5,
    "Q5": frq_6,
    "Q6": frq_7,
    "Q7": frq_8,
    "Q8": frq_9,
    "Q9": frq_10,
    "Q10": frq_11,
    "Q11": frq_12,
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
frq_2[0, 2].on_click(check_frq)
frq_3[0, 2].on_click(check_frq)
frq_4[0, 2].on_click(check_frq)
frq_5[0, 2].on_click(check_frq)
frq_6[0, 2].on_click(check_frq)
frq_7[0, 2].on_click(check_frq)
frq_8[0, 2].on_click(check_frq)
frq_9[0, 2].on_click(check_frq)
frq_10[0, 2].on_click(check_frq)
frq_11[0, 2].on_click(check_frq)
frq_12[0, 2].on_click(check_frq)

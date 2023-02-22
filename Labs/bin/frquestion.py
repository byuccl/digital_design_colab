import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText, IntSlider

# Free Response QUESTIONs
frquestions = [
    ["Convert this binary number to decimal: 10110", 22],
    ["Convert this binary number to decimal: 10001", 17],
    ["Convert this binary number to decimal: 101011", 43],
    ["Convert this decimal number to binary: 9", 1001],
    ["Convert this decimal number to binary: 21", 10101],
    ["Convert this decimal number to binary: 63", 111111],
    ["Convert this hexadecimal number to decimal: A3E", 2622],
    ["Convert this hexadecimal number to binary: 5B", 1011011],
    ["Convert this hexadecimal number to binary: C9", 11001001],
    ["Convert this decimal number to hexadecimal: 137", 89],
    ["Convert this binary number to hexadecimal: 10000011 ", 83],
    ["Convert this binary number to hexadecimal: 1011111011101111", "BEEF"],
]


def create_expanded_button(description, button_style, width="auto"):
    return Button(
        description=description,
        button_style=button_style,
        layout=Layout(height="auto", width=width),
    )


def create_frq_int(list, index, q_width=500, max_=11111111):
    qlist = list[index]
    grid = GridspecLayout(1, 3, width=(str(250 + q_width) + "px"))
    grid[0, 0] = create_expanded_button(qlist[0], "info", str(q_width) + "px")
    grid[0, 1] = widgets.BoundedIntText(
        min=(-1 * max_), max=max_, layout=Layout(width="100px")
    )
    grid[0, 2] = create_expanded_button("Check", "info")
    return grid


def create_frq_string(list, index, q_width=500):
    qlist = list[index]
    grid = GridspecLayout(1, 3, width=(str(250 + q_width) + "px"))
    grid[0, 0] = create_expanded_button(qlist[0], "info", str(q_width) + "px")
    grid[0, 1] = widgets.Text(
        placeholder="Answer",
        layout=Layout(width="100px"),
    )
    grid[0, 2] = create_expanded_button("Check", "info")
    return grid


# Question 1
frq_1 = create_frq_int(frquestions, 0, 400)


def frq_1_check(grid, qlist):
    if grid[0, 1].value == qlist[0][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_1(self):
    frq_1_check(frq_1, frquestions)


# Question 2
frq_2 = create_frq_int(frquestions, 1, 400)


def frq_2_check(grid, qlist):
    if grid[0, 1].value == qlist[1][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_2(self):
    frq_2_check(frq_2, frquestions)


# Question 3
frq_3 = create_frq_int(frquestions, 2, 400)


def frq_3_check(grid, qlist):
    if grid[0, 1].value == qlist[2][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_3(self):
    frq_3_check(frq_3, frquestions)


# Question 4
frq_4 = create_frq_int(frquestions, 3, 400)


def frq_4_check(grid, qlist):
    if grid[0, 1].value == qlist[3][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_4(self):
    frq_4_check(frq_4, frquestions)


# Question 5
frq_5 = create_frq_int(frquestions, 4, 400)


def frq_5_check(grid, qlist):
    if grid[0, 1].value == qlist[4][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_5(self):
    frq_5_check(frq_5, frquestions)


# Question 6
frq_6 = create_frq_int(frquestions, 5, 400)


def frq_6_check(grid, qlist):
    if grid[0, 1].value == qlist[5][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_6(self):
    frq_6_check(frq_6, frquestions)


# Question 7
frq_7 = create_frq_int(frquestions, 6, 400)


def frq_7_check(grid, qlist):
    if grid[0, 1].value == qlist[6][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_7(self):
    frq_7_check(frq_7, frquestions)


# Question 8
frq_8 = create_frq_int(frquestions, 7, 400)


def frq_8_check(grid, qlist):
    if grid[0, 1].value == qlist[7][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_8(self):
    frq_8_check(frq_8, frquestions)


# Question 9
frq_9 = create_frq_int(frquestions, 8, 400, 11111111)


def frq_9_check(grid, qlist):
    if grid[0, 1].value == qlist[8][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_9(self):
    frq_9_check(frq_9, frquestions)


# Question 10
frq_10 = create_frq_int(frquestions, 9, 400)


def frq_10_check(grid, qlist):
    if grid[0, 1].value == qlist[9][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_10(self):
    frq_10_check(frq_10, frquestions)


# Question 11
frq_11 = create_frq_int(frquestions, 10, 400)


def frq_11_check(grid, qlist):
    if grid[0, 1].value == qlist[10][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_11(self):
    frq_11_check(frq_11, frquestions)


# Question 12
frq_12 = create_frq_string(frquestions, 11, 400)


def frq_12_check(grid, qlist):
    if grid[0, 1].value == qlist[11][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_12(self):
    frq_12_check(frq_12, frquestions)

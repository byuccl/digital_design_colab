# @title FRQ Creation { form-width: "1000px" }
# TO DO: Refactor this nightmare using a dictionary
# Question 1
frq_1 = create_frq(frquestions, 0)


def frq_1_check(grid, qlist):
    if grid[0, 1].value == qlist[0][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_1(self):
    frq_1_check(frq_1, frquestions)


# Question 2
frq_2 = create_frq(frquestions, 1)


def frq_2_check(grid, qlist):
    if grid[0, 1].value == qlist[1][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_2(self):
    frq_2_check(frq_2, frquestions)


# Question 3
frq_3 = create_frq(frquestions, 2)


def frq_3_check(grid, qlist):
    if grid[0, 1].value == qlist[2][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_3(self):
    frq_3_check(frq_3, frquestions)


# Question 4
frq_4 = create_frq(frquestions, 3)


def frq_4_check(grid, qlist):
    if grid[0, 1].value == qlist[3][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_4(self):
    frq_4_check(frq_4, frquestions)


# Question 5
frq_5 = create_frq(frquestions, 4)


def frq_5_check(grid, qlist):
    if grid[0, 1].value == qlist[4][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_5(self):
    frq_5_check(frq_5, frquestions)


frq_5[0, 2].on_click(check_frq_5)
# Question 6
frq_6 = create_frq(frquestions, 5)


def frq_6_check(grid, qlist):
    if grid[0, 1].value == qlist[5][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_6(self):
    frq_6_check(frq_6, frquestions)


frq_6[0, 2].on_click(check_frq_6)
# Question 7
frq_7 = create_frq(frquestions, 6)


def frq_7_check(grid, qlist):
    if grid[0, 1].value == qlist[6][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_7(self):
    frq_7_check(frq_7, frquestions)


frq_7[0, 2].on_click(check_frq_7)
# Question 8
frq_8 = create_frq(frquestions, 7)


def frq_8_check(grid, qlist):
    if grid[0, 1].value == qlist[7][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_8(self):
    frq_8_check(frq_8, frquestions)


frq_8[0, 2].on_click(check_frq_8)
# Question 9
frq_9 = create_frq(frquestions, 8)


def frq_9_check(grid, qlist):
    if grid[0, 1].value == qlist[8][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_9(self):
    frq_9_check(frq_9, frquestions)


frq_9[0, 2].on_click(check_frq_9)
# Question 10
frq_10 = create_frq(frquestions, 9)


def frq_10_check(grid, qlist):
    if grid[0, 1].value == qlist[9][1]:
        grid[0, 2].button_style = "success"
    else:
        grid[0, 2].button_style = "danger"


def check_frq_10(self):
    frq_10_check(frq_10, frquestions)


frq_10[0, 2].on_click(check_frq_10)

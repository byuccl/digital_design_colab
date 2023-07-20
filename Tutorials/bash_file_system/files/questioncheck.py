import os
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
frquestions = {
    "Q1": ["How many files are in the QuestionOne folder?", 5, "Question One"]
}


def check_frq(self):
    key = self.tooltip
    frq_check(key)


def create_frq_grids():
    frqs = {}
    i = 1
    for key in frquestions:
        if isinstance(frquestions[key][1], str):
            frqs[key] = [
                create_frq_string(frquestions, i),
                create_expanded_button(frquestions[key][2], "primary", "550px"),
            ]
        else:
            frqs[key] = [
                create_frq_int(frquestions, i),
                create_expanded_button(frquestions[key][2], "primary", "550px"),
            ]
        i += 1

    return frqs


frqs = create_frq_grids()


def frq_check(key):
    qlist = frquestions[key]
    if frqs[key][0][0, 1].value == qlist[1]:
        frqs[key][0][0, 2].button_style = "success"
    else:
        frqs[key][0][0, 2].button_style = "danger"


def print_frq_grid(question_number):
    key = "Q" + str(question_number)
    frqs[key][0][0, 2].on_click(check_frq)
    # Create the head tab
    # Display the widgets
    display(widgets.VBox([frqs[key][1], frqs[key][0]]))


# Question One FRQ Answer = 5
# Question 2. Check if Directory exists Create the directory plants in the QuestionTwo folder
def QuestionTwoCheck():
    return os.path.exists("/content/Questions/QuestionTwo/plants")


# Question 3 Create copy the QuestionOne folder into the QuestionThree folder with all of its contents. Keep the folder intact.
def QuestionThreeCheck():
    return (
        os.path.exists("/content/Questions/QuestionThree/QuestionOne")
        and os.path.isfile("/content/Questions/QuestionThree/QuestionOne/two.txt")
        and os.path.isfile("/content/Questions/QuestionOne/one.txt")
    )


# Rename the file "text.txt" that is in the QuestionFour folder to "q4.q4"
def QuestionFourCheck():
    return os.path.isfile(
        "/content/Questions/QuestionFour/q4.q4"
    ) and not os.path.isfile("/content/Questions/QuestionFour/text.txt")


# Print the contents of the Question One folder into QuestionFive into a new file called "q5.q5"
def QuestionFiveCheck():
    if not os.path.isfile("/content/Questions/QuestionFive/q5.q5"):
        return False
    with open("/content/Questions/QuestionFive/q5.q5", "r") as f:
        x = f.read()
        if x == f"bash.bash\nfile.file\none.txt\nthree.txt\ntwo.txt\num.sv\n":
            return True
        else:
            return False


# Create an empty file called "q6.q6" in QuestionSix folder
def QuestionSixCheck():
    return os.path.isfile("/content/Questions/QuestionSix/q6.q6")


# Remove the "text.txt" file in QuestionSeven directory
def QuestionSevenCheck():
    return not os.path.isfile("/content/Questions/QuestionSeven/q7.q7")


buttons = [
    create_expanded_button("Check 2","primary"),
    create_expanded_button("Check 3", "primary"),
    create_expanded_button("Check 4", "primary"),
    create_expanded_button("Check 5", "primary"),
    create_expanded_button("Check 6", "primary"),
    create_expanded_button("Check 7", "primary"),
]


def Button_On_Click(self):
    number = self.description[-1]
    x = False
    if number is 2:
        x = QuestionTwoCheck()
    elif number is 3:
        x = QuestionThreeCheck()
    elif number is 4:
        x = QuestionFourCheck()
    elif number is 5:
        x = QuestionFiveCheck()
    elif number is 6:
        x = QuestionSixCheck()
    elif number is 7:
        x = QuestionSevenCheck()

    if x:
        self.button_style = "success"
    else:
        self.button_style = "danger"


def print_button(question_number):
    key = question_number - 2
    buttons[key].on_click(Button_On_Click)
    # Create the head tab
    # Display the widgets
    display(buttons[key])

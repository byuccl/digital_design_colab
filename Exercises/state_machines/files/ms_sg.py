# @title Multiple Choice Creation
from IPython.display import IFrame, display, HTML
import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText, IntSlider

# function of creating button widget
def create_expanded_button(description, button_style, width="400px"):
    return Button(
        description=description,
        button_style=button_style,
        layout=Layout(height="auto", width=width),
    )


# function of creating grid layout
def create_grid(options):
    grid = GridspecLayout(len(options) + 1, 3, width="470px")
    index = 0
    LETTERS = "ABCDEFGHIJKLMNOP"
    for i in options:
        grid[index, 0] = create_expanded_button(i, "primary")
        setattr(grid[index, 0], "letter", LETTERS[index])
        index += 1
    grid[index, 0] = create_expanded_button("Submit", "warning")
    return grid


def check_answerms(self):
    """
    Used with .on_click to make sure the answer is correct
        self: This is a button. We have added 2 new attributes to it
        current_answer: This is the last clicked button and its description value stored as a str
        answer: This is the correct answer from the mcdict

    """
    if self.current_answers == {}:
        return
    for i in self.current_answers:
        if i not in self.answer:
            self.button_style = "Danger"
            self.description = "Wrong, Try Again!"
            return
    self.button_style = "Success"
    self.description = "Correct!"


"""
key: The question number
pair: This should be a list. indexes 0 - -3 are the choices. You can have up to 10 choices. -2 is the answer. -1 is the question
answer: This should be a string made up of the letters of the correct answers. For example, if the first and second answer are correct, the answer is "AB"
question: This is used as the header text
"""
ms_dict = {
    "1": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "E",
        "Which States are Complete?",
    ],
    "2": ["A", "B", "C", "D", "E", "ABCD", "Which States are Incomplete?"],
    "3": ["A", "B", "C", "D", "E", "ABCD", "Which States are Conflicting?"],
}


def multiple_select(key, dictionary):
    """
    Creates a multiple choice widget that has 4 options.
    key: This is the key to the dictionary. It will be a str of digits.
    dictionary: the dictionary used is ms_dict. Which houses the multiple choice answers.
    grid: The grid that has been set up and can be shown
    header_button: sets the header_button that houses the question description
    """

    answers = dictionary[key]
    question = answers[-1]
    grid = create_grid(answers[0:-2])
    correct_answer = answers[-2]
    setattr(grid[-1, 0], "answer", correct_answer)
    current_answer = 0
    # Set up empty grid
    current_answers = set()

    setattr(grid[-1, 0], "current_answers", current_answers)
    grid[-1, 0].button_style = "info"

    def change_color(self):
        current_btn = int(self.layout.grid_area[-1])
        # for i in range(0, len(answers)-2):
        #     grid[i, 0].button_style = "primary"
        if grid[current_btn - 1, 0].button_style == "primary":
            grid[current_btn - 1, 0].button_style = "warning"
        # switch it
        else:
            grid[current_btn - 1, 0].button_style = "primary"
        if grid[current_btn - 1, 0].letter in grid[-1, 0].current_answers:
            grid[-1, 0].current_answers.remove(grid[current_btn - 1, 0].letter)
        else:
            grid[-1, 0].current_answers.add(grid[current_btn - 1, 0].letter)

    for i in range(0, len(answers[0:-2])):
        grid[i, 0].on_click(change_color)
    grid[-1, 0].on_click(check_answerms)
    header_button = create_expanded_button(question, "info", "465px")
    return grid, header_button


def create_ms_grids():
    ms_grids = {}
    i = 1
    for key in ms_dict:
        ms_grids[key] = multiple_select(key, ms_dict)
        i += 1
    return ms_grids


ms_grids = create_ms_grids()


def print_ms_grid(question_number):
    key = str(question_number)
    # Create the head tab
    widgets.VBox(
        [
            widgets.HTML(value="<span id='something'></span>"),
            AppLayout(header=ms_grids[key][1], footer=None),
            ms_grids[key][0],
        ]
    )
    display(widgets.VBox([ms_grids[key][1], ms_grids[key][0]]))

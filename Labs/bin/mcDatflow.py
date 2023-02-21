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
def create_grid(A, B, C, D):
    grid = GridspecLayout(5, 3, width="470px")
    grid[0, 0] = create_expanded_button(A, "primary")
    grid[1, 0] = create_expanded_button(B, "primary")
    grid[2, 0] = create_expanded_button(C, "primary")
    grid[3, 0] = create_expanded_button(D, "primary")
    grid[4, 0] = create_expanded_button("Submit", "Danger")
    return grid


def check_answermc4(self):
    """
    Used with .on_click to makesure the answer is correct
      self: This is a button. We have added 2 new attributes to it
        current_answer: This is the last clicked button and its description value stored as a str
        answer: This is the correct answer from the mcdict

    """
    if self.current_answer == 0:
        return
    if self.answer[0] == self.current_answer[0]:
        self.button_style = "Success"
        self.description = "Correct!"
    else:
        self.button_style = "Danger"
        self.description = "Wrong, Try Again!"


"""
key: The question number
pair: This should be a list. indexes 0-3 are the choices. 4 is the answer. 5 is the question
answer: This must be the same str value as the choice
question: This is used in the header
"""
mc_dict = {
    "1": [
        "A. 0101",
        "B. 01010",
        "C. 1010",
        "D. Syntax Error",
        "A",
        "What is the value of A[5:2] where A = 9’b101010101?",
    ],
    "2": [
        "A. 11010",
        "B. 10100",
        "C. 10111",
        "D. 01000",
        "D",
        "What is the value of A << 3 where A  = 5’b11101 ?",
    ],
    "3": [
        "A. 10111",
        "B. 11101",
        "C. 101",
        "D. Syntax Error",
        "A",
        "What is the Value of {A,B} where A = 3’b101 and B = 2’11?",
    ],
    "4": [
        "A. 1010",
        "B. 111000",
        "C. 101010",
        "D. Syntax Error",
        "C",
        "What is the value of {3{2’b10}}?",
    ],
    "5": [
        "A.logic input [3:0] x",
        "B. logic [3:0] input x",
        "C. input logic x [3:0]",
        "D. input logic [3:0] x",
        "D",
        "Which signal is defined correctly?",
    ],
    "6": [
        "A 1’b1",
        "B. 1’b0",
        "C. An Error will be thrown",
        "D. Undefined",
        "C",
        "What is the value of x from the code above?",
    ],
    "7": [
        "A. 1’b1",
        "B. 1’b0",
        "C. 2’b11",
        "D. An Error will be thrown",
        "A",
        "What is the value of x from the above code?",
    ],
    "8": [
        "A. 4'b0001",
        "B. 4'b0011",
        "C. 4'b0111",
        "D. 4'b1001",
        "D",
        "What is the value of x in the above code?",
    ],
}


def multiple_choice4(key, dictionary):
    """
    Creates a multiple choice widget that has 4 options.
    key: This is the key to the dictionary. It will be a str of digits.
    dictionary: the dictionary used is mc_dict. Which houses the multiple choice answers.
    grid: The grid that has been set up and can be shown
    header_button: sets the header_button that houses the question description
    """
    answers = dictionary[key]
    question = answers[5]
    A = answers[0]
    B = answers[1]
    C = answers[2]
    D = answers[3]
    grid = create_grid(A, B, C, D)
    correct_answer = answers[4]
    setattr(grid[4, 0], "answer", correct_answer)
    current_answer = 0
    setattr(grid[4, 0], "current_answer", 0)
    grid[4, 0].button_style = "Warning"

    def change_color(self):
        current_btn = int(self.layout.grid_area[-1])
        for i in range(0, 4):
            grid[i, 0].button_style = "primary"
        grid[current_btn - 1, 0].button_style = "info"
        grid[4, 0].current_answer = self.description

    for i in range(0, 4):
        grid[i, 0].on_click(change_color)
    grid[4, 0].on_click(check_answermc4)
    header_button = create_expanded_button(question, "info", "465px")
    return grid, header_button

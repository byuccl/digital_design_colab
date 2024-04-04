import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText, IntSlider

"""
Holds the values for the truth tables.
Structure:
------------
    key: Q + question number.
List 
    [0] : The number of inputs
    [1] : Equation of truth table 
    [2] : The correct answer, MSB is the top row
"""
tt = {}
tt_grids = {}

def create_tt_dictionary(tt_input):
   global tt, tt_grids
   tt = tt_input; 
   tt_grids = create_tt_grids()



def create_expanded_button(description, button_style, width="100px", tooltip=""):
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


# creates variable grid size
def create_grid(questionNumber):
    """
    Returns a grid for the Truth Table. Autosizes the gride to much the number of inputs
    - num_input = number of inputs in the function. Can be from 1 to 4.
    - input_string = a string of all the default values and input names that are passed in (ex: AB000011011)
    """

    tooltip = f"Q%d" % questionNumber
    num_input = tt[tooltip][0]
    input_string = ""
    question_string = ""
    if num_input == 1:
        input_string = "A01"
        question_string = "f(A) ="
    elif num_input == 2:
        input_string = "AB00011011"
        question_string = "f(A,B) ="
    elif num_input == 3:
        question_string = "f(A,B,C) ="
        input_string = "ABC000001010011100101110111"
    elif num_input == 3 :
        question_string = "f(A,B,S) ="
        input_string = "ABS000001010011100101110111"
    elif num_input == 4:
        question_string = "f(A,B,C,D) = "
        input_string = (
            "ABCD0000000100100011010001010110011110001001101010111100110111101111"
        )

    num_row = int((2**num_input) + 1)
    num_col = num_input + 2
    grid = GridspecLayout(num_row, num_col, width=str(num_col * 117.5) + "px")

    # creates the default values for the different input combos of the truth table
    for i in range(0, num_row):
        for j in range(0, num_input):
            val = str(input_string[0])
            grid[i, j] = create_expanded_button(val, "info")
            input_string = input_string[1:]

    # creates the click to check button as well as the userinput section of the table
    for i in range(1, num_row):
        grid[i, num_input] = widgets.BoundedIntText(
            min=0, max=1, layout=Layout(height="auto", width="100px")
        )
        grid[0, num_col - 1] = create_expanded_button(
            "Click to Check", "warning", width="150px", tooltip=tooltip
        )

    # creates the output section of the truth table to know if you're right or not
    for i in range(1, num_row):
        grid[i, num_col - 1] = create_expanded_button(" ", "warning", width="150px")

    grid[0, num_input] = create_expanded_button(question_string, "info")

    header_button = create_expanded_button(tt[tooltip][1], "info", "466px")

    return grid, header_button


def CheckAnswer(grid, num_inputs, input):
    """
    Checks each input box and sees if it matches the answer. Then Tells the user which rows were wrong.
    Parameters
    ------
    grid: The grid to be checked
    num_inputs: The size of the grid, the number of inputs of the function.
    input: The answer to the truth table

    """
    for i in range(0, len(input)):
        if grid[i + 1, num_inputs].value == int(input[i]):
            grid[i + 1, num_inputs + 1].button_style = "Success"
            grid[i + 1, num_inputs + 1].description = "Correct!"
        else:
            grid[i + 1, num_inputs + 1].button_style = "Danger"
            grid[i + 1, num_inputs + 1].description = "Wrong! Submit again"


"""
Create each Truth Table as a grid object. These can then be called from the notebook.
"""


def create_tt_grids():
    tt_grids = {}
    i = 1
    for key in tt:
        tt_grids[key] = create_grid(i)
        i += 1
    return tt_grids





def on_button_clicked(self):
    CheckAnswer(tt_grids[self.tooltip][0], tt[self.tooltip][0], tt[self.tooltip][2])


def print_tt_grid(question_number):
    key = "Q" + str(question_number)
    tt_grids[key][0][0, -1].on_click(on_button_clicked)
    # Create the head tab
    # Display the widgets
    display(widgets.VBox([tt_grids[key][1], tt_grids[key][0]]))

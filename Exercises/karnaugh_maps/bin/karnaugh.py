import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import (
    AppLayout,
    Button,
    Layout,
    jslink,
    IntText,
    IntSlider,
    ButtonStyle,
)

"""
Holds the values for the truth tables.
Structure:
------------
    key: Q + question number.
List 
    [0] : The number of inputs
    [1] : The correct answer, MSB is the top row
"""
km = {
    "Q1": [2, "A'*B + A'+B'", "1110"],
    "Q2": [3, "ABC + B'C + A'C'", "11100101"],
    "Q3": [3, "A'B'C + AC + BC", "01010101"],
    "Q4": [4, "ABCD' + A'BCD' + BC'D + B +  BC'D' + C'D", "0100111101001111"],
}


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
def create_three_highlight(questionNumber):
    """
    Returns a grid for the Truth Table. Autosizes the gride to much the number of inputs
    - num_input = number of inputs in the function. Can be from 1 to 4.
    - input_string = a string of all the default values and input names that are passed in (ex: AB000011011)
    """

    corner = "   A\BC"
    column_headers = ["B'C'", "B'C", "BC", "BC'"]
    row_headers = ["A'", "A"]

    tooltip = f"Q%d" % questionNumber
    num_row = 4
    num_col = 6
    grid = GridspecLayout(num_row, num_col, width=str(num_col * 117.5) + "px")

    def change_color(self):
        if self.description == "1":
            self.style = ButtonStyle(button_color="Green")
            self.description = "0"
        else:
            self.style = ButtonStyle(button_color="Yellow")
            self.description = "1"

    # Creates the first column
    for i in range(2, num_row):
        val = row_headers[i - 2]
        grid[i, 1] = create_expanded_button(val, "primary")
    # Creates the first row
    for i in range(1, num_col - 1):
        val = column_headers[i - 1]
        grid[1, i] = create_expanded_button(val, "primary")

    # creates the click to check button as well as the userinput section of the table
    for i in range(2, num_row):
        for j in range(1, num_col):
            grid[i, j] = create_expanded_button("0", "info")
            grid[i, j].on_click(change_color)
    grid[0, num_col - 1] = create_expanded_button(
        "Click to Check", "warning", width="150px", tooltip=tooltip
    )

    # creates the output section of the truth table to know if you're right or not
    for i in range(1, num_row):
        grid[i, num_col - 1] = create_expanded_button(" ", "warning", width="150px")
    grid[1, 0] = create_expanded_button(corner, "info", width="100px")

    # Ability To Choose
    grid[0, 1] = create_expanded_button("0", "info", width="100px")
    grid[0, 2] = create_expanded_button("1", "info", width="100px")
    grid[0, 3] = create_expanded_button("1", "info", width="100px")
    grid[0, 4] = create_expanded_button("1", "info", width="100px")

    header_button = create_expanded_button(
        km[tooltip][1], "info", str(num_col * 117.5) + "px"
    )

    return grid, header_button


def create_three_grid(questionNumber):
    """
    Returns a grid for the Truth Table. Autosizes the gride to much the number of inputs
    - num_input = number of inputs in the function. Can be from 1 to 4.
    - input_string = a string of all the default values and input names that are passed in (ex: AB000011011)
    """

    corner = "   A\BC"
    column_headers = ["B'C'", "B'C", "BC", "BC'"]
    row_headers = ["A'", "A"]

    tooltip = f"Q%d" % questionNumber
    num_row = 3
    num_col = 6
    grid = GridspecLayout(num_row, num_col, width=str(num_col * 117.5) + "px")

    def change_color(self):
        if self.description == "1":
            self.style = ButtonStyle(button_color="Green")
            self.description = "0"
        else:
            self.style = ButtonStyle(button_color="Yellow")
            self.description = "1"

    # Creates the first column
    for i in range(1, num_row):
        val = row_headers[i - 1]
        grid[i, 0] = create_expanded_button(val, "primary")
    # Creates the first row
    for i in range(1, num_col - 1):
        val = column_headers[i - 1]
        grid[0, i] = create_expanded_button(val, "primary")

    # creates the click to check button as well as the userinput section of the table
    for i in range(1, num_row):
        for j in range(1, num_col):
            grid[i, j] = create_expanded_button("0", "info")
            grid[i, j].on_click(change_color)
    grid[0, num_col - 1] = create_expanded_button(
        "Click to Check", "warning", width="150px", tooltip=tooltip
    )

    # creates the output section of the truth table to know if you're right or not
    for i in range(1, num_row):
        grid[i, num_col - 1] = create_expanded_button(" ", "warning", width="150px")
    grid[0, 0] = create_expanded_button(corner, "info", width="150px")
    header_button = create_expanded_button(
        km[tooltip][1], "info", str(num_col * 117.5) + "px"
    )

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


def create_km_grids():
    km_grids = {}
    i = 1
    for key in tt:
        km_grids[key] = create_grid(i)
        i += 1
    return km_grids


km_grids = create_km_grids()


def on_button_clicked(self):
    CheckAnswer(km_grids[self.tooltip][0], km[self.tooltip][0], km[self.tooltip][2])


def print_km_grid(question_number):
    key = "Q" + str(question_number)
    km_grids[key][0][0, -1].on_click(on_button_clicked)
    # Create the head tab
    # Display the widgets
    display(widgets.VBox([km_grids[key][1], km_grids[key][0]]))

import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText, IntSlider

# function of creating button widget
def create_expanded_button(description, button_style, width="100px"):
    return Button(
        description=description,
        button_style=button_style,
        layout=Layout(height="auto", width=width),
    )


# creates variable grid size
def create_grid(num_input, input_string, func):
    """
    - num_input = number of inputs in the function
    - input_string = a string of all the default values and input names that are passed in (ex: AB000011011)
    """
    num_row = (2**num_input) + 1
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
            "Click to Check", "warning", width="150px"
        )

    # creates the output section of the truth table to know if you're right or not
    for i in range(1, num_row):
        grid[i, num_col - 1] = create_expanded_button(" ", "warning", width="150px")

    grid[0, num_input] = create_expanded_button(func, "info")
    return grid


# checks if the user input is correct
def CheckAnswer(grid, num_inputs, input):
    for i in range (0,len(input)):
        if grid[i + 1, num_inputs].value == int(input[i]):
            grid[i + 1, num_inputs + 1].button_style = "Success"
            grid[i + 1, num_inputs + 1].description = "Correct!"
        else:
            grid[i + 1, num_inputs + 1].button_style = "Danger"
            grid[i + 1, num_inputs + 1].description = "Wrong! Submit again"


# populates default input values
def populate():
    pass

# AND gate truth table creation
grid1_1 = create_grid(2, 'AB00011011', 'F=AB')

# OR gate truth table creation
grid1_2 = create_grid(2, 'AB00011011', 'F=A+B')

# NOT gate truth table creation
grid1_3 = create_grid(1, "A01", '!A')

# NOR gate truth table creation
grid1_4 = create_grid(2, 'AB00011011', 'F=NOR')

# NAND gate truth table creatione
grid1_5 = create_grid(2, 'AB00011011', 'F=NAND')

# XOR gate truth table creation
grid1_6 = create_grid(2, 'AB00011011', 'F=A^B')

# XNOR gat truth table creatione
grid1_7 = create_grid(2, 'AB00011011', 'F=~(A^B)')

# Harder question
grid1_8 = create_grid(3,'ABC000001010011100101110111', 'F=!(AC)|(BA)')

# THIS CAN PROBABLY BE PLACED IN THE CREATE FUNCTION WITH F AS AN ARGUMENT ABCF 000 001 010 011 100 101 110 111


# LOOK INTO HAVING THE CHECK ANSWER BUTTON DO DIFFERENT THINGS
# DON'T LIKE THIS IMPLEMENTATION. Find a way to only need one 'on_button_clicked' function

# Process when clicking the "Check" button
# AND
def on_button_clicked(self):
    CheckAnswer(grid1_1, 2, '0001')


# OR
def on_button_clicked2(self):
    CheckAnswer(grid1_2, 2, '0111')

# NOT
def on_button_clicked3(self):
    CheckAnswer(grid1_3, 1, '10')

# NOR
def on_button_clicked4(self):
    CheckAnswer(grid1_4, 2, '1000')

# NAND
def on_button_clicked5(self):
    CheckAnswer(grid1_5, 2, '1110')

# XOR
def on_button_clicked6(self):
    CheckAnswer(grid1_6, 2, '0110')

# XNOR
def on_button_clicked7(self):
    CheckAnswer(grid1_7, 2, '1001')

def on_button_clicked8(self):
    CheckAnswer(grid1_8, 3, '11111011')

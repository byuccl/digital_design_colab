"""
Holds the values for the truth tables.
Structure:
------------
    key: Q + question number.
List 
    [0] : The number of inputs
    [1] : The correct answer, MSB is the top row
"""
tt = {
    "Q1": [3, "none", "01001100"],
}

tt_ff = {
    "Q1": [3, "Flip Flop", "01001122"],
}

def get_tt_data():
    return tt_ff
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
    "Q1": [3., "2:1 MUX Table, with A, B, S inputs", "00011011"],
}

def get_tt_data():
    return tt
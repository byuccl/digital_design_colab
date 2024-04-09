"""
Holds the values for the truth tables.
Structure:
------------
    key: Q + question number.
List 
    [0] : The number of inputs
    [1] : The correct answer, MSB is the top row
    [2] : specifices questions with different types but same inputs
"""
tt = {
    "Q1": [3, "2:1 MUX Table, with A, B, S inputs", "00011011", "ABS"],
    # Rest of the dictionary...
}

def get_tt_data():
    return tt
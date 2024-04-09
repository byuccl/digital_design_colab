
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
tt = {
    "Q1": [2, "And Gate", "0001", "AB"],
    "Q2": [2, "Or Gate", "0111", "AB"],
    "Q3": [1, "Not Gate", "10", "A"],
    "Q4": [2, "Nand Gate", "1110", "AB"],
    "Q5": [2, "Nor Gate", "1000", "AB"],
    "Q6": [2, "Xor Gate", "0110", "AB"],
    "Q7": [2, "Xnor Gate", "1001", "AB"],
}

def get_tt_data():
    return tt



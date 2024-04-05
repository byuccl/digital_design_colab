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
    "Q1": [2, "A' * B + A' + B'", "1110", "AB"],
    "Q2": [3, "ABC + B'C + A'C'", "11100101", "ABC"],
    "Q3": [3, "A'B'C + AC + BC", "01010101", "ABC"],
    "Q4": [4, "ABCD' + A'BCD' + BC'D + B +  BC'D' + C'D", "0100111101001111", "ABCD"],
}

def get_tt_data():
    return tt
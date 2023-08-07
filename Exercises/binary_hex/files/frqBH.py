"""
The dictionary that holds the questions and the answers.
Answers can be String or Int type. This does change the function used to create the grid object as shown
"""
frquestions = {
    "Q1": ["Convert this binary number to decimal: 10110", 22],
    "Q2": ["Convert this binary number to decimal: 10001", 17],
    "Q3": ["Convert this binary number to decimal: 101011", 43],
    "Q4": ["Convert this decimal number to binary: 9", 1001],
    "Q5": ["Convert this decimal number to binary: 21", 10101],
    "Q6": ["Convert this decimal number to binary: 63", 111111],
    "Q7": ["Convert this hexadecimal number to decimal: A3E", 2622],
    "Q8": ["Convert this hexadecimal number to binary: 5B", 1011011],
    "Q9": ["Convert this hexadecimal number to binary: C9", 11001001],
    "Q10": ["Convert this decimal number to hexadecimal: 137", 89],
    "Q11": ["Convert this binary number to hexadecimal: 10000011 ", 83],
    "Q12": ["Convert this binary number to hexadecimal: 1011111011101111", "BEEF"],
}

def get_data():
    return frquestions

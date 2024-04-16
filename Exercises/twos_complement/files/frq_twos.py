"""
The dictionary that holds the questions and the answers.
Answers can be String or Int type. This does change the function used to create the grid object as shown
The key is Q + Question Index. 
"""
frquestions = {
    "Q1": [
        "What integer does this sign-magnitude number represent? `10101`",
        -5,
        "Question 1",
    ],
    "Q2": [
        "What integer does this sign-magnitude number represent? `01110`?",
        14,
        "Question 2",
    ],
    "Q3": [
        "What integer does this two's complement number represent? `10101`",
        -11,
        "Question 3",
    ],
    "Q4": [
        "What integer does this two's complement number represent? `01110`",
        14,
        "Question 4",
    ],
    "Q5": [
        "What integer represents the inverse of the two's complement number? `10101`",
        11,
        "Question 5",
    ],
    "Q6": [
        "What integer represents the inverse of the twos complement number? `01110`",
        -14,
        "Question 6",
    ],
    "Q7": ["What is `1011` sign extended to 8 bits wide?", 11111011, "Question 7"],
    "Q8": ["What is `0001` sign extended to 8 bits wide?", 1, "Question 8"],
}

def get_data():
    return frquestions


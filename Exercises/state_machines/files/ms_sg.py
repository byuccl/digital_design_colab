"""
key: The question number
pair: This should be a list. indexes 0 - -3 are the choices. You can have up to 10 choices. -2 is the answer. -1 is the question
answer: This should be a string made up of the letters of the correct answers. For example, if the first and second answer are correct, the answer is "AB"
question: This is used as the header text
"""
ms_dict = {
    "1": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "E",
        "Which States are Complete?",
    ],
    "2": ["A", "B", "C", "D", "E", "ABCD", "Which States are Incomplete?"],
    "3": ["A", "B", "C", "D", "E", "ABCD", "Which States are Conflicting?"],
}

def get_data():
    return ms_dict


# @title Multiple Choice Creation
"""
key: The question number
pair: This should be a list. indexes 0-3 are the choices. 4 is the answer. 5 is the question
answer: This must be the same str value as the choice
question: This is used in the header
"""
mc_dict = {
    "1": [
        ["A. A' * B",
        "B. A' + B",
        "C. A' + B",
        "D. A' + B'",],
        "D",
        "Which of the following match the truth table?",
    ],
    "2": [
        ["A. BC + AC",
        "B. A'B + AB",
        "C. AC + A'B",
        "D. AB' + AC",],
        "C",
        "Which of the following match the truth table?",
    ],
    "3": [
        ["A. A' + B'C'",
        "B. A'C + A'B' + C",
        "C. A'C + A'B + B'C'",
        "D. A'B + B'C'",],
        "D",
        "Which of the following match the truth table?",
    ],
    "4": [
        ["A. ABCD + A'B'C",
        "B. ABCD'+AB",
        "C. CD + ABD'",
        "D. AD' + ABC",],
        "C",
        "Which of the following match the truth table?",
    ],
}


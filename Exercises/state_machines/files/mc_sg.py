"""
key: The question number
pair: This should be a list. indexes 0-3 are the choices. 4 is the answer. 5 is the question
answer: This must be the same str value as the choice
question: This is used in the header
"""
mc_dict = {
    "1": [
        ["A. This will cause a conflict",
        "B. The state is incomplete and will cause a latch",
        "C. The State is Correct",
        "D. Syntax Error will be thrown", 
        "E, this is a test],
        "A",
        "For the code above, is there an error?",
    ],
    "2": [
        ["A. This will cause a conflict",
        "B. The state is incomplete and will cause a latch",
        "C. The State is Correct",
        "D. Syntax Error will be thrown"],
        "D",
        "For the code above, is there an error?",
    ],
    "3": [
        ["A. This will cause a conflict",
        "B. The state is incomplete and will cause a latch",
        "C. The State is Correct",
        "D. Syntax Error will be thrown"],
        "A",
        "For the code above, is there an error?",
    ],
    "4": [
        ["A. This will cause a conflict",
        "B. The state is incomplete and will cause a latch",
        "C. The State is Correct",
        "D. Syntax Error will be thrown"],
        "C",
        "For the code above, is there an error?",
    ],
}

def get_data():
  return mc_dict


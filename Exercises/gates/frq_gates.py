"""
The dictionary that holds the questions and the answers.
Answers can be String or Int type. This does change the function used to create the grid object as shown
The key is Q + Question Index. 
"""
frquestions = {
    "Q1": ["What is the output if A=1, B=1, C=0", "1", "Question 1"],
    "Q2": ["What is the output if A=1, B=0, C=1", "0", "Question 2"],
    "Q3": ["What is the output if A=0, B=0, C=0", "1", "Question 3"],
    "Q4": ["What is the output if A=0, B=1, C=1", "0", "Question 4"],
    "Q5": ["What is the output if A=0, B=0, C=0, D=1", "1", "Question 5"],
    "Q6": ["What is the output if A=1, B=0, C=1, D=0", "0", "Question 6"],
}

def get_data():
    return frquestions

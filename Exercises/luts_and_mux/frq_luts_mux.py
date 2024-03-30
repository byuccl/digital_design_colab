"""
The dictionary that holds the questions and the answers.
Answers can be String or Int type. This does change the function used to create the grid object as shown
The key is Q + Question Index. 
"""
frquestions = {
    "Q1": ["How Many 2:1 Muxes are need to implement an 8:1 MUX?", 7, "Question 1"],
    "Q2": ["To implement If/Else logic, what should be used?", "MUX", "Question 2"],
    "Q3": [
        "To implement an arbitrary function what should be used?",
        "LUT",
        "Question 3",
    ],
    "Q4": ["How many total input signals would an 8:1 MUX have including select signals?", 11, "Question 4"],
    "Q5": ["How many 2:1 muxes are needed to implement an 8:1 mux", 6, "Question 5"],
    "Q6": [
        "With 4 select signals, how many different values could a LUT hold?",
        16,
        "Question 6",
    ],
}

def get_data():
    return frquestions


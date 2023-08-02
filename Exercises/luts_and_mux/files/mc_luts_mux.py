"""
key: The question number
pair: This should be a list. indexes 0-3 are the choices. 4 is the answer. 5 is the question
answer: This must be the same str value as the choice
question: This is used in the header
"""
mc_dict = {
    "1": [
        ["A. MUX",
        "B. LUT",
        "C. Not Possible",
        "D. A and B"],
        "A",
        "What should be used to implement an if/else statement?",
    ],
    "2": [
        ["A. MUX",
        "B. LUT",
        "C. Not Possible",
        "D. A and B"],
        "B",
        "What should primarily be used to implement the memory of a function?",
    ],
    "3": [
        ["A. 10111",
        "B. 11101",
        "C. 101",
        "D. Syntax Error"],
        "A",
        "What is the Value of {A,B} where A = 3’b101 and B = 2’11?",
    ],
    "4": [
        ["A. 1010",
        "B. 111000",
        "C. 101010",
        "D. Syntax Error"],
        "C",
        "What is the value of {3{2’b10}}?",
    ],
    "5": [
        ["A.logic input [3:0] x",
        "B. logic [3:0] input x",
        "C. input logic x [3:0]",
        "D. input logic [3:0] x"],
        "D",
        "Which signal is defined correctly?",
    ],
    "6": [
        ["A 1’b1",
        "B. 1’b0",
        "C. An Error will be thrown",
        "D. Undefined"],
        "C",
        "What is the value of x from the code above?",
    ],
    "7": [
        ["A. 1’b1",
        "B. 1’b0",
        "C. 2’b11",
        "D. An Error will be thrown"],
        "A",
        "What is the value of x from the above code?",
    ],
    "8": [
        ["A. 4'b0001",
        "B. 4'b0011",
        "C. 4'b0111",
        "D. 4'b1001"],
        "D",
        "What is the value of x in the above code?",
    ],
}

def get_data():
  return mc_dict

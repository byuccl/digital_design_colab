"""
key: The question number
pair: [List of all the options, can be any length], Answer(This must be the same str value as the choice), Question
"""
mc_dict = {

    "1": [["A. 0101","B. 01010", "C. 1010","D. Syntax Error"], "A", "What is the value of A[5:2] where A = 9’b101010101?"],
    "2": [["A. 11010", "B. 10100", "C. 10111", "D. 01000"], "B", "What is the value of A << 3 where A  = 5’b11101 ?"],
    "3": [["A. 10111", "B. 11101", "C. 101", "D. Syntax Error"], "A", "What is the Value of {A,B} where A = 3’b101 and B = 2’11?"],
    "4": [["A. 1010", "B. 111000", "C. 101010", "D. Syntax Error"], "C", "What is the value of {3{2’b10}}?"],
    "5": [["A.logic input [3:0] x", "B. logic [3:0] input x", "C. input logic x [3:0]"], "D. input logic [3:0] x", "D", "Which signal is defined correctly?"  ],
    "6": [["A 1’b1", "B. 1’b0", "C. An Error will be thrown", "D. Undefined"], "C", "What is the value of x from the code above?"],
    "7": [["A. 1’b1", "B. 1’b0", "C. 2’b11", "D. An Error will be thrown"], "A", "What is the value of x from the above code?"] ,
    "8": [["A. 4'b0001", "B. 4'b0011", "C. 4'b0111", "D. 4'b1001"], "D", "What is the value of x in the above code?" ]
}

def get_data():
  return mc_dict

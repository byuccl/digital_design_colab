"""
The dictionary that holds the questions and the answers.
Answers can be String or Int type. This does change the function used to create the grid object as shown
The key is Q + Question Index. 
"""
frquestions = {
    "Q1":["What is the value of 4'b1011&4'b1001?", 1001, "Qestion 1"],
    "Q2":["What is the output of 4’b1001|4’b1011?", 1011, "Question 2"],
    "Q3":["What is the output of 4’b1001^4b’1011?", 10, "Question 3"],
    "Q4":["What is the output of 4’b1001&&4’b1011?", 1, "Question 4"],
    "Q5":["What is the output of 4’b1001||4’b1011?", 1, "Question 5"],
    "Q6":["What is the output of 4’b1001^^4’b1011?", 0, "Question 6"],
    "Q7":["What is &4’b1011?", 0, "Question 7"],
    "Q8":["What is |4’b1011?", 1, "Question 8"],
    "Q9":["What is ^4’b1011?", 1, "Question 9"],
    "Q10":["What is !4b’1011?", 0, "Question 10"]

}

def get_data():
    return frquestions




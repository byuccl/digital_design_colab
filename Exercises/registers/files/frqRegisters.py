"""
The dictionary that holds the questions and the answers.
Answers can be String or Int type. This does change the function used to create the grid object as shown
The key is Q + Question Index. 
"""
# frquestions = {"Q1": ["Example Question", "Answer", "Title"]}
frquestions = {"Q1": ["What is the value of Q at time 3?", "1", "Question 1"],
               "Q2": ["What is the value of Q at time 4?", "2", "Question 2"],
               "Q3": ["What is the value of Q at time 5?", "2", "Question 3"],
               "Q4": ["What is the value of Q at time 6?", "0", "Question 4"],
               "Q5": ["What is the value of Q at time 7?", "1", "Question 5"],
               "Q6": ["What time interval does the first falling edge of Q occur?", "6-7", "Question 6"],
               "Q7": ["What time interval does the first rising edge of Q' occur?", "6-7", "Question 7"],
               "Q8": ["What time interval does the next rising edge of Q occur?", "7-8", "Question 8"],
               "Q9": ["What time interval does the next falling edge of Q' occur?", "8-9", "Question 9"],
}

def get_data():
    return frquestions


"""
The dictionary that holds the questions and the answers.
Answers can be String or Int type. This does change the function used to create the grid object as shown
The key is Q + Question Index. 
"""
frquestions = {
    "Q1": ["In KHZ:", 200, "If the period is 5 microseconds what is the frequency?"],
    "Q2": ["In MHZ:", 40, "If the period is 25 ns what is the frequency? "],
    "Q3": ["In ns:", "0.1", "If the frequency is 10 GHZ what is the period?"],
    "Q4": ["In ms:", 40, "If the frequency is 25 Hz what is the period?"],
    "Q5": ["In ns", 10, "If the frequency of the Clock is 100 MHZ, what is the period?"],
    "Q6": ["Number of clock cycles:", 10000000, "Using the same clock frequency as the last question, how many clock cycles occur in 1/10th of a second?"],
    "Q6": ["Number of clock cycles:", 10000000, "Using the same clock from Q5, how many clock cycles occur in 1/10th of a second?"],
}

def get_data():
    return frquestions


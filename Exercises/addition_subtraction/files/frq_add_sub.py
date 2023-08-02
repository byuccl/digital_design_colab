"""
The dictionary that holds the questions and the answers.
Answers can be String or Int type. This does change the function used to create the grid object as shown
The key is Q + Question Index. 
"""
frquestions = {
    "Q1": ["What is `1001` + `0110` in Binary? (Its unsigned)", 1111, "Question 1"],
    "Q2": ["What is `0111` + `0011` in Binary? (Its unsigned)", 1010, "Question 2"],
    "Q3": [
        "What is `1010101`+0101101` in Binary? (Its unsigned)",
        10000010,
        "Question 3",
    ],
    "Q4": [
        "What is the value of `1111` + `0100`? (Put 9999 for overflow)",
        9999,
        "Question 4",
    ],
    "Q5": [
        "What is the value of `1010` + `0111`? (Put 9999 for overflow)",
        9999,
        "Question 5",
    ],
    "Q6": ["What is `1001` + `0110` in Binary? (2's complement)", 1111, "Question 6"],
    "Q7": ["What is `0111` + `0011` in Binary? (2's complement)", 1010, "Question 7"],
    "Q8": [
        "What is `1010101`+0101010` in Binary? (2's complement)",
        1111111,
        "Question 8",
    ],
    "Q9": ["What is `1100` - `1001` in Binary? (2's complement)", 11, "Question 9"],
    "Q10": ["What is `0111` - `0011` in Binary? (2's complement)", 100, "Question 10"],
}

def get_data():
    return frquestions

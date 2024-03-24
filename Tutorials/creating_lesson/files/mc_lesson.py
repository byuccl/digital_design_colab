# if you want questions where the question is a table and you select the correct answer use mcTemplate:

#create an mc.py python file of this form and add it to the files directory.

# """
# key: The question number
# pair: [List of all the options, can be any length], Answer(This must be the same str value as the choice), Question
# """
# mc_dict = {
#     "1": [
#         ["A. Option 1",
#         "B .Option 2",
#         "C. Option 3",
#         "D. Option 4",],
#         "the correct answer",
#         "The question",
#     ],
#     an example is provided below:
#     "2": [
#         ["A. BC + AC",
#         "B. A'B + AB",
#         "C. AC + A'B",
#         "D. AB' + AC",],
#         "C",
#         "Which of the following match the truth table?",
#     ],
# }


# def get_data():
#   return mc_dict


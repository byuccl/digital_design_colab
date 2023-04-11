import os

# Question One FRQ Answer = 5
# Question 2. Check if Directory exists Create the directory plants in the QuestionTwo folder
def QuestionTwoCheck():
    return os.path.exists("/content/Questions/QuestionTwo/plants")


# Question 3 Create copy the QuestionOne folder into the QuestionThree folder with all of its contents. Keep the folder intact.
def QuestionThreeCheck():
    return (
        os.path.exists("/content/Questions/QuestionThree/QuestionOne")
        and os.path.isfile("/content/Questions/QuestionThree/QuestionOne/two.txt")
        and os.path.isfile("/content/Questions/QuestionOne/one.txt")
    )


# Rename the file "text.txt" that is in the QuestionFour folder to "q4.q4"
def QuestionFourCheck():
    return os.path.isfile(
        "/content/Questions/QuestionFour/q4.q4"
    ) and not os.path.isfile("/content/Questions/QuestionFour/text.txt")


# Print the contents of the Question One folder into QuestionFive into a new file called "q5.q5"
def QuestionFiveCheck():
    if not os.path.isfile("/content/Questions/QuestionFive/q5.q5"):
        return False
    with open("/content/Questions/QuestionFive/q5.q5", "r") as f:
        x = f.read()
        if x == f"bash.bash\nfile.file\none.txt\nthree.txt\ntwo.txt\num.sv\n":
            return True
        else:
            return False


# Create an empty file called "q6.q6" in QuestionSix folder
def QuestionSixCheck():
    return os.path.isfile("/content/Questions/QuestionSix/q6.q6")


# Remove the "text.txt" file in QuestionSeven directory
def QuestionSevenCheck():
    return not os.path.isfile("/content/Questions/QuestionSeven/q7.q7")

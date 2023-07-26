# @title Multiple Choice Creation
from IPython.display import IFrame, display, HTML
import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText, IntSlider
import mcTemplate

mc_dict = {}
mc_grids = {}

# Create multiple choice dictionary used by other functions 
# def create_mc_dict(numbers, questions, options, answers):
#     global mc_dict, mc_grids
#     for i in range(len(numbers)):
#         mc_dict[numbers[i]] = [options[i], answers[i], questions[i]]
#     mc_grids = create_mc_grids()

def create_mc_dict(dictionary):
    global mc_dict, mc_grids
    mc_dict = dictionary
    mc_grids = create_mc_grids()
   

# function of creating button widget
def create_expanded_button(description, button_style, width="400px"):
    return Button(
        description=description,
        button_style=button_style,
        layout=Layout(height="auto", width=width),
    )

# function of creating grid layout
def create_grid(options):
    grid = GridspecLayout(len(options)+1, 3, width="470px")
    for i in range(len(options)):
        grid[i,0] = create_expanded_button(options[i], "primary")
    grid[(len(options)), 0] = create_expanded_button("Submit", "Danger"); 
    return grid

def check_answermc4(self):
    """
    Used with .on_click to make sure the answer is correct
        self: This is a button. We have added 2 new attributes to it
        current_answer: This is the last clicked button and its description value stored as a str
        answer: This is the correct answer from the mcdict

    """
    if self.current_answer == 0:
        return
    if self.answer[0] == self.current_answer[0]:
        self.button_style = "Success"
        self.description = "Correct!"
    else:
        self.button_style = "Danger"
        self.description = "Wrong, Try Again!"

def multiple_choice4(key, dictionary):
    """
    Creates a multiple choice widget that has 4 options.
    key: This is the key to the dictionary. It will be a str of digits.
    dictionary: the dictionary used is mc_dict. Which houses the multiple choice answers.
    grid: The grid that has been set up and can be shown
    header_button: sets the header_button that houses the question description
    """
    data = dictionary[key]
    question = data[2]
    options = data[0]
    answer_loc = len(options); 

    grid = create_grid(options)
    correct_answer = data[1]
    setattr(grid[answer_loc, 0], "answer", correct_answer)
    current_answer = 0
    setattr(grid[answer_loc, 0], "current_answer", 0)
    grid[answer_loc, 0].button_style = "Warning"

    def change_color(self):
        current_btn = int(self.layout.grid_area[-1])
        for i in range(len(options)):
            grid[i, 0].button_style = "primary"
        grid[current_btn - 1, 0].button_style = "info"
        grid[answer_loc, 0].current_answer = self.description

    for i in range(len(options)):
        grid[i, 0].on_click(change_color)
    grid[answer_loc, 0].on_click(check_answermc4)
    header_button = create_expanded_button(question, "info", "465px")
    return grid, header_button


def create_mc_grids():
    mc_grids = {}
    i = 1
    for key in mc_dict:
        mc_grids[key] = multiple_choice4(key, mc_dict)
        i += 1
    return mc_grids

def print_mc_grid(question_number):
    global mc_grids
    key = str(question_number)
    # Create the head tab
    widgets.VBox(
        [
            widgets.HTML(value="<span id='something'></span>"),
            AppLayout(header=mc_grids[key][1], footer=None),
            mc_grids[key][0],
        ]
    )
    display(widgets.VBox([mc_grids[key][1], mc_grids[key][0]]))



def main():
    #Test that the create multiple choice dictionary function works
    create_mc_dict(['1','2','3','4'], ["who", "what", "when", "where"], [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','16']], ['1','5','9','13'])
    print(mc_dict)
    print_mc_grid(1)
   

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function when the script is run directly
    main()
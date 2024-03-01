# Template Information 

Instructions and comments on how each of these templates work and what lessons they are assigned to. 

# frqTemplate Information
Excercises:
addition_subtracion Lesson,
assign_operators Lesson,
binary_hex Lesson,
Gates Lesson,
Luts and Mux Lesson,
Registers Lesson,
Sequential Logic Lesson,
Two's Compliment Lesson

Creates and displays the interactive FRQs, allowing for questions with either integer or string answers. The interaction is currently designed to have the user input their answers into the widgets for immediate feedback. 

Imports necessary libraries, such as ipywidgets

Main Functionalities
- Dictionary Initializiation: Defines a dictionary ('frquestions') that will hold the questions and answers. This dictionary is key to generating the question widgets, and typically just imports the questions from a seperate dictionary file
- Creating FRQ Widgets: The core functionality of the widgets revolves around two types of question widgets
    - Integer Answer FRQ: For questions that expect an integer answer, it creates a widget comprised of two buttons and a bounded integer text widget
    - String Answer FRQ: For questions that expect an integer answer, it creates a widget with two buttons again and a text widget
- Utility Functions: 
        'create_expanded_button' - Creates the button widgets, along with setting the layout and formatting it 
        'create_frq_int' and 'create'frq_string' - Generate the grid layout based on whether the answer type is an integer or string response
- Checking Answers: There is the function 'frq_check' that is used to check to see whether the correct answer was inputted against the provided dictionary stored within 'frquestions'. It is set to provide immediate feedback as to whether the answer is correct or not. 


# mcTemplate Information
Imports necessary libraries: importing pywidgets for creating interactive widgets in Jupyter notebooks


# ms_template information:

Import necessary libraries:

IPython.display: For displaying HTML and creating IFrames.
ipywidgets: Provides interactive widgets for the Jupyter Notebook.
Define a function create_expanded_button to create a customized button widget.

Define a function create_grid to create a grid layout for multiple-choice options.

Define a function check_answerms used with .on_click to check if the selected answers are correct.

Define a dictionary ms_dict that contains multiple-choice questions and their choices. Each entry in the dictionary is keyed by a question number (e.g., "1") and contains a list of choices, the correct answer, and the question itself.

Define a function multiple_select that creates a multiple-choice widget using the provided question number and dictionary. It extracts choices, correct answers, and the question itself from the dictionary.

Define a function change_color used with .on_click to toggle the color of selected answer buttons and update the set of current answers.

Iterate through the choices and set up click events for each button.

Set up a click event for the "Submit" button to check the answers using the check_answerms function.

Define a function create_ms_grids to create multiple-choice grids for all questions in ms_dict.

Create multiple-choice grids using the create_ms_grids function and store them in the ms_grids dictionary.

Define a function print_ms_grid to display a specific multiple-choice question using its question number.

# tt_template information:

Import Libraries: The script begins by importing the required libraries, including ipywidgets for creating interactive widgets in Jupyter notebooks.

Global Variables: The global dictionaries tt and tt_grids are initialized to hold truth table data and corresponding grid structures.

Initialize Truth Table Dictionary: The function create_tt_dictionary is defined to initialize the global dictionaries tt and tt_grids with input truth table data.

Create Button Function: The utility function create_expanded_button generates button objects with specified parameters for widget creation.

Create Grid Function: The create_grid function generates a truth table grid based on the number of inputs, dynamically adjusting its size and content. It populates the grid with default values and input fields.

Check Answer Function: The CheckAnswer function compares user inputs against correct answers, updating button styles and descriptions to indicate correctness.

Create Truth Table Grids: The create_tt_grids function generates a dictionary of truth table grids based on the initialized truth table data.

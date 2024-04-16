# Digital Design Colab Notebooks<br>

This repository contains [Google Colab](https://colab.research.google.com/) pages for learning about and developing digital circuits. There are 3 types of notebooks.

* [Tutorials](./Tutorials/README.md)
* [Learning Exercises](./Exercises/README.md)
* [Design Labs](./Labs/README.md)

Explanations about each type of Notebook can be found on the [wiki](https://github.com/byuccl/digital_design_colab/wiki).

## Getting Started <br>
If you're new to this repository and are looking for a place to start, [this notebook](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Tutorials/notebook_functionality/notebook_functionality.ipynb) explains what you need to know about Google Colabs in order to follow along with the rest of the notebooks. We recommend opening it in a new tab.

## Notebook List

The notebooks are organized into 5 notebook sets. 

<details open>
<summary>Dataflow System Verilog</summary>
<br>

|Category| Notebook| Link| Description
|---|---|---|---|
|Lesson|Boolean Algebra| [![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/boolean_algebra/boolean_algebra.ipynb)|Introduction to the boolean operators AND, OR, and NOT. Creating equations with these operators and performing analysis with truth tables.|
|Lesson|Logic Gates| [![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/gates/gates.ipynb)|Implementing boolean logic using logic gates. Introduction to XOR operator. Analyzing circuit diagrams composed of logic gates.|
|Lab|Logic Gates|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Labs/gates_lab/gates_lab.ipynb)|This lab teaches how to use Gate Level logic (and, or, not) and how the Waveforms work. It doesn't require a board.|
|Lesson|Karnaugh Maps| [![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/karnaugh_maps/karnaugh_maps.ipynb)|Introduction to Karnough maps. Using Karnough maps to analyze boolean expressions.|
|Lesson|LUTs And Mux| [![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/luts_and_mux/luts_and_mux.ipynb)|Introduction to Look Up Tables and Multiplexers. How these building blocks are used in circuit design.|
|Lesson|Assign Operators| [![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/assign_operators/assign_operators.ipynb)|Introduction to system verilog. How to code simple logic using assign statments.|
|Lesson|Always_comb Blocks| [![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/always_comb/always_comb.ipynb)|Introduction to always_comb blocks in system verilog. How to use always comb blocks to implement complex logic in system verilog.|
|Lab|Dataflow System Verilog|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Labs/dataflow_lab/dataflow_lab.ipynb)|The user implements Dataflow system verilog in 4 functions in a simple project.|

</details>

<details open>
<summary>Arithmetic</summary>
<br>

|Category| Notebook| Link| Description
|---|---|---|---|
|Lesson|Binary and Hexadecimal |[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/binary_hex/binary_hex.ipynb)|Indrocuction to hinary and hexadeximal number systems. Conversions between decimal, binary, and hexadecimal.|
|Lesson|Twos Complement |[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/twos_complement/twos_complement.ipynb)|Introduction to twos complement. Representing positive and negative integers with twos complement.|
|Lesson|Addition and Subtraction|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/addition_subtraction/addition_subtraction.ipynb)|Introduction to arithmetic operations on binary numbers. Adding and subtract on signed and unsigned binary numbers.|
|Lab|Arithmetic|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Labs/arithmetic_lab/arithmetic_lab.ipynb)|User implements an adder using multiple modules.|

</details>

<details open>
<summary>Seven Segment Display</summary>
<br>

|Category| Notebook| Link| Description
|---|---|---|---|
|Lesson|Seven Segment Display| [![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab2/blob/master/Exercises/seven_segment/seven_segment_lesson.ipynb)|Explanation of how a seven segment display works and how to decode a binary input to make each number.| 
|Lab|Seven Segment Display|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Labs/seven_segment_lab/seven_segment_lab.ipynb)| User implements a Binary to Seven Segment Hex Display converter |

</details>

<details open>
<summary>Stopwatch</summary>
<br>

|Category| Notebook| Link| Description
|---|---|---|---|
|Lesson|Flip Flops|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/flip_flops/flip_flops.ipynb)|Introduction to sequential logic. How flip flops are created from logic gates.|
|Lesson|Registers|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/registers/registers.ipynb)|How to create registers from flip flops. How to perfom analysis with timing diagrams|
|Lesson|Sequential Logic |[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/sequential_logic/sequential_logic.ipynb)|Introduction to always_ff blocks. How to create registers and implement sequential logic in SystemVeilog.|
|Lab|Stopwatch|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Labs/stopwatch_lab/stopwatch_lab.ipynb)| User implements a stopwatch using modules and hierarchical design. |


</details>


<details open>
<summary>State Machines</summary>
<br>

|Category| Notebook| Link| Description
|---|---|---|---|
|Lesson|State Machines|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Exercises/state_machines/state_machines.ipynb) | User learns what state machines are and common errors when constructing them|
|Lab|State Machines|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Labs/state_machine_lab/state_machine_lab.ipynb)|User learns how to design state machines and how to code them|

</details>

<br>

## Tutorials


There are also several tutorial notebooks that help users learn more about the open source tools being used, how to use our notebooks, and other helpful background information.

<details open>
<summary>Tutorials</summary>
<br>

|Category| Notebook| Link| Description
|---|---|---|---|
|Tutorial|Notebook Functionality|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Tutorials/notebook_functionality/notebook_functionality.ipynb)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|How to use Colab notebooks|
|Tutorial| XDC |[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Tutorials/xdc_tutorial/xdc_tutorial.ipynb)|Demonstrates how the XDC file works and how to use it for a personal project.|
|Tutorial|Verilator Overview|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Tutorials/verilator_overview/verilator_overview.ipynb)| Shows what Verilator is, what it does, and how to troubleshoot the test benches. |
|Tutorial|Verilog With VS Code|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Tutorials/verilog_with_vs_code/verilog_with_vs_code.ipynb)|Demonstrates a  better way to write verilog and how to set up VS Code|
|Tutorial|Bash File System|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Tutorials/bash_file_system/bash_file_system.ipynb)|How to view and navigate files in a notebook|
|Tutorial|Simulation Tools|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byuccl/digital_design_colab/blob/master/Tutorials/using_simulation_tools/using_simulation_tools.ipynb)| Teaches more about WaveDrom and VCD.|
|Tutorial|Creating a lesson|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/byuccl/digital_design_colab/blob/master/Tutorials/creating_lesson/your_lesson.ipynb)| Teaches more about how to create a lesson on your own.|
|Tutorial|Creating a lab|[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/byuccl/digital_design_colab/blob/master/Tutorials/labTemplateFolder/lab_template.ipynb)| Teaches more about how to create a lab on your own.|

</details>
import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText, IntSlider

#Free Response QUESTIONs
frquestions = [
["What is the value of 4'b1011&4'b1001?", 1001],
["What is the output of 4’b1001|4’b1011?", 1011],
["What is the output of 4’b1001^4b’1011?", 10],
["What is the output of 4’b1001&&4’b1011?", 1],
["What is the output of 4’b1001||4’b1011?", 1],
["What is the output of 4’b1001^^4’b1011?", 0],
["What is &4’b1011?", 0],
["What is |4’b1011?", 1],
["What is ^4’b1011?", 1],
["What is !4b’1011?", 0]
]
def create_expanded_button(description, button_style, width='auto'):
    return Button(description=description, button_style=button_style, layout=Layout(height='auto', width=width))

def create_frq(list, index):
  qlist = list[index]
  grid = GridspecLayout(1,3, width = '550px')
  grid[0,0] = create_expanded_button(qlist[0], "info", "300px")
  grid[0,1] =widgets.BoundedIntText(min=0,max=9999,layout=Layout(width='100px'))
  grid[0,2] =  create_expanded_button("Check", "info")
  return grid
#Question 1  
frq_1 = create_frq(frquestions, 0)
def frq_1_check(grid, qlist):
  if grid[0,1].value == qlist[0][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_1(self):
  frq_1_check(frq_1, frquestions)
#Question 2
frq_2 = create_frq(frquestions,1)
def frq_2_check(grid, qlist):
  if grid[0,1].value == qlist[1][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_2(self):
  frq_2_check(frq_2, frquestions)
#Question 3
frq_3 = create_frq(frquestions,2)
def frq_3_check(grid, qlist):
  if grid[0,1].value == qlist[2][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_3(self):
  frq_3_check(frq_3, frquestions)
#Question 4
frq_4 = create_frq(frquestions,3)
def frq_3_check(grid, qlist):
  if grid[0,1].value == qlist[3][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_4(self):
  frq_3_check(frq_4, frquestions)

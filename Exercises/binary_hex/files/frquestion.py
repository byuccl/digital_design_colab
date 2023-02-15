
import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText, IntSlider

#Free Response QUESTIONs
frquestions = [
["What integer does this sign-magnitude number represent? `10101`", -5],
["What integer does this sign-magnitude number represent? `01110`?", 14],
["What integer does this two's complement number represent? `10101`", -11],
["What integer does this two's complement number represent? `01110`", 14],
["What is the inverse of the two's complement number? `10101`", 11],
["What is the inverse of the twos complement value? `01110`", -14],
["What is `1001` + `0110` in Binary? (Its unsigned)", 1111],
["What is `0111` + `0011` in Binary? (Its unsigned)",  1010],
["What is `1010101`+0101101` in Binary? (Its unsigned)", 10000010],
["What is the value of `1111` + `0100`? (Put 9999 for overflow)", 9999],
["What is the value of `1010` + `0111`? (Put 9999 for overflow)", 9999],
["What is `1011` sign extended to 8 bits wide?", 11111011],
["What is `0001` sign extended to 8 bits wide?", 1],
["What is `1001` + `0110` in Binary? (2's complement)", 1111],
["What is `0111` + `0011` in Binary? (2's complement)", 1010],
["What is `1010101`+0101010` in Binary? (2's complement)", 1111111],
["What is `1100` - `1001` in Binary? (2's complement)", 11],
["What is `0111` - `0011` in Binary? (2's complement)", 100],
["What is the value of the output if A=1 and B = 0 and Cin = 1?", 0],
["What is the value of the carry out (Cout) if A=1 and B = 0 and Cin = 1?", 1]
]
def create_expanded_button(description, button_style, width='auto'):
    return Button(description=description, button_style=button_style, layout=Layout(height='auto', width=width))

def create_frq(list, index, q_width=500, max_=11111111):
  qlist = list[index]
  grid = GridspecLayout(1,3, width = (str(250 + q_width) +'px'))
  grid[0,0] = create_expanded_button(qlist[0], "info", str(q_width)+'px')
  grid[0,1] =widgets.BoundedIntText(min=(-1*max_),max=max_,layout=Layout(width='100px'))
  grid[0,2] =  create_expanded_button("Check", "info")
  return grid
#Question 1  
frq_1 = create_frq(frquestions, 0, 550)
def frq_1_check(grid, qlist):
  if grid[0,1].value == qlist[0][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_1(self):
  frq_1_check(frq_1, frquestions)
#Question 2
frq_2 = create_frq(frquestions, 1, 550)
def frq_2_check(grid, qlist):
  if grid[0,1].value == qlist[1][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_2(self):
  frq_2_check(frq_2, frquestions)
#Question 3
frq_3 = create_frq(frquestions, 2, 550)
def frq_3_check(grid, qlist):
  if grid[0,1].value == qlist[2][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_3(self):
  frq_3_check(frq_3, frquestions)
#Question 4
frq_4 = create_frq(frquestions, 3, 450)
def frq_4_check(grid, qlist):
  if grid[0,1].value == qlist[3][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_4(self):
  frq_4_check(frq_4, frquestions)
#Question 5
frq_5 = create_frq(frquestions, 4, 450)
def frq_5_check(grid, qlist):
  if grid[0,1].value == qlist[4][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_5(self):
  frq_5_check(frq_5, frquestions)
#Question 6
frq_6 = create_frq(frquestions, 5, 450)
def frq_6_check(grid, qlist):
  if grid[0,1].value == qlist[5][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_6(self):
  frq_6_check(frq_6, frquestions)
#Question 7
frq_7 = create_frq(frquestions, 6, 450)
def frq_7_check(grid, qlist):
  if grid[0,1].value == qlist[6][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_7(self):
  frq_7_check(frq_7, frquestions)
#Question 8
frq_8 = create_frq(frquestions, 7, 450)
def frq_8_check(grid, qlist):
  if grid[0,1].value == qlist[7][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_8(self):
  frq_8_check(frq_8, frquestions)
#Question 9
frq_9 = create_frq(frquestions, 8, 450, 11111111)
def frq_9_check(grid, qlist):
  if grid[0,1].value == qlist[8][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_9(self):
  frq_9_check(frq_9, frquestions)
#Question 10
frq_10 = create_frq(frquestions, 9, 450)
def frq_10_check(grid, qlist):
  if grid[0,1].value == qlist[9][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_10(self):
  frq_10_check(frq_10, frquestions)
#Question 11
frq_11 = create_frq(frquestions, 10, 450)
def frq_11_check(grid, qlist):
  if grid[0,1].value == qlist[10][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_11(self):
  frq_11_check(frq_11, frquestions)
#Question 12
frq_12 = create_frq(frquestions, 11, 450, 11111111)
def frq_12_check(grid, qlist):
  if grid[0,1].value == qlist[11][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_12(self):
  frq_12_check(frq_12, frquestions)
#Question 13
frq_13 = create_frq(frquestions, 12, 450)
def frq_13_check(grid, qlist):
  if grid[0,1].value == qlist[12][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_13(self):
  frq_13_check(frq_13, frquestions)
#Question 14
frq_14 = create_frq(frquestions, 13, 450)
def frq_14_check(grid, qlist):
  if grid[0,1].value == qlist[13][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_14(self):
  frq_14_check(frq_14, frquestions)
#Question 15
frq_15 = create_frq(frquestions, 14, 450)
def frq_15_check(grid, qlist):
  if grid[0,1].value == qlist[14][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_15(self):
  frq_15_check(frq_15, frquestions)
#Question 16
frq_16 = create_frq(frquestions, 15, 450, 11111111)
def frq_16_check(grid, qlist):
  if grid[0,1].value == qlist[15][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_16(self):
  frq_16_check(frq_16, frquestions)
#Question 17
frq_17 = create_frq(frquestions, 16, 450)
def frq_17_check(grid, qlist):
  if grid[0,1].value == qlist[16][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_17(self):
  frq_17_check(frq_17, frquestions)
#Question 18
frq_18 = create_frq(frquestions, 17, 450)
def frq_18_check(grid, qlist):
  if grid[0,1].value == qlist[17][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_18(self):
  frq_18_check(frq_18, frquestions)
#Question 19
frq_19 = create_frq(frquestions, 18, 450)
def frq_19_check(grid, qlist):
  if grid[0,1].value == qlist[18][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_19(self):
  frq_19_check(frq_19, frquestions)
#Question 20
frq_20 = create_frq(frquestions, 19, 450)
def frq_20_check(grid, qlist):
  if grid[0,1].value == qlist[19][1]:
    grid[0,2].button_style = "success"
  else:
    grid[0,2].button_style = "danger"
def check_frq_20(self):
  frq_20_check(frq_20, frquestions)

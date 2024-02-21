import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText

#Key
seven_segment_decode =[
 "1000000",#0
 "1111001",#1
 "0100100",#2
 "0110000",#3
 "0011001",#4
 "0010010",#5
 "0000010",#6
 "1111000",#7
 "0000000",#8
 "0010000",#9
 "0001000",#A
 "0000011",#B
 "1000110", #C
 "0100001",#D
 "0000110", #E
 "0001110"#F
]

def cbi(): #Create Bounded Int
  return widgets.BoundedIntText(min = 0, max = 1, layout=Layout(height="60px", width="75px"))
def create_expanded_button(description="", button_style='info', width='150px', height='50px'):
    return Button(description=description, button_style=button_style, layout=Layout(height=height, width=width))
#first row

def create_expanded_button_primary(description="", button_style='Primary', width='150px', height='50px'):
    return Button(description=description, button_style=button_style, layout=Layout(height=height, width=width))
#first row
first_row = GridspecLayout(1,3, width = '1200px')
first_row[0,0] = create_expanded_button_primary(description = "Hex")
first_row[0,1] = create_expanded_button_primary(description = "Input", width = '320px')
first_row[0,2] = create_expanded_button_primary(description = "Output", width = '710px')

#second row
#first row
second_row = GridspecLayout(1,3, width = '1200px')
second_row[0,0] = create_expanded_button(description = "Character")
second_row[0,1] = create_expanded_button(description = "Binary", width = '320px')
second_row[0,2] = create_expanded_button(description = "Segment [6:0]", width = '710px')
main_block = GridspecLayout(16,13, width = '1200px')

#Third Row

third_row = GridspecLayout(1, 13, width = '1200px')
descr_list = ["data[3]", "data[2]", "data[1]", "data[0]", "CG", "CF", "CE", "CD", "CC", "CB", "CA"]
third_row[0,0] = create_expanded_button(button_style = "info")
third_row[0,12] = create_expanded_button(button_style = "")

i = 1
for l in descr_list:
  third_row[0,i] = create_expanded_button(description = l, width = "75px")
  i += 1

def check_seven(self):
  answer_value = ''
  for i in range(5,12):
    answer_value += str(main_block[self.row, i].value)
  if(answer_value == seven_segment_decode[self.row]):
    print("Correct")
    self.button_style = "Success"
    self.description = "Correct"
  else:
    self.button_style = "Danger"
    self.description = "Incorrect, Try Again"
  print(answer_value + " " + seven_segment_decode[self.row])


#First Column
for i in range(16):
  main_block[i,0] = create_expanded_button(description=str(hex(i))[-1])
#Create a binary pattern
x = 8
for j in range(1,5):
  z = 0
  binary_v = '0'
  for i in range(16):
    z += 1
    main_block[i,j] = create_expanded_button(description = binary_v, button_style = "", width = '75px')
    if (z == x) and binary_v == '1':
      binary_v = '0'
      z = 0
    elif (z == x) and binary_v =='0':
      binary_v = '1'
      z= 0
  x = x/2
for j in range (5,12):
  for i in range (16):
    main_block[i,j] = cbi()
for i in range (16):
  main_block[i,12] = create_expanded_button(description = "Check", button_style = 'Warning')
  setattr(main_block[i,12], 'row', i)
  main_block[i,12].on_click(check_seven)
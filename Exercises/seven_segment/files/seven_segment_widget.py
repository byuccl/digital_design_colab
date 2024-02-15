import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText
#Seven Segment Display
def create_expanded_button(description="", button_style='', width='50px', height='50px'):
    return Button(description=description, button_style=button_style, layout=Layout(height=height, width=width))
def create_7_grid():
 grid = GridspecLayout(5,1, width='105px') #Middle Column
 grid[0,0] = create_expanded_button(button_style = "Danger", width = '100px')
 grid[1,0] = create_expanded_button(width = '100px', height = '65px')
 grid [2,0] = create_expanded_button(button_style = "Danger", width = '100px')
 grid [3,0] = create_expanded_button(width = '100px',  height= '65px')
 grid [4,0] = create_expanded_button(button_style = "Danger", width = '100px')
 return grid

def create_7b_grid(): #Side Columns
 grid = GridspecLayout(2, 1, width='54px')
 grid[0,0] = create_expanded_button(height="150px", width="50px", button_style="Danger")
 grid[1,0] = create_expanded_button(height="150px", width="50px", button_style="Danger")
 return grid

#Value Entry
def cbi(): #Create Bounded Int
  return widgets.BoundedIntText(min = 0, max = 1, layout=Layout(height="auto", width="50px"))

def create_value_grid():
  grid = GridspecLayout(2,8, width = '500px')
  for i in range (7):
    grid[1,i] = cbi()
  i = 0
  for letter in  reversed(['a','b','c','d','e','f','g']):
    grid[0,i] = Button(description=letter, button_style = 'info',layout=Layout(height="auto", width="50px"))
    i += 1
  grid[1,7] = Button(description = "Show", button_style = 'primary',layout=Layout(height="auto", width="100px"))
  return grid

def update_seven(self):
  if(value_list[1,6].value == 1):
    y[0,0].button_style = ''#a
  else:
    y[0,0].button_style = 'Danger'

  #b
  if(value_list[1,5].value == 1):
    z[0,0].button_style = ''
  else:
    z[0,0].button_style = 'Danger'
  #c
  if(value_list[1,4].value == 1):
    z[1,0].button_style = ''
  else:
    z[1,0].button_style = 'Danger'
  #d
  if(value_list[1,3].value == 1):
    y[4,0].button_style = ''
  else:
    y[4,0].button_style = 'Danger'
  #e
  if(value_list[1,2].value == 1):
    x[1,0].button_style = ''
  else:
    x[1,0].button_style = 'Danger'
  #f
  if(value_list[1,1].value == 1):
    x[0,0].button_style = ''
  else:
    x[0,0].button_style = 'Danger'
  #g
  if(value_list[1,0].value == 1):
    y[2,0].button_style = ''
  else:
    y[2,0].button_style = 'Danger'
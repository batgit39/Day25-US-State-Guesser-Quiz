import turtle
import pandas
import os

from pandas.core.indexers.utils import check_key_length
from pandas.io.parsers.readers import check_dtype_backend

writer = turtle.Turtle()
writer.penup()
screen = turtle.Screen()
screen.setup(width = 725, height = 490) 
screen.title("U.S. State Guesser")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")

checkinglist = []
counter = 0
game = True
while game:
    answer_state = screen.textinput(title = f"{counter}/50 States Correct", prompt = "What's another State's name?").title()
    if answer_state == "Exit":
            break
    else:
        for i in range(len(data)):
            x = int(data.x[i])
            y = int(data.y[i])
            
            if answer_state in checkinglist:
                pass     
            elif  answer_state == data.state[i]:
                counter += 1
                writer.goto(x, y)
                writer.write(data.state[i])
                checkinglist.append(answer_state)


new_list = []
for x in range(len(checkinglist)):
    for y in range(len(data)):
        if checkinglist[x] == data.state[y]:
            pass
        elif checkinglist[x] not in new_list:
            new_list.append(data.state[y])

os.system('rm States_to_Learn.csv')
missing_states = pandas.DataFrame(new_list)
missing_states.to_csv("States_to_Learn.csv")

turtle.mainloop()

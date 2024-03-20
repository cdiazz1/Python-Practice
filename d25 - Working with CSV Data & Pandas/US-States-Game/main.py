import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "./US-States-Game/blank_states_img.gif"  
screen.addshape(image)
turtle.shape(image)

#Read State CSV
state_data = pd.read_csv("./US-States-Game/50_states.csv")
all_states = state_data.state.to_list()
guessed_states = []


while len(guessed_states) < 50: 
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_data = pd.DataFrame(missing_states)
        missing_states_data.to_csv("./US-States-Game/states_to_learn.csv")
        break


    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        selected_state = state_data[state_data.state == answer_state]
        t.goto(int(selected_state.x), int(selected_state.y))
        t.write(answer_state)
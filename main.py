import turtle as t
import pandas as pd
import tkinter

FONT = ("Arial", 8, "bold")

screen = t.Screen()
screen.title(f"U.S. States Name by Luisga.")
screen.setup()

image = "blank_states_img.gif"

screen.addshape(image)

t.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# t.onscreenclick(get_mouse_click_coor)

data = pd.read_csv("50_states.csv")

data_states = data.state

number_states = len(data_states)

# print(answer_state)

def game():

    score = 0

    while score < number_states:

        def state_validation():
            answer_state = (screen.textinput(title=f"{score}/{number_states} states correct",
                                             prompt="What's another state's name?").
                            lower().title())

            state_validated = False

            while not state_validated:

                try:
                    index = pd.Index(data_states).get_loc(answer_state)
                except:
                    tkinter.messagebox.showwarning(message="Try again")
                    answer_state = (screen.textinput(title=f"{score}/{number_states} states correct",
                                                     prompt="What's another state's name?").lower().title())
                    print(answer_state)
                else:
                    state_validated = True
                    return state_validated, answer_state
                    # print(state)

        is_state_validated, answer_state = state_validation()

        if is_state_validated:
            state_info = data[data.state == answer_state]
            # print(state_info)
            x_coordinate = state_info.x.values[0]
            y_coordinate = state_info.y.values[0]

            new_turtle = t.Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            new_turtle.goto(x_coordinate, y_coordinate)
            state_value = state_info.state.values[0]
            new_turtle.write(state_value, move=False, align="center", font=FONT)

            score += 1

    # print(state_value)
    # print(x_coordinate)
    # print(y_coordinate)

game()

t.mainloop()



# screen.exitonclick()

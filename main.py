import turtle as t
import pandas as pd
import tkinter

FONT = ("Arial", 8, "bold")

screen = t.Screen()
screen.title(f"U.S. States Name by Luisga.")
screen.setup(height=491, width=725)

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
    states_guessed = []

    while score < number_states:

        def state_validation():
            answer_state = (screen.textinput(title=f"{score}/{number_states} states correct",
                                             prompt="What's another state's name?").title())

            state_validated = False

            while not state_validated:

                if answer_state == "Exit":
                    state_validated = True
                    return state_validated, answer_state

                try:
                    index = pd.Index(data_states).get_loc(answer_state)
                except:
                    tkinter.messagebox.showwarning(title="error", message="Try again")
                    answer_state = (screen.textinput(title=f"{score}/{number_states} states correct",
                                                     prompt="What's another state's name?").title())
                    print(answer_state)
                else:
                    state_validated = True
                    return state_validated, answer_state
                    # print(state)

        is_state_validated, answer_state = state_validation()

        if is_state_validated:

            if answer_state != "Exit":

                state_info = data[data.state == answer_state]
                # print(state_info)
                x_coordinate = state_info.x.values[0]
                y_coordinate = state_info.y.values[0]

                new_turtle = t.Turtle()
                new_turtle.penup()
                new_turtle.hideturtle()
                new_turtle.goto(x_coordinate, y_coordinate)
                state_value = state_info.state.values[0]
                states_guessed.append(state_value)
                new_turtle.write(state_value, move=False, align="center", font=FONT)

                score += 1

            else:

                list_states = data_states.to_list()
                missing_states = ["state"]

                for state in list_states:
                    if state in states_guessed:
                        pass
                    else:
                        missing_states.append(state)

                print(missing_states)
                print(len(missing_states)-1)

                states_to_learn = pd.DataFrame(missing_states)

                states_to_learn.to_csv("states_to_learn.csv")

                break






    # print(state_value)
    # print(x_coordinate)
    # print(y_coordinate)

game()

t.mainloop()
#
#
#
# # screen.exitonclick()


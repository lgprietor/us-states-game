import turtle as t

screen = t.Screen()
screen.title("U.S. States Name by Luisga")
screen.setup()

image = "blank_states_img.gif"

screen.addshape(image)

t.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

t.onscreenclick(get_mouse_click_coor)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")

print(answer_state)

t.mainloop()




















# screen.exitonclick()

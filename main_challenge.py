import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed_states = []
all_states = data["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct States",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # with open("states_to_learn.csv", mode="a") as file:
        #     for states in all_states:
        #         if states not in guessed_states:
        #             file.write(f"{states}\n")
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        index = (data[data.state == f"{answer_state}"]).index[0]
        data_x = data[data.state == f"{answer_state}"].to_dict()["x"][index]
        data_y = data[data.state == f"{answer_state}"].to_dict()["y"][index]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(data_x, data_y)
        t.write(f"{answer_state}")

screen.exitonclick()

# def get_mouse_click_coor(x, y):  # i# Logic for obtaining x, y coordinates.
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

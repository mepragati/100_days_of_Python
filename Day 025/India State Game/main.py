import turtle
import pandas

screen = turtle.Screen()
screen.title("India State Game")
image = "Day 025\India State Game\india-outline-map.gif"
screen.addshape(image)
turtle.shape(image)
turtle.screensize(800,950)

# #for getting the coordinates 
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

correct_guess_list = []
count = 0

while len(correct_guess_list) < 29: 
    answer_state = screen.textinput(title=f"{count}/29 Correct Guess", prompt="What's another state's name?").title()

    data = pandas.read_csv("Day 025\India State Game\Indian_States.csv")
    all_states = data.state.to_list()

    if answer_state == "Exit":
        # missing_state = []
        # for state in all_states:
        #     if state not in correct_guess_list:
        #         missing_state.append(state)

        missing_state = [state for state in all_states if state not in correct_guess_list]
        
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("Day 025\India State Game\states_to_learn.csv")
        break
    if answer_state in all_states:
        correct_guess_list.append(answer_state)
        loc = turtle.Turtle()
        loc.hideturtle()
        loc.penup()
        state_data = data[data.state == answer_state]
        loc.goto(int(state_data.x),int(state_data.y))
        loc.write(answer_state)
        # loc.write(state_data.state.item())
        count+=1
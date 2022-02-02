#!/usr/bin/env python3

# Aleksandr Verevkin
# U.S. States Guessing Game
import turtle
import pandas
IMAGE = "blank_states_img.gif"


def setup_writer():
    temp = turtle.Turtle()
    temp.hideturtle()
    temp.penup()
    return temp


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.addshape(IMAGE)
    screen.setup(width=800, height=800, startx=2000, starty=200)
    screen.title("U.S. States Game")
    turtle.shape(IMAGE)

    data = pandas.read_csv("50_states.csv")
    states = data.state.tolist()
    answered = []
    writer = setup_writer()

    # Game
    answer_state = screen.textinput(title="Guess the State", prompt="What's state name?").title()
    while len(answered) < 50:
        if answer_state == "Exit":
            # Exit is a end game word
            break
        if answer_state in states and answer_state not in answered:
            answered.append(answer_state)
            writer.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
            writer.write(arg=answer_state, align="center")
        answer_state = screen.textinput(f"{len(answered)}/{len(states)} States Correct", "What's another state name?").title()

    # Ending
    writer.home()
    if len(answered) < 50:
        # Saving all unanswered states into a csv file
        writer.write(arg="GAME OVER", align="center")
        left_states = {"state": [state for state in states if state not in answered]}
        pandas.DataFrame(left_states).to_csv("states_to_learn.csv")
    else:
        writer.write(arg="YOU GUESSED ALL STATES, CONGRATULATION!!!", align="center")

    screen.exitonclick()

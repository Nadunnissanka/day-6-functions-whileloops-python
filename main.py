def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() == False:
    if right_is_clear():
        turn_right()
        move()
        if right_is_clear():
            turn_left()
    elif front_is_clear():
        move()
    else:
        turn_left()
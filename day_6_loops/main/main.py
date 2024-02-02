def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if front_is_clear():
        move()
    else:
        if not wall_in_front():
            move()
        else:
            turn_left()
    if at_goal():
        done()
            
    if not wall_on_right():
        turn_right()
        move()
        turn_right()

while not at_goal():
    jump()
        
    
        


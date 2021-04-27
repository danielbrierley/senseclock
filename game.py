import time
from displayStuff import displayNumber


RED = [255,0,0]
GREEN = [0,255,0]
GRID = 1

def moveBall():
    global ball,ballVelocity,score,run
    ball = [ball[0]+ballVelocity[0], ball[1]+ballVelocity[1]]
    if not ball[0] in range(1,7*GRID):
        ballVelocity[0] = -ballVelocity[0]
    if ball[1] == 0*GRID:
        ballVelocity[1] = -ballVelocity[1]
    if ball[1] == 6*GRID and ball[0] in range(paddle*GRID,paddle+3*GRID):
        ballVelocity[1] = -ballVelocity[1]
        score += 1
        if score == 99:
            run = False
    if ball[1] == 7*GRID:
        run = False
        

def getInput(sense):
    global paddle
    for event in sense.stick.get_events():
        #print("The joystick was {} {}".format(event.action, event.direction))
        if event.action == 'pressed':
            if event.direction == 'left':
                paddle -= 1
                if paddle < 0:
                    paddle = 0
            if event.direction == 'right':
                paddle += 1
                if paddle > 5:
                    paddle = 5

def Game(sense):
    global run,paddle,ball,ballVelocity,score

    paddle = 2
    ball = [4*GRID,6*GRID]
    ballVelocity = [1,-1]
    score = 0

    #PREGAME
    wait = True
        
    pixels = [[0,0,0] for x in range(64)]

    pixels[7*8+paddle] = RED
    pixels[7*8+paddle+1] = RED
    pixels[7*8+paddle+2] = RED

    pixels[(ball[1]//GRID)*8+(ball[0]//GRID)] = GREEN
        
    sense.set_pixels(pixels)
    
    while wait:
        for event in sense.stick.get_events():
            wait = not event.action == 'released'
            if event.action == 'released':
                if event.direction == 'left':
                    paddle -= 1
                    if paddle < 0:
                        paddle = 0
                if event.direction == 'right':
                    paddle += 1
                    if paddle > 5:
                        paddle = 5
            
        try: #Pygame sense emu
            sense.mainloop()
        except AttributeError: #Real sense hat or emu
            pass
        time.sleep(0.01)

    ##GAME
    run = True
    while run:
        getInput(sense)
        moveBall()
        
        
        pixels = [[0,0,0] for x in range(64)]

        pixels[7*8+paddle] = RED
        pixels[7*8+paddle+1] = RED
        pixels[7*8+paddle+2] = RED

        pixels[(ball[1]//GRID)*8+(ball[0]//GRID)] = GREEN
        
        sense.set_pixels(pixels)
        
        try: #Pygame sense emu
            sense.mainloop()
        except AttributeError: #Real sense hat or emu
            pass

        time.sleep(0.1/GRID)
        #print(ball)

    ##POSTGAME
    wait = True

    pixels = [[0,0,0] for x in range(64)]
    pixels = displayNumber(pixels,score, [1,1], RED)
    
    sense.set_pixels(pixels)

    time.sleep(2)
    
    while wait:
        for event in sense.stick.get_events():
            wait = not (event.action == 'released' and event.direction == 'middle')
            
        try: #Pygame sense emu
            sense.mainloop()
        except AttributeError: #Real sense hat or emu
            pass

        time.sleep(0.01)

if __name__ == '__main__':
    from sense_emu_pygame import SenseHat
    sense = SenseHat()
    Game(sense)

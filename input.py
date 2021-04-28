letters = [chr(x) for x in range(ord('A'),ord('Z')+1)]+[str(x) for x in range(10)]



def textInput(sense,col=[255,255,255]):
    global string,selected,run
    selected = 0
    string = ''
    sense.show_letter(letters[selected],col)
    
    run = True
    back = False
    while run:
        for event in sense.stick.get_events():
            #print("The joystick was {} {}".format(event.action, event.direction))
            if event.action == 'pressed':
                if event.direction == 'up':
                    selected -= 1
                    if selected < 0:
                        selected = len(letters)-1
                    sense.show_letter(letters[selected],col)
                if event.direction == 'down':
                    selected += 1
                    if selected > len(letters)-1:
                        selected = 0
                    sense.show_letter(letters[selected],col)
                if event.direction == 'left':
                    if len(string) > 0:
                        selected = letters.index(string[len(string)-1])
                        string = string[:len(string)-1]
                    else:
                        run = False
                    sense.show_letter(letters[selected],col)
                    print(string)
                if event.direction == 'right':
                    string = string + letters[selected]
                    selected = 0
                    sense.show_letter(letters[selected],col)
                    print(string)
            if event.action == 'released':
                if event.direction == 'middle':
                    #string = string + letters[selected]
                    run = False
        
        try: #Pygame sense emu
            sense.mainloop()
        except AttributeError: #Real sense hat or emu
            pass
    return string
        
        
        
if __name__ == '__main__':
    from sense_emu_pygame import SenseHat
    sense = SenseHat()
    print(letters)
    out = textInput(sense)
    print(out)

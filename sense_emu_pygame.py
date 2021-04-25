import pygame, sys

class SenseHat:
    
    def __init__(self, size=8, px=50):
        self.size = size
        self.px = px
        self.stick = Stick()
        self.temp = -20
        self.iteration = 0
        pygame.init()
        self.screen = pygame.display.set_mode((self.size*self.px, self.size*self.px))

    def set_pixels(self, pixels):
        for y in range(self.size):
            for x in range(self.size):
                pygame.draw.rect(self.screen, pixels[(y*self.size)+x], (x*self.px, y*self.px, self.px, self.px))
        pygame.display.update()

    def get_temperature(self):
        return self.temp
        

    def mainloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                self.stick.addEvent(event)
        self.iteration += 1
        if self.iteration == 10:
            self.iteration = 0
            self.temp += 1
            if self.temp == 60:
                self.temp = -20

class Stick:
    def __init__(self):
        self.events = []
        
    def get_events(self):
        events = self.events
        self.events = []
        return events

    def addEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.events.append(Event('pressed','up'))
            if event.key == pygame.K_s:
                self.events.append(Event('pressed','down'))
            if event.key == pygame.K_a:
                self.events.append(Event('pressed','left'))
            if event.key == pygame.K_d:
                self.events.append(Event('pressed','right'))
            if event.key == pygame.K_RETURN:
                self.events.append(Event('pressed','middle'))
                
class Event:
    def __init__(self, action, direction):
        self.action = action
        self.direction = direction
                
if __name__ == '__main__':
    pixels = [[x*4, 0, 0] for x in range(64)]
    sense = SenseHat()
    sense.set_pixels(pixels)
    clock = pygame.time.Clock()
    while True:
        sense.mainloop()
        clock.tick(30)

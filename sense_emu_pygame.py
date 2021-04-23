import pygame

class SenseHat():
    
    def __init__(self, size=8, px=50):
        self.size = size
        self.px = px
        pygame.init()
        self.screen = pygame.display.set_mode((self.size*self.px, self.size*self.px))

    def set_pixels(self, pixels):
        for y in range(self.size):
            for x in range(self.size):
                pygame.draw.rect(self.screen, pixels[(y*self.size)+x], (x*self.px, y*self.px, self.px, self.px))
        pygame.display.update()

if __name__ == '__main__':
    pixels = [[x*4, 0, 0] for x in range(64)]
    sense = SenseHat()
    sense.set_pixels(pixels)

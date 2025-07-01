from settings import *


class Bullet:
    def __init__(self, screen, img, x, y = player_y):
        self.screen = screen
        self.img = img
        self.x = x 
        self.y = y 
        self.state = "ready"

    def shoot(self):
        self.state = "fire"
        self.draw()


    def draw(self):
        self.y -= bullet_speed
        self.screen.blit(self.img, (self.x+16, self.y))
    
    def load(self, x, y):
        self.state = "ready"
        self.y = y
        self.x = x
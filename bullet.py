from settings import *
from math import sqrt, pow


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

    def check_Collision(self, en_x, en_y, bull_x, bull_y):
        #euklidische distanz
        distance = sqrt(pow(en_x - bull_x, 2) + pow(en_y - bull_y, 2))
        if distance < 27:
            return True
        else: 
            return False


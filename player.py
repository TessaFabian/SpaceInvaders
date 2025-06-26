from settings import *

class Player:
    def __init__(self, screen, img, x = player_x, y = player_y):
        self.x = x
        self.y = y
        self.screen = screen
        self.img = img


    def move(self, direction):
        self.x += direction
        if self.x <= 0:
            self.x = 0
        if self.x >= screen_height - 64:
            self.x = screen_height - 64

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))
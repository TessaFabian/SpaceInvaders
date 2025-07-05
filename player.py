from settings import *

class Player:
    def __init__(self, screen, img, x = player_x, y = player_y):
        self.x = x
        self.y = y
        self.screen = screen
        self.img = img
        self.state = "ready"
        self.score = 0


    def move(self, direction):
        self.state = "move"
        self.x += direction
        if self.x <= 0:
            self.x = 0
        if self.x >= screen_width - 64:
            self.x = screen_width - 64

    def increase_sore(self):
        self.score += 10
        print(self.score)

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))
from settings import *


class Enemy:
    def __init__(self, screen, img):
        self.x = 0
        self.y = 0
        self.dx = 0.5
        self.dy = 1
        self.screen = screen
        self.img = img

    
    def move(self):
        self.x += self.dx

        # Richtungsumkehr
        if self.y >= screen_height - 90:
            self.dy = -1 
        if self.y <= 0:
            self.dy = 1
        
        if self.x <= 0:
            self.dx = 0.5
            self.y += self.dy * 50
        if self.x >= screen_width - 64:
            self.dx = -0.5
            self.y += self.dy*50

    def reset(self):
        self.x = 0
        self.y = 0

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))
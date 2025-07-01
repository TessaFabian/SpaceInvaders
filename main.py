import pygame as pg
from enemy import Enemy
from player import Player
from bullet import Bullet
from settings import *

pg.init()

#Screen einrichten
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Space Invaders")
pg.display.set_icon(pg.image.load("images/ufo.png")) # image.load liefert eine surface zurück


enemy = Enemy(screen, pg.image.load("images/enemy.png"))
player = Player(screen, pg.image.load("images/player.png"))
bullet = Bullet(screen, pg.image.load("images/bullet.png"), player.x)

#Game loop
running = True
while running:
    screen.fill((179, 238, 187))
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player_direction = -0.1
            if event.key == pg.K_RIGHT:
                player_direction = 0.1
            if event.key == pg.K_SPACE:
                bullet.shoot()
                print(bullet.state)
                 
        if event.type == pg.KEYUP:
                player.state = "ready"
                player_direction = 0
    
    player.move(player_direction)
    player.draw()

    #automatic enemy movement
    enemy.move()
    enemy.draw()

    if bullet.state == "fire":
        bullet.draw()
    if bullet.y <= 0:
        bullet.load(player.x + 16, player.y + 10)
    
    pg.display.flip()

pg.quit()
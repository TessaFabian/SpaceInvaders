import pygame as pg
from enemy import Enemy
from settings import *

pg.init()

#Screen einrichten
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Space Invaders")
pg.display.set_icon(pg.image.load("images/ufo.png")) # image.load liefert eine surface zurück

#bilder laden und im Fenster anzeigen
#spieler
def player(x, y):
    player_img = pg.image.load("images/player.png")
    screen.blit(player_img, (player_x, player_y)) #player an der Position 200,300 hinzufügen

#enemy
# def enemy(x = enemy_x, y = enemy_y): #standardwerte
#     enemy_img = pg.image.load("images/enemy.png")
#     screen.blit(enemy_img, (enemy_x, enemy_y))
enemy = Enemy(screen, pg.image.load("images/enemy.png"))

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
        if event.type == pg.KEYUP:
                player_direction = 0
    #player movement
    player_x += player_direction
    if player_x <= 0:
        player_x = 0
    if player_x >= screen_height - 64: 
        player_x = screen_height - 64

    #automatic enemy movement
    enemy.move()
    enemy.draw()

        

    player(player_x, player_y)
    pg.display.flip()

pg.quit()
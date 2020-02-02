# -*- coding: utf-8 -*-


import pygame
import random
pygame.init()

screenWidth = 600
screenHeight = 600


win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("First Game")
mainShip = pygame.image.load('bgbattleship_small.png')
enemyShip = pygame.image.load('enemyship2.png')
projBullet = pygame.image.load('bullet_1.png')


# class for player's ship
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        
    def draw(self, win):
        win.blit(mainShip, (self.x, self.y))
        
# class for bullets               
class projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10

    def draw(self, win):
        win.blit(projBullet, (self.x, self.y))

# class for enemy ships       
class enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.hitbox = (self.x, self.y, self.width, self.height)
        
    def draw(self, win):
        win.blit(enemyShip, (self.x, self.y))
        # draw hitbox
        self.hitbox = (self.x + 7, self.y, self.width - 13, self.height)
# visual of hitbox:
#        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)
        


# function to redraw window after each iteration of the main loop
def redrawWin():
    win.fill((0,0,0))
    for bullet in bullets:
        bullet.draw(win)
        
    spaceship.draw(win)
    for e in enemies:
        e.draw(win)
      
    text = font.render('Score: ' + str(score), True, (255, 0, 0))    
    win.blit(text, (screenWidth - 140, 0))
    
    pygame.display.update()
        
# main loop
spaceship = player(screenWidth/2 - 85/2, screenHeight - 85, 85, 85)
enemies = []
bullets = []
enemyCounter = 50
newEnemyTime = 50
run = True
score = 0
font = pygame.font.Font('freesansbold.ttf', 24)
bulletCooldown = 0

while run:
    pygame.time.delay(100)
    
    if enemyCounter == newEnemyTime:
        enemies.append(enemy(random.randint(0, screenWidth - 64), 0, 64, 64))
        enemyCounter = 0
    else:
        enemyCounter += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            
    for bullet in bullets:
        for e in enemies:
            if bullet.x > e.hitbox[0] and bullet.x < (e.hitbox[0] + e.hitbox[2]):
                if bullet.y > e.hitbox[1] and bullet.y < (e.hitbox[1] + e.hitbox[3]):
                    bullets.pop(bullets.index(bullet))
                    enemies.pop(enemies.index(e))
                    score += 5
                    
        if bullet.y > 0 and bullet.y < screenHeight:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE] and bulletCooldown == 0:
        bullets.append(projectile(int(spaceship.x + spaceship.width/2), int(spaceship.y + spaceship.height/2)))
        bulletCooldown += 1
    else:
        bulletCooldown += 1
    
    if keys[pygame.K_LEFT] and spaceship.x > spaceship.vel:
        spaceship.x -= spaceship.vel
        
    if keys[pygame.K_RIGHT] and spaceship.x < screenWidth - spaceship.width - spaceship.vel:
        spaceship.x += spaceship.vel
        
    
    redrawWin()
    
    for e in enemies:
        if e.y < screenHeight - e.height:
            e.y += e.vel
        else:
            print('GAME OVER. Your final score is:' + str(score))
            run = False
            
    if bulletCooldown == 2: 
        bulletCooldown = 0

    
        
pygame.quit()


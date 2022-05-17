import pygame
import random
import time

pygame.init()#initialize libraries
screen_width,screen_height = 800,450
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

#groups
coin_list = pygame.sprite.Group() #adds all coins to the group
all_sprites_list = pygame.sprite.Group() #adds everything to the group

#background load
mariobackground = pygame.image.load(('mariobackground.png')).convert()

#coin load
for i in range(50):
    coin = pygame.sprite.Sprite() #loads coin
    coin.image = pygame.image.load("coin.png")
    coin.rect = coin.image.get_rect()
    coin.rect.x = random.randrange(screen_width) # Set a random location for the coin
    coin.rect.y = random.randrange(screen_height)
    coin_list.add(coin) # Add the coin to the list of objects
    all_sprites_list.add(coin)

#mario load
mario = pygame.sprite.Sprite()
mario.image = pygame.image.load("mario.png")
mario.rect = mario.image.get_rect()
screen.blit(mario.image, mario.rect)
all_sprites_list.add(mario)


#variables
backgroundy = 0
score = 0

while (True):
    event=pygame.event.poll() #quitting the screen
    if(event.type==pygame.QUIT):
        break

    #background moving code
    rel_y = backgroundy % mariobackground.get_rect().height
    screen.blit(mariobackground, (0, rel_y - mariobackground.get_rect().height))
    if rel_y < screen_height:
        screen.blit(mariobackground, (0, rel_y))
    backgroundy -= 1

    #player moving code
    visibility = pygame.mouse.set_visible(False) #makes the cursor invisible
    pos = pygame.mouse.get_pos() #list (x,y)
    mario.rect.x = pos[0] #moves mario to cursor x and y postion
    mario.rect.y = pos[1]

    #moves coin down
    for coin in coin_list:
        coin.rect.y += 1
    if coin.rect.y > 450:
        coin.rect.y = random.randrange(-100, -20)
        coin.rect.x = random.randrange(0, screen_width)

    #coin colliding code
    coin_hit_list = pygame.sprite.spritecollide(mario, coin_list, True)
    for coin in coin_hit_list:
        score += 1
        print(score)
        coin.rect.y = random.randrange(-100, -20)
        coin.rect.x = random.randrange(0, screen_width)

    all_sprites_list.has

    #draws all sprites
    all_sprites_list.draw(screen)

    clock.tick(120)
    pygame.display.update()


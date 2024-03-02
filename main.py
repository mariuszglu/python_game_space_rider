import pygame
import time
import random
pygame.font.init()


WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Rider")

# BG = pygame.image.load("bg.png")
#when image is smaller than scrern you can usig transform, scale
BG = pygame.transform.scale(pygame.image.load("bg.png"),(WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
# velocity, speed player
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time):
#blit spacial method when you want to put it on the screen
    WIN.blit(BG,(0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s",1,"white")

#put time on window in position x,y 10,10
    WIN.blit(time_text,(10,10))
#drawing red rectangle (player) on WIN window
    pygame.draw.rect(WIN,"red",player)
#update usign every time when you want put changes on the screen
    pygame.display.update()



def main():
    run = True

# moving a charakter
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []

    while run:

        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0,WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
                #add every 50mils star
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + PLAYER_HEIGHT <= HEIGHT:
            player.y += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL

        draw(player, elapsed_time)

    pygame.quit()

if __name__ == "__main__":
    main()
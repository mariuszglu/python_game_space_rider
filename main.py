import pygame


WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Rider")

# BG = pygame.image.load("bg.png")
#when image is smaller than scrern you can usig transform, scale
BG = pygame.transform.scale(pygame.image.load("bg.png"),(WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
# velocity, speed player
PLAYER_VEL = 2

def draw(player):
#blit spacial method when you want to put it on the screen
    WIN.blit(BG,(0,0))
#drawing red rectangle (player) on WIN window
    pygame.draw.rect(WIN,"red",player)
#update usign every time when you want put changes on the screen
    pygame.display.update()



def main():
    run = True

# moving a charakter
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    while run:
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

        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()
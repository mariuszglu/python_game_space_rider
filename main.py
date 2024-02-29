import pygame


WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Rider")

# BG = pygame.image.load("bg.png")
#when image is smaller than scrern you can usig transform, scale
BG = pygame.transform.scale(pygame.image.load("bg.png"),(WIDTH, HEIGHT))

def draw():
#blit spacial method when you want to put it on the screen
    WIN.blit(BG,(0,0))
#update usign every time when you want put changes on the screen
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame

pygame.init()
screen,running = pygame.display.set_mode((800,600)),True
pygame.display.set_caption("hm")
ic = pygame.image.load("Imagenes/1.png")
pygame.display.set_icon(ic)
pygame.display.flip()

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE: running = False

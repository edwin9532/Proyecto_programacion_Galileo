# -*- coding: utf-8 -*-

import pygame

def main():
    pygame.init()
    pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    pygame.display.flip()
    
    running = True
    
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE: running = False
            
main()
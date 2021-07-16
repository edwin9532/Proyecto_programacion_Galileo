#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 12:00:11 2021

@author: lizeth
"""

import pygame
from pygame.locals import *
import sys

class Text:

    def __init__(self, text, pos, fontsize=90, fontname='BebasNeue.otf', color='white'):
        self.text = text
        self.len = len(self.text)+1
        self.pos = pos
        self.fontname = fontname
        self.fontsize = fontsize
        self.fontcolor = Color(color)
        self.set_font()
        self.move = True
            
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)
     
    def tfin(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.center = self.pos
        screen.blit(self.img, self.rect)
        pygame.display.update()
        
    def draw(self):
        while self.move:
            for n in range(0, self.len):
                if n == self.len-1:
                    self.move = False
                self.img = self.font.render(self.text[0:n], True, self.fontcolor)
                self.rect = self.img.get_rect()
                self.rect.center = self.pos
                R=Rect(self.rect.topleft, (self.rect.width, self.rect.height))
                pygame.draw.rect(screen, (0,0,0), R)
                screen.blit(self.img, self.rect)
                pygame.display.update()
                pygame.time.wait(200)
        self.tfin()
            



pygame.init()


clock = pygame.time.Clock()


display = pygame.Surface((0,0))
screen = pygame.display.set_mode((0,0), FULLSCREEN)
w, h = screen.get_width(), screen.get_height()

k = Text('Esto es un ejemplo', (w/2,h-500))


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                
    screen.fill(Color(0, 0, 0))
    k.draw()
           
    pygame.display.update()
    
    


pygame.quit()
            

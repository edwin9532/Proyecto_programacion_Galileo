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
        #self.render()
            
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)
        
    def draw(self):
        global n
        for n in range(0, self.len): 
            self.img = self.font.render(self.text[0:n], True, self.fontcolor)
            self.rect = self.img.get_rect()
            self.rect.center = self.pos
            R=Rect(self.rect.topleft, (self.rect.width, self.rect.height))
            pygame.draw.rect(screen, (0,0,0), R)
            screen.blit(self.img, self.rect)
            pygame.display.update()
            pygame.time.wait(200)
            #if n == self.len:
               # break                                       
        #self.img = self.font.render(self.text, True, self.fontcolor)
        #self.rect = self.img.get_rect()
        #self.rect.topleft = self.pos
        #a.screen.blit(self.img, self.rect)
        #pygame.display.update()
            #screen.fill(Color(0, 0, 0))
       
        
       #si pongo esto de arriba al terminar se cierra el programa



pygame.init()


clock = pygame.time.Clock()
#clock.tick(60)
#for n in (0,len(self.text)-1):

display = pygame.Surface((0,0))
screen = pygame.display.set_mode((0,0), FULLSCREEN)
w, h = screen.get_width(), screen.get_height()

a = Text('Narrador: “Corre el siglo XVI.', (w/2,h-500))
b = Text('Despertaste en los recuerdos del maestro Galileo Galilei,', (w/2,h-500))
c = Text('y estoy aquí para ayudarte a entender qué está pasando.', (w/2,h-500))
d = Text('Estás aquí gracias a tu curiosidad.', (w/2,h-500))
e = Text('Y bueno, porque estás dormido en tu comedor mientras hacias', (w/2,h-500))
f = Text('la tarea de física y pensaste en ¿por qué los cuerpos caen?”', (w/2,h-500))


#------------------EJEMPLO(1.0)--------------------
k = Text('Hola', (w/2,h-500))
l = Text('Esto', ( w/2,h-500))
m = Text('Es', (w/2,h-500))
n = Text('Un', (w/2,h-500))
o = Text('Ejemplo', (w/2,h-500))
p = Text(':)', (w/2,h-500))

#--------------------------------------------------

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                
    screen.fill(Color(0, 0, 0))
    #a.draw()
    k.draw() #Para ver el ejemplo activar esta y desactivar a.draw()
    
    #if n == a.len-1:
      #  screen.fill(Color(0,0,0))
      #  b.draw()
    #if n == b.len-1:
      # screen.fill(Color(0,0,0))
      #  c.draw()
    #if n == c.len-1:
      #  screen.fill(Color(0,0,0))
      #  d.draw()
    #if n == d.len-1:
      #  screen.fill(Color(0,0,0))
      #  e.draw()
    #if n == e.len-1:
      #  screen.fill(Color(0,0,0))
      #  f.draw()
        
    
    
    
    
    
    pygame.display.update()
    
    
    
#--------------------EJEMPLO(1.1)---------------------
    if n == k.len-1:
       screen.fill(Color(0, 0, 0))
       l.draw()
    if n == l.len-1:
       screen.fill(Color(0, 0, 0))
       m.draw()
    if n == m.len-1:
       screen.fill(Color(0, 0, 0))
       n.draw()
    if n == n.len-1:
       screen.fill(Color(0, 0, 0))
       o.draw()
    if n == o.len-1:
       screen.fill(Color(0, 0, 0))
       p.draw()        
        
        #break               # si pongo esto al terminar se cierra el programa
                             # No es necesario por ahora
                             # La gracia es hacer esto pero con todo el texto
                             # y cuando se llegue al ultimo dialogo trasladar a la simulación
                             # PD: Mi pc explota
#------------------------------------------------------
    
    


pygame.quit()
            

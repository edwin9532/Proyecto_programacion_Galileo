#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:51:52 2021

@author: lizeth
"""

import pygame
from pygame.locals import *
import sys


class Text:

    def __init__(self, text, pos, fontsize=90, fontname='BebasNeue.otf', color='white'):
        self.text = text
        self.pos = pos
        self.fontname = fontname
        self.fontsize = fontsize
        self.fontcolor = Color(color)
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos         

    def draw(self):
        a.screen.blit(self.img, self.rect)

#-----------------------------------------------------------------------------------#

class Dialogos():
    
    def __init__(self, Introd):
        
        self.Introd = Introd
        self.mw , self.mh = self.Introd.w/2 , self.Introd.h/2
        
        self.rundisplay = True
        
    def drawdp(self): #muestra el mensaje presione enter para continuar
        self.msj = Text('Presione enter para continuar', (self.mw+150 , self.mh-100), fontsize=50)
        self.msj.draw()

    def blit_screen(self):
        self.Introd.screen.blit(self.Introd.display, (0,0))
        pygame.display.update()
        self.Introd.reiniciark()

#-----------------------------------------------------------------------------------#

class Dial_1p(Dialogos):
    
    def __init__(self, Introd):   
        Dialogos.__init__(self, Introd)
        
        self.state = '1'
        
    def displaydial(self):
        
        #fondo = pygame.image.load("fondo.png")        #---> para poner el fondo 
        #fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        #frect = fondo.get_rect()
        
        self.rundisplay1 = True
        while self.rundisplay1:
            
            self.Introd.events()
            self.checkstate()
            
            if self.state == '1':
                
                self.Introd.screen.fill(Color(71, 75, 78))
                self.d1 = Text('Este es el primer diálogo', (100, 100))
                self.d1.draw()
                self.drawdp()
                self.blit_screen()
                
            elif self.state == '2':
                
                self.Introd.screen.fill(Color(71, 75, 78))
                self.d2 = Text('Este es el segundo diálogo', (100, 100))
                self.d2.draw()
                self.drawdp()
                self.blit_screen()
                
            elif self.state == '3':
                
                self.Introd.screen.fill(Color(71, 75, 78))
                self.d3 = Text('Este es el tercer diálogo', (100, 100))
                self.d3.draw()
                self.drawdp()
                self.blit_screen()
                
            elif self.state == 'Juego':
                self.Introd.playing = True
                self.rundisplay1 = False
    
            
    def checkstate(self):
        
        if self.Introd.esc:
            self.Introd.running = False
            #self.rundisplay = False
        
        elif self.Introd.enter:
            if self.state == '1':
                self.state = '2'
            elif self.state == '2':
                self.state = '3'
            elif self.state == '3':
                self.state = 'Juego'
                
        elif self.Introd.borrar:
            if self.state == 'Juego':
                self.state == '3'
            elif self.state == '3':
                self.state = '2'
            elif self.state == '2':
                self.state = '1'
            
        

#-----------------------------------------------------------------------------#


class Introd():

    def __init__(self):
        pygame.init()
        
        
        self.running = True
        self.playing = False
        
        self.enter, self.borrar, self.esc = False, False, False
        
        self.display = pygame.Surface((0,0))
        self.screen = pygame.display.set_mode((0,0), FULLSCREEN)
        self.w, self.h = self.screen.get_width(), self.screen.get_height()
        
              
        self.diag1p = Dial_1p(self)
        #self.options = OptionsMenu(self)
        self.curr_diag = self.diag1p #parte de diálogos actual
    
    
    def juego(self):
        
        while self.playing:
            
            self.screen.fill(Color(71, 75, 78))
            self.asd = Text('aqui va la simulación', (self.w/2, self.h/2))
            self.asd.draw()
            pygame.display.update()
            self.events()
            
            #self.events()
            #if self.enter or self.atras:
            #    self.playing = False
            
        
    
    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                self.playing = False
                self.curr_diag.displaydial = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.esc = True
                    self.running = False
                    self.playing = False 
                #if event.key == K_DOWN:
                    #self.fabajo = True
                #if event.key == K_UP:
                    #self.farriba = True
                if event.key == K_RETURN:
                    self.enter = True
                if event.key == K_BACKSPACE:
                    self.borrar = True
                    
    def reiniciark(self):
        self.enter, self.borrar, self.esc = False, False, False


#-----------------------------------------------------------------------------#  

a = Introd()

while a.running:
    a.curr_diag.displaydial()
    a.juego()
  


    
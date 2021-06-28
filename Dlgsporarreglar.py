#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 12:37:57 2021

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

class TextM:

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
        
    def tfin(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
        a.screen.blit(self.img, self.rect)
        pygame.display.update()
        
    def draw(self):
        global n
        for n in range(0, self.len): 
            self.img = self.font.render(self.text[0:n], True, self.fontcolor)
            self.rect = self.img.get_rect()
            self.rect.topleft = self.pos
            R=Rect(self.rect.topleft, (self.rect.width, self.rect.height))
            pygame.draw.rect(a.screen, (0, 75, 78), R)
            a.screen.blit(self.img, self.rect)
            pygame.display.update()
            pygame.time.wait(55)
            if n == self.len:
                break
        
        #screen.fill(Color(0, 0, 0))

#-----------------------------------------------------------------------------------#

class Dialogos():
    
    def __init__(self, Introd):
        
        self.Introd = Introd
        self.mw , self.mh = self.Introd.w/2 , self.Introd.h/2
        
        self.rundisplay = True
        
    def diabox(self):
        R = Rect((self.Introd.w*0.03 , self.Introd.h*0.06), (self.Introd.w*0.95, self.Introd.h*0.25))
        pygame.draw.rect(self.Introd.screen, (0, 75, 78), R)
        
    def drawdp(self): #muestra el mensaje presione enter para continuar
        self.msj = Text('Presione enter para continuar', (self.mw*1.50 , self.mh*0.7), fontsize=30)
        Re = Rect((self.msj.pos[0]-20, self.msj.pos[1]-10),(self.msj.rect.width+40, self.msj.rect.height+10))
        pygame.draw.rect(self.Introd.screen, (0, 0, 0), Re)
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
                self.diabox()
                self.drawdp()
                
                self.d1 = TextM('Corre el siglo XVI. Despertaste en los recuerdos del maestro Galileo Galilei,', (100, 100), fontsize= 50)
                self.d12 = TextM('y estoy aquí para ayudarte a entender qué está pasando.', (100, 150), fontsize= 50)
                
                self.d1.draw()
                self.d12.draw()
                
                self.d1.tfin()
                self.d12.tfin()
                
                
                self.blit_screen()
                
            elif self.state == '2':
                
                self.diabox()
                
                self.d2 = TextM('Estás aquí gracias a tu curiosidad, y, bueno, porque te quedaste dormido ', (100, 100) , fontsize= 50)
                self.d22 = TextM('en tu comedor mientras hacías la tarea de física y pensabas: ', (100, 150) , fontsize= 50)
                self.d23 = TextM('¿por qué los cuerpos caen?', (100, 200) , fontsize= 50)
                
                self.d2.draw()
                self.d22.draw()
                self.d23.draw()
                
                self.drawdp()
                self.blit_screen()
                
            elif self.state == '3':
                
                self.diabox()
                
                self.d3 = TextM('Este es el tercer diálogo', (100, 100), fontsize= 50)
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
        #print (self.w , self.h)
              
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
  



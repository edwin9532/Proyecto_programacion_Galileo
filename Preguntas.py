#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 08:57:37 2021

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
    

#-----------------------------------------------------------------------------#

class TextM:

    def __init__(self, text, pos, fontsize=90, fontname='BebasNeue.otf', color='black', cfondo=(61, 64, 70), time=55):
        self.text = text
        self.len = len(self.text)+1
        self.pos = pos
        self.cfondo = cfondo
        self.time = time
        self.fontname = fontname
        self.fontsize = fontsize
        self.fontcolor = Color(color)
        self.set_font()
        self.move = True
        #self.render()
            
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)
        
    def tfin(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
        R=Rect(self.rect.topleft, (self.rect.width, self.rect.height))
        pygame.draw.rect(a.screen, (229,190,1), R)
        a.screen.blit(self.img, self.rect)
        pygame.display.update()
        
    def draw(self):
        while self.move:
            for n in range(0, self.len+1): 
                if n == self.len:
                    self.move = False
                    return True
                self.img = self.font.render(self.text[0:n], True, self.fontcolor)
                self.rect = self.img.get_rect()
                self.rect.topleft = self.pos
                R=Rect(self.rect.topleft, (self.rect.width, self.rect.height))
                pygame.draw.rect(a.screen, self.cfondo, R)
                a.screen.blit(self.img, self.rect)
                pygame.display.update()
                pygame.time.wait(self.time)
                
        
#-----------------------------------------------------------------------------------#


class Preguntas():

    def __init__(self, Preg):
        
        self.Preg = Preg
        self.w , self.h = self.Preg.w , self.Preg.h
        self.mw, self.mh = self.Preg.w/2 , self.Preg.h/2
        self.x100 = self.w*0.069
        self.y100 = self.h*0.11
        self.f50 = round(self.w*0.05)
        
        
        self.rundisplay = True
        self.cursorrect= pygame.Rect(0, 0, 90, 90)
        self.offset= -260       
        
    def draw_cursor(self):
        self.cursorr = Text('*', pos=(self.cursorrect.x, self.cursorrect.y))
        self.cursorr.draw()
     
    def draw_answer(self):
        
        if self.Preg.var1 == 0:
            pass
        elif self.Preg.var1 == 1:
            self.resp_correcta()
        elif self.Preg.var1 == 2:
            self.resp_incorrecta()
        
        
    def resp_correcta(self):
        self.bien = Text('Correcto',(self.w*0.6, self.h*0.7), color='green')
        self.bien.draw()
        pygame.display.update()
        
    def resp_incorrecta(self):    
        self.mal = Text('Incorrecto',(self.w*0.6, self.h*0.7), color='red')
        self.mal.draw()
        pygame.display.update()
        
    def blit_screen(self):
        self.Preg.screen.blit(self.Preg.display, (0,0))
        pygame.display.update()
        self.Preg.reiniciark()
    
    
        
        
        
#-----------------------------------------------------------------------------#

class Preguntas1(Preguntas):
    
    def __init__(self, Preg):
        Preguntas.__init__(self, Preg)
        
        self.state = 'A'
        self.Preg.var1 = 0
        self.cursorrect.midtop = (self.x100 , self.h*0.5)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.Preg.w, self.Preg.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.Preg.events()
            self.checkstate()
            self.Preg.screen.blit(fondo, frect)
            
            self.t = Text('Pregunta Número 1', (self.x100, self.y100), self.f50)
            #self.tt = Text('Mente Brillante', pos=(self.mw, self.mh-140), fontsize=185, color='black')
            self.t1 = Text('Opción 1', (self.w*0.2, self.h*0.5))
            #self.tt1 = Text('Empezar Aventura', pos=(self.mw, self.mh+100), fontsize=93, color='black')
            self.t2 = Text('Opción 2', (self.w*0.2, self.h*0.6))
            #self.tt2 = Text('Opciones', pos=(self.mw, self.mh+200), fontsize=97, color='black')
            self.t3 = Text('Opción 3', (self.w*0.2, self.h*0.7))
            #self.tt3 = Text('Salir', pos=(self.mw, self.mh+300), fontsize=97, color='black')
            
            #self.tt.draw()
            self.t.draw()
            #self.tt1.draw()
            self.t1.draw()
            #self.tt2.draw()
            self.t2.draw()
            #self.tt3.draw()
            self.t3.draw()
            self.draw_cursor()
            self.draw_answer()
            
            self.blit_screen()
            
            
    def cursor(self):
        if self.Preg.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.x100 , self.h*0.6)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.x100 , self.h*0.7)
                self.state='C'
            elif self.state=='C':
                self.cursorrect.midtop = (self.x100 , self.h*0.5)
                self.state='A'
        elif self.Preg.farriba:
            if self.state=='C':
                self.cursorrect.midtop = (self.x100 , self.h*0.6)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.x100 , self.h*0.5)
                self.state='A'
            elif self.state=='A':
                self.cursorrect.midtop = (self.x100 , self.h*0.7)
                self.state='C'
            
            
    def checkstate(self):
        self.cursor()
        if self.Preg.enter:
            if self.state == 'A':
                self.Preg.var1 = 2
            elif self.state == 'B':
                self.Preg.var1 = 1  
            elif self.state == 'C':
                self.Preg.var1 = 2
                

        if self.Preg.esc:
            self.Preg.running = False
            self.rundisplay = False
#-----------------------------------------------------------------------------#   



            
#-----------------------------------------------------------------------------#   

class Preg():
    
    def __init__(self):
        pygame.init()
        
        #pygame.mixer.music.load("audio1.mp3")
        #pygame.mixer.music.play(3)
        
        self.running = True
        self.playing = False
        
        self.var1 = 0
        
        self.fabajo, self.farriba, self.enter, self.atras, self.esc = False, False, False, False, False
        
        self.display = pygame.Surface((0,0))
        self.screen = pygame.display.set_mode((0,0), FULLSCREEN)
        self.w , self.h = self.screen.get_width(), self.screen.get_height()
        
        #pygame.display.set_caption("hm")
        #ic = pygame.image.load("Imagenes/Icono.png")
        #pygame.display.set_icon(ic)
              
        self.preg1 = Preguntas1(self)
        #self.preg2 = Preguntas2(self)
        self.curr_preg = self.preg1 # Sección de preguntas actual
        
    def juego(self):
        while self.playing:
            
            self.screen.fill(Color(71, 75, 78))
            self.asd = Text('aquí va la simulación', (self.w/2, self.h/2))
            self.asd.draw()
            pygame.display.update()
            self.events()
            
    
    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                self.playing = False
                self.curr_preg.rundisplay = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.esc = True
                    self.running = False
                if event.key == K_DOWN:
                    self.fabajo = True
                if event.key == K_UP:
                    self.farriba = True
                if event.key == K_RETURN:
                    self.enter = True
                if event.key == K_BACKSPACE:
                    self.atras = True

    def reiniciark(self):
        self.fabajo, self.farriba, self.enter, self.atras, self.esc = False, False, False, False, False

#-----------------------------------------------------------------------------#  

a = Preg()

while a.running:
    a.curr_preg.displaypreg()
    a.juego()
    
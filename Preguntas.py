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
        
        #Coor. Enunciado
        self.Ex = self.w*0.069
        self.Ey = self.h*0.11
        self.El = round(self.w*0.055)
        self.El1 = round(self.w*0.042)
        
        #Coor. Respuestas
        self.rx = self.w*0.15
        self.ry1 =self.h*0.5
        self.ry2 =self.h*0.62
        self.ry3 =self.h*0.74
        self.rl =round(self.w*0.05)
        
        self.rundisplay = True
        self.cursorrect= pygame.Rect(0, 0, 90, 90)
        self.offset= -260       
    
    def diabox(self):
        R = Rect((self.Preg.w*0.03 , self.Preg.h*0.075), (self.Preg.w*0.95, self.Preg.h*0.25))
        pygame.draw.rect(self.Preg.screen, (61, 64, 70), R)
    
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
        self.bien = Text('Correcto',(self.w*0.75, self.h*0.85), color='green')
        self.bien.draw()
        pygame.display.update()
        
    def resp_incorrecta(self):    
        self.mal = Text('Incorrecto',(self.w*0.75, self.h*0.85), color='red')
        self.mal.draw()
        pygame.display.update()
        
    def blit_screen(self):
        self.Preg.screen.blit(self.Preg.display, (0,0))
        pygame.display.update()
        self.Preg.reiniciark()
    
    
        
        
        
#-----------------------------------------------------------------------------#

#- ¿Los cuerpos caen dependiendo de su masa ? ... NO
#- Si hay una corriente de aire ¿Cae primero una roca que una pluma? ... SI
#- Con tus conocimientos: ¿La tierra atrae a los objetos hacia el centro de la tierra y es por esto que caen? ... SI
#- Si dejamos caer 2 objetos cualquiera y sabiendo que no hay resistencia al aire, ¿Los cuerpos caen dependiendo de su tamaño? ... NO
#- ¿Cae primero una roca que un trozo de madera? ... NO
#- Lo planteado por Aristoteles, sobre "...Que los cuerpos caen porque quieren estar pegados a la tierra..." es falso. ... SI


class Preguntas1(Preguntas):
    
    def __init__(self, Preg):
        Preguntas.__init__(self, Preg)
        
        self.state = 'A'
        self.Preg.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.Preg.w, self.Preg.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.Preg.events()
            self.checkstate()
            self.Preg.screen.blit(fondo, frect)
            self.diabox()
            
            self.t = Text('¿Los cuerpos caen dependiendo de su masa ?', (self.Ex, self.Ey), self.El)
            self.t1 = Text('Sí', (self.rx, self.ry1))
            self.t2 = Text('No', (self.rx, self.ry2))
               
            self.t.draw()
            self.t1.draw()
            self.t2.draw()
            
            self.draw_cursor()
            self.draw_answer()
            
            self.blit_screen()       
            
    def cursor(self):
        if self.Preg.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.Preg.farriba:
            #if self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry2)
                #self.state='B'
            if self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            elif self.state=='A':
                self.cursorrect.midtop = (self.Ex  , self.ry2)
                self.state='B'
            
            
    def checkstate(self):
        self.cursor()
        if self.Preg.enter:
            if self.state == 'A':
                self.Preg.var1 = 2
            elif self.state == 'B':
                self.Preg.var1 = 1  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.Preg.esc:
            self.Preg.running = False
            self.rundisplay = False
#-----------------------------------------------------------------------------#   

class Preguntas2(Preguntas):
    
    def __init__(self, Preg):
        Preguntas.__init__(self, Preg)
        
        self.state = 'A'
        self.Preg.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.Preg.w, self.Preg.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.Preg.events()
            self.checkstate()
            self.Preg.screen.blit(fondo, frect)
            self.diabox()
            
            self.t = Text('Si hay una corriente de aire ¿Cae primero ', (self.Ex, self.Ey), self.El)
            self.t01 = Text('una roca que una pluma?', (self.Ex, self.Ey+self.El), self.El)
            self.t1 = Text('Sí', (self.rx, self.ry1))
            self.t2 = Text('No', (self.rx, self.ry2))
               
            self.t.draw()
            self.t01.draw()
            self.t1.draw()
            self.t2.draw()
            
            self.draw_cursor()
            self.draw_answer()
            
            self.blit_screen()       
            
    def cursor(self):
        if self.Preg.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.Preg.farriba:
            #if self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry2)
                #self.state='B'
            if self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            elif self.state=='A':
                self.cursorrect.midtop = (self.Ex  , self.ry2)
                self.state='B'
            
            
    def checkstate(self):
        self.cursor()
        if self.Preg.enter:
            if self.state == 'A':
                self.Preg.var1 = 1
            elif self.state == 'B':
                self.Preg.var1 = 2  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.Preg.esc:
            self.Preg.running = False
            self.rundisplay = False

class Preguntas3(Preguntas):
    
    def __init__(self, Preg):
        Preguntas.__init__(self, Preg)
        
        self.state = 'A'
        self.Preg.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.Preg.w, self.Preg.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.Preg.events()
            self.checkstate()
            self.Preg.screen.blit(fondo, frect)
            self.diabox()
            
            self.t = Text('¿La tierra atrae a los objetos hacia el centro', (self.Ex, self.Ey), self.El)
            self.t01 = Text('de la tierra y es por esto que caen?', (self.Ex, self.Ey+self.El), self.El)
            self.t1 = Text('Sí', (self.rx, self.ry1))
            self.t2 = Text('No', (self.rx, self.ry2))
               
            self.t.draw()
            self.t01.draw()
            self.t1.draw()
            self.t2.draw()
            
            self.draw_cursor()
            self.draw_answer()
            
            self.blit_screen()       
            
    def cursor(self):
        if self.Preg.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.Preg.farriba:
            #if self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry2)
                #self.state='B'
            if self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            elif self.state=='A':
                self.cursorrect.midtop = (self.Ex  , self.ry2)
                self.state='B'
            
            
    def checkstate(self):
        self.cursor()
        if self.Preg.enter:
            if self.state == 'A':
                self.Preg.var1 = 1
            elif self.state == 'B':
                self.Preg.var1 = 2  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.Preg.esc:
            self.Preg.running = False
            self.rundisplay = False

class Preguntas4(Preguntas):
    
    def __init__(self, Preg):
        Preguntas.__init__(self, Preg)
        
        self.state = 'A'
        self.Preg.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.Preg.w, self.Preg.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.Preg.events()
            self.checkstate()
            self.Preg.screen.blit(fondo, frect)
            self.diabox()
            
            self.t = Text('Si dejamos caer 2 objetos cualquiera y sabiendo que no hay', (self.Ex, self.Ey), self.El1)
            self.t01 = Text('resistencia al aire, ¿Los cuerpos caen dependiendo de su ', (self.Ex, self.Ey+self.El1), self.El1)
            self.t02 = Text('tamaño?', (self.Ex, self.Ey+2*self.El1), self.El1)
            self.t1 = Text('Sí', (self.rx, self.ry1))
            self.t2 = Text('No', (self.rx, self.ry2))
               
            self.t.draw()
            self.t01.draw()
            self.t02.draw()
            self.t1.draw()
            self.t2.draw()
            
            self.draw_cursor()
            self.draw_answer()
            
            self.blit_screen()       
            
    def cursor(self):
        if self.Preg.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.Preg.farriba:
            #if self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry2)
                #self.state='B'
            if self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            elif self.state=='A':
                self.cursorrect.midtop = (self.Ex  , self.ry2)
                self.state='B'
            
            
    def checkstate(self):
        self.cursor()
        if self.Preg.enter:
            if self.state == 'A':
                self.Preg.var1 = 2
            elif self.state == 'B':
                self.Preg.var1 = 1  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.Preg.esc:
            self.Preg.running = False
            self.rundisplay = False
 
class Preguntas5(Preguntas):
    
    def __init__(self, Preg):
        Preguntas.__init__(self, Preg)
        
        self.state = 'A'
        self.Preg.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.Preg.w, self.Preg.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.Preg.events()
            self.checkstate()
            self.Preg.screen.blit(fondo, frect)
            self.diabox()
            
            self.t = Text('¿Cae primero una roca que un trozo de madera?', (self.Ex, self.Ey), self.El)
            #self.t01 = Text('resistencia al aire, ¿Los cuerpos caen dependiendo de su ', (self.Ex, self.Ey+self.El1), self.El1)
            #self.t02 = Text('tamaño?', (self.Ex, self.Ey+2*self.El1), self.El1)
            self.t1 = Text('Sí', (self.rx, self.ry1))
            self.t2 = Text('No', (self.rx, self.ry2))
               
            self.t.draw()
            #self.t01.draw()
            #self.t02.draw()
            self.t1.draw()
            self.t2.draw()
            
            self.draw_cursor()
            self.draw_answer()
            
            self.blit_screen()       
            
    def cursor(self):
        if self.Preg.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.Preg.farriba:
            #if self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry2)
                #self.state='B'
            if self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            elif self.state=='A':
                self.cursorrect.midtop = (self.Ex  , self.ry2)
                self.state='B'
            
            
    def checkstate(self):
        self.cursor()
        if self.Preg.enter:
            if self.state == 'A':
                self.Preg.var1 = 2
            elif self.state == 'B':
                self.Preg.var1 = 1  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.Preg.esc:
            self.Preg.running = False
            self.rundisplay = False
            
class Preguntas6(Preguntas):
    
    def __init__(self, Preg):
        Preguntas.__init__(self, Preg)
        
        self.state = 'A'
        self.Preg.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.Preg.w, self.Preg.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.Preg.events()
            self.checkstate()
            self.Preg.screen.blit(fondo, frect)
            self.diabox()
            
            self.t = Text('Lo planteado por Aristoteles, sobre "...Que los cuerpos', (self.Ex, self.Ey), self.El1)
            self.t01 = Text('caen porque quieren estar pegados a la tierra..."', (self.Ex, self.Ey+self.El1), self.El1)
            self.t02 = Text('¿Es falso?', (self.Ex, self.Ey+2*self.El1), self.El1)
            self.t1 = Text('Sí', (self.rx, self.ry1))
            self.t2 = Text('No', (self.rx, self.ry2))
               
            self.t.draw()
            self.t01.draw()
            self.t02.draw()
            self.t1.draw()
            self.t2.draw()
            
            self.draw_cursor()
            self.draw_answer()
            
            self.blit_screen()       
            
    def cursor(self):
        if self.Preg.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.Preg.farriba:
            #if self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry2)
                #self.state='B'
            if self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            elif self.state=='A':
                self.cursorrect.midtop = (self.Ex  , self.ry2)
                self.state='B'
            
            
    def checkstate(self):
        self.cursor()
        if self.Preg.enter:
            if self.state == 'A':
                self.Preg.var1 = 1
            elif self.state == 'B':
                self.Preg.var1 = 2  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.Preg.esc:
            self.Preg.running = False
            self.rundisplay = False
 
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
        self.preg2 = Preguntas2(self)
        self.preg3 = Preguntas3(self)
        self.preg4 = Preguntas4(self)
        self.preg5 = Preguntas5(self)
        self.preg6 = Preguntas6(self)
        self.curr_preg = self.preg6 # Sección de preguntas actual
        
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
    
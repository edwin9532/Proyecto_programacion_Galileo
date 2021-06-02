#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:19:17 2021

@author: lizeth
"""

import pygame , PlanoInclinado
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
        self.rect.center = self.pos         

    def draw(self):
        a.window.blit(self.img, self.rect)
 

#-----------------------------------------------------------------------------#

class Menu():

    def __init__(self, App):
        
        self.App = App
        self.mw, self.mh = self.App.w/2, self.App.h/2
        
        self.rundisplay = True
        self.cursorrect= pygame.Rect(0, 0, 90, 90)
        self.offset= -260       
        
    def draw_cursor(self):
        self.cursorr = Text('*', pos=(self.cursorrect.x, self.cursorrect.y))
        self.cursorr.draw()
        
    def blit_screen(self):
        self.App.window.blit(self.App.display, (0,0))
        pygame.display.update()
        self.App.reiniciark()
        
#-----------------------------------------------------------------------------#

class MainMenu(Menu):
    
    def __init__(self, App):
        Menu.__init__(self, App)
        
        self.state = 'Empezar Aventura'
        self.cursorrect.midtop = (self.mw + self.offset, self.mh+110)
    
    def displaymenu(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        frect = fondo.get_rect()
        
        self.rundisplay = True
        while self.rundisplay:
            self.App.events()
            self.checkstate()
            self.App.window.blit(fondo, frect)
            
            self.t = Text('Mente Brillante', pos=(self.mw, self.mh-140), fontsize=180)
            self.tt = Text('Mente Brillante', pos=(self.mw, self.mh-140), fontsize=185, color='black')
            self.t1 = Text('Empezar Aventura', pos=(self.mw, self.mh+100))
            self.tt1 = Text('Empezar Aventura', pos=(self.mw, self.mh+100), fontsize=93, color='black')
            self.t2 = Text('Opciones', pos=(self.mw, self.mh+200))
            self.tt2 = Text('Opciones', pos=(self.mw, self.mh+200), fontsize=97, color='black')
            self.t3 = Text('Salir', pos=(self.mw, self.mh+300))
            self.tt3 = Text('Salir', pos=(self.mw, self.mh+300), fontsize=97, color='black')
            
            self.tt.draw()
            self.t.draw()
            self.tt1.draw()
            self.t1.draw()
            self.tt2.draw()
            self.t2.draw()
            self.tt3.draw()
            self.t3.draw()
            self.draw_cursor()
            
            self.blit_screen()
            
            
    def cursor(self):
        if self.App.fabajo:
            if self.state=='Empezar Aventura':
                self.cursorrect.midtop = (self.mw + self.offset, self.mh+210)
                self.state='Opciones'
            elif self.state=='Opciones':
                self.cursorrect.midtop = (self.mw + self.offset, self.mh+310)
                self.state='Salir'
            elif self.state=='Salir':
                self.cursorrect.midtop = (self.mw + self.offset, self.mh+110)
                self.state='Empezar Aventura'
        elif self.App.farriba:
            if self.state=='Salir':
                self.cursorrect.midtop = (self.mw + self.offset, self.mh+210)
                self.state='Opciones'
            elif self.state=='Opciones':
                self.cursorrect.midtop = (self.mw + self.offset, self.mh+110)
                self.state='Empezar Aventura'
            elif self.state=='Empezar Aventura':
                self.cursorrect.midtop = (self.mw + self.offset, self.mh+310)
                self.state='Salir'
            
            
    def checkstate(self):
        self.cursor()
        if self.App.enter:
            if self.state == 'Empezar Aventura':
                self.App.playing = True
            elif self.state == 'Opciones':
                self.App.curr_menu = self.App.options
            elif self.state == 'Salir':
                self.App.running = False
            self.rundisplay = False

#-----------------------------------------------------------------------------#   

class OptionsMenu(Menu):
    
    def __init__(self, App):
        Menu.__init__(self, App)
        
    def displaymenu(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        frect = fondo.get_rect()
        
        self.rundisplay = True
        while self.rundisplay:
            self.App.events()
            if self.App.enter or self.App.atras:
                self.App.curr_menu = self.App.mainmenu
                self.rundisplay = False
                
            self.App.window.blit(fondo, frect)
            self.t6 = Text('Opciones', pos=(self.mw, self.mh-220), fontsize=120)
            self.t6.draw()
            self.blit_screen()


            
#-----------------------------------------------------------------------------#   

class App():
    
    def __init__(self):
        pygame.init()
        
        pygame.mixer.music.load("audio1.mp3")
        pygame.mixer.music.play(3)
        
        self.running = True
        self.playing = False
        
        self.fabajo, self.farriba, self.enter, self.atras = False, False, False, False
        
        self.display = pygame.Surface((0,0))
        self.window = pygame.display.set_mode((0,0), FULLSCREEN)
        self.w, self.h = self.window.get_width(), self.window.get_height()
        
        pygame.display.set_caption("hm")
        ic = pygame.image.load("Imagenes/1.png")
        pygame.display.set_icon(ic)
              
        self.mainmenu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.curr_menu = self.mainmenu #Menú actual
        
    def juego(self):
        while self.playing:
            pygame.mixer.music.stop()
            
            #self.events()
            #if self.enter or self.atras:
            #    self.playing = False
            
            self.playing = PlanoInclinado.main()
            self.reiniciark()
            pygame.mixer.music.play(4)
            
    
    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                self.playing = False
                self.curr_menu.rundisplay = False
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.fabajo = True
                if event.key == K_UP:
                    self.farriba = True
                if event.key == K_RETURN:
                    self.enter = True
                if event.key == K_BACKSPACE:
                    self.atras = True

    def reiniciark(self):
        self.fabajo, self.farriba, self.enter, self.atras = False, False, False, False

#-----------------------------------------------------------------------------#  

a = App()

while a.running:
    a.curr_menu.displaymenu()
    a.juego()
    
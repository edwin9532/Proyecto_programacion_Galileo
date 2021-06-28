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
        
    def diabox(self):
        R = Rect((self.Introd.w*0.03 , self.Introd.h*0.06), (self.Introd.w*0.95, self.Introd.h*0.25))
        pygame.draw.rect(self.Introd.screen, (0, 75, 78), R)
        
    def diabox2(self): #hacer otro cuadro de texto ahora como globo de diálogo más abajo que
        # muestre lo que galileo está diciendo 
        R = Rect((self.Introd.w*0.4 , self.Introd.h*0.45), (self.Introd.w*0.55, self.Introd.h*0.25))
        pygame.draw.rect(self.Introd.screen, (125, 96, 114), R)
        
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
                
                self.d1 = Text('Corre el siglo XVI. Despertaste en los recuerdos del maestro Galileo Galilei,', (100, 100), fontsize= 50)
                self.d12 = Text('y estoy aquí para ayudarte a entender qué está pasando.', (100, 150), fontsize= 50)
                
                self.d1.draw()
                self.d12.draw()
                
                self.drawdp()
                self.blit_screen()
                
            elif self.state == '2':
                
                self.diabox()
                
                self.d2 = Text('Estás aquí gracias a tu curiosidad, y, bueno, porque te quedaste dormido ', (100, 100) , fontsize= 50)
                self.d22 = Text('en tu comedor mientras hacías la tarea de física y pensabas: ', (100, 150) , fontsize= 50)
                self.d23 = Text('¿por qué los cuerpos caen?', (100, 200) , fontsize= 50)
                
                self.d2.draw()
                self.d22.draw()
                self.d23.draw()
                
                self.drawdp()
                self.blit_screen()
                
            elif self.state == '3':
                
                self.diabox()
                
                self.d3 = Text('Tu deber es entender el razonamiento de Galileo sobre el movimiento de' , (100, 100), fontsize= 50)
                self.d32 = Text('los cuerpos, y tratar de convencer y, convencerte, de que lo que estás', (100, 150) , fontsize= 50)
                self.d33 = Text('haciendo es correcto.    ¿Estás preparado?', (100, 200) , fontsize= 50)
                
                
                self.d3.draw()
                self.d32.draw()
                self.d33.draw()
                
                self.drawdp()
                self.blit_screen()
                
            elif self.state == 'Juego':
                self.Introd.curr_diag = self.Introd.diag2p
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
       
#-----------------------------------------------------------------------------------#           
       
class Dial_2p(Dialogos):
    
    def __init__(self, Introd):   
        Dialogos.__init__(self, Introd)
        
        self.state = '1'
        
    def displaydial(self):
        
        #fondo = pygame.image.load("fondo.png")        -----> para poner el fondo 
        #fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        #frect = fondo.get_rect()
        
        
                
        self.rundisplay2 = True
        while self.rundisplay2:
            
            self.Introd.events()
            self.checkstate()
            
            if self.state == '1':
                
                self.Introd.screen.fill(Color(71, 75, 78))
                self.diabox()
                self.diabox2()
                
                self.d1 = Text('Mira, ahí está Galileo, ¿puedes leer su mente?', (100, 100), fontsize= 50)
                self.g1 = Text(' . . . ', (self.Introd.w*0.42, self.Introd.h*0.47), fontsize= 50)
                
                self.d1.draw()
                self.g1.draw()
                
                self.drawdp()
                self.blit_screen()
                
            elif self.state == '2':
                
                self.diabox()
                self.diabox2()
                
                self.d2 = Text('Mira, ahí está Galileo, ¿puedes leer su mente?', (100, 100), fontsize= 50)
                
                self.g2 = Text('¡¿Cómo es posible que tal barbarie la sigamos creyendo', (self.Introd.w*0.42, self.Introd.h*0.47), fontsize= 40)
                self.g21 = Text('después de ya más de dos mil años?!  Es absurdo pensar', (self.Introd.w*0.42, self.Introd.h*0.47+42), fontsize= 40)
                self.g22 = Text('que \'los cuerpos se detienen porque se cansan\' y que', (self.Introd.w*0.42, self.Introd.h*0.47+84), fontsize= 40)
                self.g23 = Text('\'caen porque quieren estar pegados a la tierra\',', (self.Introd.w*0.42, self.Introd.h*0.47+126), fontsize= 40)               
                
                self.d2.draw()
                self.g2.draw()
                self.g21.draw()
                self.g22.draw()
                self.g23.draw()
                     
                self.drawdp()
                self.blit_screen()
                
            elif self.state == '3':
                
                self.diabox()
                self.diabox2()
                
                self.d3 = Text('Tal vez olvidé mencionarlo, pero Galileo tiene un genio bastante  .  .  .     ', (100, 100), fontsize= 50)
                self.d31 = Text('particular.     ', (100, 150), fontsize= 50)
                
                
                self.g3 = Text('Tiene que haber una forma de explicar por qué se mueven', (self.Introd.w*0.42, self.Introd.h*0.47), fontsize= 40)
                self.g31 = Text('las cosas. Tal vez por medio de la matemática y la ', (self.Introd.w*0.42, self.Introd.h*0.47+42), fontsize= 40)
                self.g32 = Text('aritmética encuentre algo.', (self.Introd.w*0.42, self.Introd.h*0.47+84), fontsize= 40)
                #self.g23 = Text('--', (self.Introd.w*0.42, self.Introd.h*0.47+126), fontsize= 40)    
                
                         
                self.d3.draw()
                self.d31.draw()
                self.g3.draw()
                self.g31.draw()
                self.g32.draw()
                
                self.drawdp()
                self.blit_screen()
            
            elif self.state == '4':
                
                self.diabox()
                self.diabox2()
                
                self.d4 = Text('Presta atención, aquí es donde, según Einstein, Galileo prende la antorcha ', (100, 100), fontsize= 50)
                self.d41 = Text('de la física moderna.', (100, 150), fontsize= 50)
                
                
                self.g4 = Text('He visto que una bala de cañón aumenta su velocidad ', (self.Introd.w*0.42, self.Introd.h*0.47), fontsize= 40)
                self.g41 = Text('a medida que cae por una colina. Revisaré primero', (self.Introd.w*0.42, self.Introd.h*0.47+42), fontsize= 40)
                self.g42 = Text('si esa velocidad es generada por el peso.', (self.Introd.w*0.42, self.Introd.h*0.47+84), fontsize= 40)
                #self.g23 = Text('--', (self.Introd.w*0.42, self.Introd.h*0.47+126), fontsize= 40)    
                
                         
                self.d4.draw()
                self.d41.draw()
                self.g4.draw()
                self.g41.draw()
                self.g42.draw()
                
                self.drawdp()
                self.blit_screen()    
            
            
            elif self.state == 'Juego':
                self.Introd.playing = True
                self.rundisplay2 = False
    
            
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
                self.state = '4'
            elif self.state == '4':
                self.state = 'Juego'
                
        elif self.Introd.borrar:
            if self.state == 'Juego':
                self.state = '4'
            elif self.state == '4':
                self.state == '3'
            elif self.state == '3':
                self.state = '2'
            elif self.state == '2':
                self.state = '1'
            
            #Cuando estoy en 4 y oprimo backspace no retrocede
            # en cambio si estoy en 3 o en 2 sí retrocede 
            # ¿qué puede ser?
         
#------------------------------------------------------------------------------------#


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
        self.diag2p = Dial_2p(self)
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
            #self.playing = False
            
    
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
  


    
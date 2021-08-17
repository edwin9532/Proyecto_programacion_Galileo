#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:17:54 2021

@author: lizeth
"""

import pygame , PlanoInclinado
from pygame.locals import *
import sys

#Texto centrado
class TextC:

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
        a.screen.blit(self.img, self.rect)
 
#Texto esquina supizq
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
        
#Texto Movimiento
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
        
#-----------------------------------------------------------------------------#

class Menu():

    def __init__(self, App):
        
        self.App = App
        self.mw, self.mh = self.App.w/2, self.App.h/2
        
        self.rundisplay = True
        self.cursorrect= pygame.Rect(0, 0, 90, 90)
        self.offset= -260       
        
    def draw_cursor(self):
        self.cursorr = TextC('*', pos=(self.cursorrect.x, self.cursorrect.y))
        self.cursorr.draw()
        
    def blit_screen(self):
        self.App.screen.blit(self.App.display, (0,0))
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
            self.App.screen.blit(fondo, frect)
            
            self.t = TextC('Mente Brillante', pos=(self.mw, self.mh-140), fontsize=180)
            self.tt = TextC('Mente Brillante', pos=(self.mw, self.mh-140), fontsize=185, color='black')
            self.t1 = TextC('Empezar Aventura', pos=(self.mw, self.mh+100))
            self.tt1 = TextC('Empezar Aventura', pos=(self.mw, self.mh+100), fontsize=93, color='black')
            self.t2 = TextC('Opciones', pos=(self.mw, self.mh+200))
            self.tt2 = TextC('Opciones', pos=(self.mw, self.mh+200), fontsize=97, color='black')
            self.t3 = TextC('Salir', pos=(self.mw, self.mh+300))
            self.tt3 = TextC('Salir', pos=(self.mw, self.mh+300), fontsize=97, color='black')
            
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
                self.App.playing = False
                self.App.dialoguing = True
            elif self.state == 'Opciones':
                self.App.curr_menu = self.App.options
            elif self.state == 'Salir':
                self.App.running = False
            self.rundisplay = False 

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
            if self.App.enter or self.App.borrar:
                self.App.curr_menu = self.App.mainmenu
                self.rundisplay = False
                
            self.App.screen.blit(fondo, frect)
            self.t6 = TextC('Opciones', pos=(self.mw, self.mh-220), fontsize=120)
            self.t6.draw()
            self.blit_screen()

#-----------------------------------------------------------------------------------#

class Dialogos():
    
    def __init__(self, App):
        
        self.App = App
        self.mw , self.mh = self.App.w/2 , self.App.h/2
        
        self.rundisplay = True
        
    def diabox(self):
        R = Rect((self.App.w*0.03 , self.App.h*0.06), (self.App.w*0.95, self.App.h*0.25))
        pygame.draw.rect(self.App.screen, (61, 64, 70), R)
        
    def diaboxPI(self):
        R = Rect((self.App.w*0.03 , self.App.h*0.07), (self.App.w*0.72, self.App.h*0.25))
        pygame.draw.rect(self.App.screen, (61, 64, 70), R)  
        
    def diabox2(self): #hacer otro cuadro de texto ahora como globo de diálogo más abajo que
        # muestre lo que galileo está diciendo
        nube = pygame.image.load("Imagenes/Nube.png")
        nube = pygame.transform.scale(nube, (round(self.App.w*0.67), round(self.App.h*0.42)))
        nrect = nube.get_rect()
        nrect.topleft = (self.App.w*0.35 , self.App.h*0.38)
        self.App.screen.blit(nube, nrect)
         
    def diabox3(self): #nube galileo en Tut pI
        nube = pygame.image.load("Imagenes/Nube.png")
        nube = pygame.transform.scale(nube, (round(self.App.w*0.67), round(self.App.h*0.42)))
        nrect = nube.get_rect()
        nrect.topleft = (self.App.w*0.001 , self.App.h*0.02)
        self.App.screen.blit(nube, nrect)
         
        #R = Rect((self.Introd.w*0.4 , self.Introd.h*0.45), (self.Introd.w*0.55, self.Introd.h*0.25))
        #pygame.draw.rect(self.Introd.screen, (125, 96, 114), R)
        
    def drawdp(self): #muestra el mensaje presione enter para continuar
        self.msj = Text('Presione enter para continuar', (self.mw*1.50 , self.mh*0.65), fontsize=round(self.App.w*0.021))
        Re = Rect((self.msj.pos[0]-20, self.msj.pos[1]-10),(self.msj.rect.width+40, self.msj.rect.height+14))
        pygame.draw.rect(self.App.screen, (4, 0, 61), Re)
        self.msj.draw()
        
    def drawdpPI(self): #muestra el mensaje presione enter para continuar
        self.msj = Text('Presione enter para continuar', (self.App.w*0.74 , self.App.h*0.92), fontsize=round(self.App.w*0.021))
        Re = Rect((self.msj.pos[0]-20, self.msj.pos[1]-10),(self.msj.rect.width+40, self.msj.rect.height+14))
        pygame.draw.rect(self.App.screen, (0, 0, 0), Re)
        self.msj.draw()
        
    def blit_screen(self):
        self.App.screen.blit(self.App.display, (0,0))
        pygame.display.update()
        self.App.reiniciark()

#-----------------------------------------------------------------------------------#

class Dial_1p(Dialogos):
    
    def __init__(self, App):   
        Dialogos.__init__(self, App)
        
        self.state = '1'
        self.stop = False
        
    def displaydial(self):
        
        fondo = pygame.image.load("Imagenes/Escenario2.png")       
        fondo = pygame.transform.scale(fondo,(self.App.w, round(self.App.h)))
        frect = fondo.get_rect()
        self.App.screen.blit(fondo, frect)
        
        gal = pygame.image.load("Imagenes/Galileoc.png")
        gal = pygame.transform.scale(gal,(round(self.App.w*0.13), round(self.App.h*0.47)))
        grect = gal.get_rect()
        
        self.x100 = self.App.w*0.069
        self.y100 = self.App.h*0.11
        self.f50 = round(self.App.w*0.034)
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.App.events()
            self.checkstate()
            #print(self.state)
            
            grect.topleft = (self.App.w*0.1, self.App.h*0.5)
            self.App.screen.blit(gal, grect)
            
            if self.state == '1':
                
                #self.App.screen.fill(Color(71, 75, 78))
                
                self.diabox()
                self.drawdp()
                
                if self.stop == False:
                
                    self.d1 = TextM('Corre el siglo XVI. Despertaste en los recuerdos del maestro Galileo Galilei,', (self.x100, self.y100), fontsize= self.f50, color='white')
                    self.d12 = TextM('y estoy aquí para ayudarte a entender qué está pasando.', (self.x100, self.y100+self.f50), fontsize= self.f50, color='white')
                
                self.d1.draw()
                self.stop = self.d12.draw()
                
                self.App.reiniciark()
                
            elif self.state == '2':
                
                self.diabox()
                self.drawdp()
                
                if self.stop == False:
                
                    self.d2 = TextM('Estás aquí gracias a tu curiosidad, y, bueno, porque te quedaste dormido ', (self.x100, self.y100) , fontsize= self.f50, color='white')
                    self.d22 = TextM('en tu comedor mientras hacías la tarea de física y pensabas: ', (self.x100, self.y100+self.f50) , fontsize=self.f50, color='white')
                    self.d23 = TextM('¿por qué los cuerpos caen?', (self.x100, self.y100+2*self.f50) , fontsize= self.f50, color='white')
                
                self.d2.draw()
                self.d22.draw()
                self.stop = self.d23.draw()
                        
                self.App.reiniciark()
                
            elif self.state == '3':
                
                self.diabox()
                self.drawdp()
                
                if self.stop == False:
                
                    self.d3 = TextM('Tu deber es entender el razonamiento de Galileo sobre el movimiento de' , (self.x100, self.y100), fontsize= self.f50, color='white')
                    self.d32 = TextM('los cuerpos, y tratar de convencer y, convencerte, de que lo que estás', (self.x100, self.y100+self.f50) , fontsize= self.f50, color='white')
                    self.d33 = TextM('haciendo es correcto.    ¿Estás preparado?  ', (self.x100, self.y100+2*self.f50) , fontsize= self.f50, color='white')
                
                
                self.d3.draw()
                self.d32.draw()
                self.stop = self.d33.draw()
                
                self.App.reiniciark()
                
            elif self.state == 'Juego':
                self.App.reiniciark()
                self.App.curr_diag = self.App.diag2p
                self.rundisplay = False
    
            
    def checkstate(self):
        
        if self.App.esc:
            #self.App.running = False
            self.App.curr_menu = self.App.mainmenu
            self.rundisplay = False
            self.App.dialoguing = False
            self.App.reiniciark()
        
        
        elif self.App.enter:
            if self.state == '1':
                self.state = '2'
                self.stop = False
            elif self.state == '2':
                self.state = '3'
                self.stop = False
            elif self.state == '3':
                self.state = 'Juego'
                self.stop = False
                
        elif self.App.borrar:
            if self.state == 'Juego':
                self.state == '3'
                self.stop = False
            elif self.state == '3':
                self.state = '2'
                self.stop = False
            elif self.state == '2':
                self.state = '1'
                self.stop = False


class Dial_2p(Dialogos):
    
    def __init__(self, App):   
        Dialogos.__init__(self, App)
        
        self.state = '1'
        self.stop = False
        
    def displaydial(self):
        
        
        fondo = pygame.image.load("Imagenes/Escenario2.png")       
        fondo = pygame.transform.scale(fondo,(self.App.w, round(self.App.h)))
        frect = fondo.get_rect()
        self.App.screen.blit(fondo, frect)
        
        galg = pygame.image.load("Imagenes/GalileoGa.gif")
        #galg = pygame.transform.scale(galg, (round(self.Introd.w), round(self.Introd.h)))
        ggrect = galg.get_rect()
        
        ggrect.topleft = (self.App.w*0.1, self.App.h*0.5)
        #self.Introd.screen.blit(galg, ggrect)
        
        self.x100 = self.App.w*0.069
        self.y100 = self.App.h*0.11
        self.f50 = round(self.App.w*0.034)
        
        self.xdg = self.App.w*0.42
        self.ydg = self.App.h*0.47
        self.f40 = round(self.App.w*0.027)
              
    
        self.rundisplay = True
        while self.rundisplay:
            
            self.App.events()
            self.checkstate()
            
            if self.state == '1':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
                
                #ggrect.topleft = (self.Introd.w*0.1, self.Introd.h*0.5)
                #self.Introd.screen.blit(galg, ggrect)
                
                if self.stop == False :
                    
                    self.d1 = TextM('Mira, ahí está Galileo, ¿puedes leer su mente?         ', (self.x100, self.y100), fontsize= self.f50, color='white')
                    self.g1 = TextM('  .     .     .  ', (self.xdg, self.ydg), fontsize= self.f50, cfondo=(255, 255, 255))
                
                self.d1.draw()
                self.stop = self.g1.draw()
                
                self.App.reiniciark()
                
            elif self.state == '2':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
                
                self.d2 = Text('Mira, ahí está Galileo, ¿puedes leer su mente? ', (self.x100, self.y100), fontsize= self.f50)
                
                if self.stop == False :
                    
                    self.g2 = TextM('¡¿Cómo es posible que tal barbarie la sigamos creyendo ', (self.xdg, self.ydg), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g21 = TextM('después de ya más de dos mil años?!  Es absurdo pensar ', (self.xdg, self.ydg+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g22 = TextM('que \'los cuerpos se detienen porque se cansan\' y que ', (self.xdg, self.ydg+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g23 = TextM('\'caen porque quieren estar pegados a la tierra\', ', (self.xdg, self.ydg+3*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))               
                
                self.d2.draw()
                self.g2.draw()
                self.g21.draw()
                self.g22.draw()
                self.stop = self.g23.draw()
                     
                self.App.reiniciark()
                
            elif self.state == '3':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
                
                if self.stop == False :
                    
                    self.d3 = TextM('Tal vez olvidé mencionarlo, pero Galileo tiene un genio bastante  .  .  .     ', (self.x100, self.y100), fontsize= self.f50, color='white')
                    self.d31 = TextM('particular.  ', (self.x100, self.y100+self.f50), fontsize= self.f50, color='white')
                
                
                    self.g3 = TextM('Tiene que haber una forma de explicar por qué se ', (self.xdg, self.ydg), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g31 = TextM('mueven las cosas. Tal vez por medio de la ', (self.xdg, self.ydg+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g32 = TextM('matemática y la aritmética encuentre algo.  ', (self.xdg, self.ydg+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    #self.g33 = Text('--', (self.xdg, self.ydg+3*self.f40), fontsize= self.f40)    
                
                         
                self.d3.draw()
                self.d31.draw()
                self.g3.draw()
                self.g31.draw()
                self.stop = self.g32.draw()
              
                self.App.reiniciark()
            
            elif self.state == '4':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
                
                if self.stop == False:
                    self.d4 = TextM('Presta atención, aquí es donde, según Einstein, Galileo prende la antorcha ',  (self.x100, self.y100), fontsize= self.f50, color='white')
                    self.d41 = TextM('de la física moderna. ',  (self.x100, self.y100+self.f50), fontsize= self.f50, color='white')
                
                
                    self.g4 = TextM('He visto que una bala de cañón aumenta su velocidad ', (self.xdg, self.ydg), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g41 = TextM('a medida que cae por una colina. Revisaré primero ', (self.xdg, self.ydg+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g42 = TextM('si esa velocidad es generada por su peso.   ', (self.xdg, self.ydg+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    #self.g43 = Text('--', self.xdg, self.ydg+3*self.f40), fontsize= self.f40)    
                
                         
                self.d4.draw()
                self.d41.draw()
                self.g4.draw()
                self.g41.draw()
                self.stop = self.g42.draw()
                
                self.App.reiniciark()  
            
            
            elif self.state == 'Juego':
                self.App.reiniciark()
                self.App.curr_diag = self.App.diag3p
                self.rundisplay = False
    
            
    def checkstate(self):
        
        if self.App.esc:
            #self.App.running = False
            self.rundisplay = False
        
        elif self.App.enter:
            if self.state == '1':
                self.state = '2'
                self.stop = False
            elif self.state == '2':
                self.state = '3'
                self.stop = False
            elif self.state == '3':
                self.state = '4'
                self.stop = False
            elif self.state == '4':
                self.state = 'Juego'
                self.stop = False
                
        elif self.App.borrar:
            if self.state == 'Juego':
                self.state = '4'
                self.stop = False
            elif self.state == '4':
                self.state == '3'
                self.stop = False
            elif self.state == '3':
                self.state = '2'
                self.stop = False
            elif self.state == '2':
                self.state = '1'
                self.stop = False
            

class Dial_3p(Dialogos):
    
    def __init__(self, App):   
        Dialogos.__init__(self, App)
        
        self.state = '1'
        self.stop = False
        
    def displaydial(self):
        
        
        fondo = pygame.image.load("Imagenes/Escenario2.png")       
        fondo = pygame.transform.scale(fondo,(self.App.w, round(self.App.h)))
        frect = fondo.get_rect()
        self.App.screen.blit(fondo, frect)
        
        fondo1 = pygame.image.load("Imagenes/ftutcl1.jpeg")       # -----> para poner el fondo 
        fondo1 = pygame.transform.scale(fondo1,(self.App.w, self.App.h))
        f1rect = fondo1.get_rect()
        
    
        galg = pygame.image.load("Imagenes/GalileoGa.gif")
        #galg = pygame.transform.scale(galg, (round(self.Introd.w), round(self.Introd.h)))
        ggrect = galg.get_rect()
        
        ggrect.topleft = (self.App.w*0.1, self.App.h*0.5)
        #self.Introd.screen.blit(galg, ggrect)
        
        self.x100 = self.App.w*0.069
        self.y100 = self.App.h*0.11
        self.f50 = round(self.App.w*0.034)
        
        self.xdg = self.App.w*0.42
        self.ydg = self.App.h*0.47
        self.f40 = round(self.App.w*0.027)
              
    
        self.rundisplay = True
        while self.rundisplay:
            
            self.App.events()
            self.checkstate()
            
            if self.state == '1':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
                
                #ggrect.topleft = (self.Introd.w*0.1, self.Introd.h*0.5)
                #self.Introd.screen.blit(galg, ggrect)
                
                
                if self.stop == False :
                    
                    self.d1 = TextM('Comenzaremos por mostrarte el primer experimento de Galileo:    ', (self.x100, self.y100), fontsize= self.f50, color='white')
                    self.d12 = TextM('La caída libre.    ', (self.x100, self.y100+self.f50), fontsize= self.f50, color='white')
                    
                    self.g1 = TextM('Teóricamente, si dejo caer una roca muy pesada y un ', (self.xdg, self.ydg), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g11 = TextM('acumulado de heno al mismo tiempo, deberá caer más ', (self.xdg, self.ydg+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g12 = TextM('rápido la roca, de igual forma que una balanza se  ', (self.xdg, self.ydg+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g13 = TextM('inclinaría hacia su lado por la diferencia de peso. ', (self.xdg, self.ydg+3*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))  
                
                self.d1.draw()
                self.d12.draw()
                
                self.g1.draw()
                self.g11.draw()
                self.g12.draw()
                self.stop = self.g13.draw()
                
                self.App.reiniciark()
                
            elif self.state == '2':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
            
                #Subiré a la torre de Pisa y lanzare una roca y un poco de heno.
                if self.stop == False :
                    
                    self.d2 = TextM('La intuición nos hizo pensar eso, veamos que hará Galileo.', (self.x100, self.y100), fontsize= self.f50, color='white')
                    
                    self.g2 = TextM('Voy a probarlo, para eso subiré a la torre de Pisa  ', (self.xdg, self.ydg), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g21 = TextM('y dejaré caer a la vez diferentes objetos. ', (self.xdg, self.ydg+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    #self.g22 = TextM('---', (self.xdg, self.ydg+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    #self.g23 = TextM('---', (self.xdg, self.ydg+3*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))               
                
                self.d2.draw()
                self.g2.draw()
                #self.g21.draw()
                #self.g22.draw()
                self.stop = self.g21.draw()
                     
                self.App.reiniciark()
                
            elif self.state == '3':
                
                self.App.screen.blit(fondo1, f1rect)
                self.diaboxPI()
                self.drawdpPI()
                
                
                if self.stop == False :
                    
                    self.d31 = TextM(' -               -               -                       -         ', (self.x100, self.y100), fontsize= self.f40, color='white')
                    self.d32 = TextM(' -               -               -                       -         ', (self.x100, self.y100+self.f40), fontsize= self.f40, color='white')      
                    self.d33 = TextM(' -               -               -                       -         ', (self.x100, self.y100+2*self.f40), fontsize= self.f40, color='white')
                    self.d34 = TextM(' -               -               -                       -         ', (self.x100, self.y100+3*self.f40), fontsize= self.f40, color='white')
                
                self.d31.draw()
                self.d32.draw()
                self.d33.draw()
                self.stop = self.d34.draw()
                     
                self.App.reiniciark()    
                
            elif self.state == '4':
                
                self.App.screen.blit(fondo1, f1rect)
                self.diaboxPI()
                self.drawdpPI()
                
                
                if self.stop == False :
                    
                    self.d41 = TextM(' -               -               -                       -         ', (self.x100, self.y100), fontsize= self.f40, color='white')
                    self.d42 = TextM(' -               -               -                       -         ', (self.x100, self.y100+self.f40), fontsize= self.f40, color='white')      
                    self.d43 = TextM(' -               -               -                       -         ', (self.x100, self.y100+2*self.f40), fontsize= self.f40, color='white')
                    self.d44 = TextM(' -               -               -                       -         ', (self.x100, self.y100+3*self.f40), fontsize= self.f40, color='white')
                
                self.d41.draw()
                self.d42.draw()
                self.d43.draw()
                self.stop = self.d44.draw()
                     
                self.App.reiniciark()    
            
            elif self.state == 'Juego':
                self.App.reiniciark()
                self.App.curr_diag = self.App.diag4p
                self.rundisplay = False
    
            
    def checkstate(self):
        
        if self.App.esc:
            #self.App.running = False
            self.rundisplay = False
        
        elif self.App.enter:
            if self.state == '1':
                self.state = '2'
                self.stop = False
            elif self.state == '2':
                self.state = '3'
                self.stop = False
            elif self.state == '3':
                self.state = '4'
                self.stop = False
            elif self.state == '4':
                self.state = 'Juego'
                self.stop = False
                
        elif self.App.borrar:
            if self.state == 'Juego':
                self.state = '4'
                self.stop = False
            elif self.state == '4':
                self.state == '3'
                self.stop = False
            elif self.state == '3':
                self.state = '2'
                self.stop = False
            elif self.state == '2':
                self.state = '1'
                self.stop = False
     
                
class Dial_4p(Dialogos):
    
    def __init__(self, App):   
        Dialogos.__init__(self, App)
        
        self.state = '1'
        self.stop = False
        
    def displaydial(self):
        
        fondo1 = pygame.image.load("Imagenes/ftutpi.png")       # -----> para poner el fondo 
        fondo1 = pygame.transform.scale(fondo1,(self.App.w, self.App.h))
        f1rect = fondo1.get_rect()
        
        fondo2 =  pygame.image.load("Imagenes/ftutpi2.png")
        fondo2 = pygame.transform.scale(fondo2,(self.App.w, self.App.h))
        f2rect = fondo2.get_rect()
        
        fondo3 =  pygame.image.load("Imagenes/ftutpi3.png")
        fondo3 = pygame.transform.scale(fondo3,(self.App.w, self.App.h))
        f3rect = fondo3.get_rect()
        
        fondo4 =  pygame.image.load("Imagenes/ftutpi4.png")
        fondo4 = pygame.transform.scale(fondo4,(self.App.w, self.App.h))
        f4rect = fondo4.get_rect()
    
        
        fondo = pygame.image.load("Imagenes/Escenario2.png")       
        fondo = pygame.transform.scale(fondo,(self.App.w, round(self.App.h)))
        frect = fondo.get_rect()
        self.App.screen.blit(fondo, frect)
        
        self.x100 = self.App.w*0.069
        self.y100 = self.App.h*0.11
        self.f50 = round(self.App.w*0.034)
        
        self.xda = self.App.w*0.55
        self.yda = self.App.h*0.88
        
        self.xdg = self.App.w*0.42
        self.ydg = self.App.h*0.47
        self.f40 = round(self.App.w*0.027)
        self.f60 = round(self.App.w*0.04)
              
        
          
        self.rundisplay = True
        while self.rundisplay:
            
            self.App.events()
            self.checkstate()
            
            if self.state == '1':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
                    
                if self.stop == False :
                    
                    self.d1 = TextM('Ahora Galileo realizará su segundo experimento:    ', (self.x100, self.y100), fontsize= self.f50, color='white')
                    
                    self.g1 = TextM('He notado que cuando un objeto cae por una colina  ', (self.xdg, self.ydg), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g11 = TextM('su velocidad va aumentando. Por lo que puedo deducir ', (self.xdg, self.ydg+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g12 = TextM('que las cosas no caen a velocidad constante. ', (self.xdg, self.ydg+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    #self.g13 = TextM(' ...', (self.xdg, self.ydg+3*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                  
                self.d1.draw()
                self.g1.draw()
                self.g11.draw()
                #self.g12.draw()
                self.stop = self.g12.draw()
                
                self.App.reiniciark()
            
            elif self.state == '1.5':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
                self.d1 = Text('Ahora Galileo realizará su segundo experimento    ', (self.x100, self.y100), fontsize= self.f50, color='white')   
                self.d1.draw()
                
                if self.stop == False :
                    
                    #self.d1 = TextM('- - -    ', (self.x100, self.y100), fontsize= self.f50, color='white')
                    
                    self.g1 = TextM('¿Cómo puedo estudiar este movimiento?     ', (self.xdg, self.ydg), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g11 = TextM('  .    .    .             ', (self.xdg, self.ydg+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g12 = TextM('  ¡Tengo una idea!   ', (self.xdg, self.ydg+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    
                 
                self.g1.draw()
                self.g11.draw()
                self.stop = self.g12.draw()
                
                self.App.reiniciark()
                
            elif self.state == '2':
                       
                self.App.screen.fill(Color(253, 194, 0))     
                
                if self.stop == False :
                    
                    self.d2 = TextM('  .     .     .  ', (self.App.w*0.35, self.App.h*0.4), fontsize= round(self.App.w*0.1), cfondo=(253, 194, 0), time=70)
                    self.pe = TextM('Presione enter para continuar', (self.xda, self.yda), fontsize= self.f60, cfondo=(253, 194, 0)) #fontsi 60
                 
                self.d2.draw()
                self.stop = self.pe.draw()
                
                self.App.reiniciark()
                
            elif self.state == '3':
                            
                self.App.screen.blit(fondo1, f1rect)
                self.diabox3()
                self.drawdpPI()
            
                
                if self.stop == False :
                    
                    self.g3 = TextM('¡He diseñado un plano inclinado! Éste me servirá  ', (self.x100, self.y100), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g31 = TextM('para realizar mis experimentos ya que puedo ', (self.x100, self.y100+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g32 = TextM('cambiarle varias características. ', (self.x100, self.y100+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    #self.g23 = TextM('\'caen porque quieren estar pegados a la tierra\', ', (self.x100, self.y100+3*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))               
                
                self.g3.draw()
                self.g31.draw()
                self.stop = self.g32.draw()
                     
                self.App.reiniciark()
                
            elif self.state == '4':
                
                self.App.screen.blit(fondo2, f2rect)
                self.diabox3()
                self.drawdpPI()
                
                
                if self.stop == False :
                    
                    self.g4 = TextM('  Por ejemplo puedo modificar su altura y ', (self.x100, self.y100), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g41 = TextM(' longitud, (y de esta forma variar el ángulo ', (self.x100, self.y100+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g42 = TextM(' de inclinación)', (self.x100, self.y100+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                               
                
                self.g4.draw()
                self.g41.draw()
                self.stop = self.g42.draw()
                     
                self.App.reiniciark()
            
            elif self.state == '5':
                
                self.App.screen.blit(fondo3, f3rect)
                self.diabox3()
                self.drawdpPI()
                
                
                
                if self.stop == False :
                    
                    self.g5 = TextM('  Y también puedo usar diferentes materiales para  ', (self.x100, self.y100), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g51 = TextM(' las esferas que van a caer. Cada material tiene  ', (self.x100, self.y100+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g52 = TextM(' un rango de masa distinto. ', (self.x100, self.y100+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g53 = TextM('    ¡Empecemos!   ', (self.x100, self.y100+3*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))           
                
                self.g5.draw()
                self.g51.draw()
                self.g52.draw()
                self.stop = self.g53.draw()
                     
                self.App.reiniciark()
                
            elif self.state == '6':
                
                self.App.screen.blit(fondo4, f4rect)
                self.diaboxPI()
                self.drawdpPI()
                #Narrador : “Por facilidad hemos añadido un reloj que te puede ayudar. Trata de entender 
                # qué pasa con cada objeto y toma nota de si la caída de cada objeto depende de su masa o no. 
                # O si del ángulo de inclinación. Recuerda que Galileo dejará caer cada objeto.”
                
                if self.stop == False :
                    
                    self.d61 = TextM('Por facilidad hemos añadido un reloj que te puede ayudar. Trata de  ', (self.x100, self.y100), fontsize= self.f40, color='white')
                    self.d62 = TextM('entender qué pasa con el movimiento de cada objeto y toma nota de  ', (self.x100, self.y100+self.f40), fontsize= self.f40, color='white')      
                    self.d63 = TextM('si su caída depende de la masa o del ángulo de inclinación.  ', (self.x100, self.y100+2*self.f40), fontsize= self.f40, color='white')
                    self.d64 = TextM('Recuerda que los objetos inician en reposo. ', (self.x100, self.y100+3*self.f40), fontsize= self.f40, color='white')
                
                self.d61.draw()
                self.d62.draw()
                self.d63.draw()
                self.stop = self.d64.draw()
                     
                self.App.reiniciark()    
            
            elif self.state == 'Juego':
                self.App.playing = True
                self.rundisplay = False
                self.App.dialoguing = False
                self.App.reiniciark()
            
    def checkstate(self):
        
        if self.App.esc:
            #self.App.running = False
            self.rundisplay = False
            self.App.dialoguing = False
            self.App.reiniciark()
        
        
        elif self.App.enter:
            if self.state == '1':
                self.state = '1.5'
                self.stop = False
            elif self.state == '1.5':
                self.state = '2'
                self.stop = False
            elif self.state == '2':
                self.state = '3'
                self.stop = False
            elif self.state == '3':
                self.state = '4'
                self.stop = False
            elif self.state == '4':
                self.state = '5'
                self.stop = False
            elif self.state == '5':
                self.state = '6'
                self.stop = False
            elif self.state == '6':
                self.state = 'Juego'
                self.stop = False
                
        elif self.App.borrar:
            
            if self.state == 'Juego':
                self.state = '6'
                self.stop = False
            elif self.state == '6':
                self.state = '5'
                self.stop = False
            elif self.state == '5':
                self.state = '4'
                self.stop = False
            elif self.state == '4':
                self.state == '3'
                self.stop = False
            elif self.state == '3':
                self.state = '2'
                self.stop = False
            elif self.state == '2':
                self.state = '1.5'
                self.stop = False
            elif self.state == '1.5':
                self.state = '1'
                self.stop = False
                        
                 
#-----------------------------------------------------------------------------#   

class Preguntas():

    def __init__(self, App):
        
        self.App = App
        self.w , self.h = self.App.w , self.App.h
        self.mw, self.mh = self.App.w/2 , self.App.h/2
        
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
        R = Rect((self.App.w*0.03 , self.App.h*0.075), (self.App.w*0.95, self.App.h*0.25))
        pygame.draw.rect(self.App.screen, (61, 64, 70), R)
    
    def draw_cursor(self):
        self.cursorr = Text('*', pos=(self.cursorrect.x, self.cursorrect.y))
        self.cursorr.draw()
     
    def draw_answer(self):
        
        if self.App.var1 == 0:
            pass
        elif self.App.var1 == 1:
            self.resp_correcta()
        elif self.App.var1 == 2:
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
        self.App.screen.blit(self.App.display, (0,0))
        pygame.display.update()
        self.App.reiniciark()
    
        
#-----------------------------------------------------------------------------#

class Preguntas1(Preguntas):
    
    def __init__(self, App):
        Preguntas.__init__(self, App)
        
        self.state = 'A'
        self.App.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.App.events()
            self.checkstate()
            self.App.screen.blit(fondo, frect)
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
        if self.App.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.App.farriba:
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
        if self.App.enter:
            if self.state == 'A':
                self.App.var1 = 2
            elif self.state == 'B':
                self.App.var1 = 1  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.App.esc:
            self.rundisplay = False

class Preguntas2(Preguntas):
    
    def __init__(self, App):
        Preguntas.__init__(self, App)
        
        self.state = 'A'
        self.App.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.App.events()
            self.checkstate()
            self.App.screen.blit(fondo, frect)
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
        if self.App.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.App.farriba:
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
        if self.App.enter:
            if self.state == 'A':
                self.App.var1 = 1
            elif self.state == 'B':
                self.App.var1 = 2  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.App.esc:
            self.rundisplay = False

class Preguntas3(Preguntas):
    
    def __init__(self, App):
        Preguntas.__init__(self, App)
        
        self.state = 'A'
        self.App.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.App.events()
            self.checkstate()
            self.App.screen.blit(fondo, frect)
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
        if self.App.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.App.farriba:
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
        if self.App.enter:
            if self.state == 'A':
                self.App.var1 = 1
            elif self.state == 'B':
                self.App.var1 = 2  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.App.esc:
            self.rundisplay = False

class Preguntas4(Preguntas):
    
    def __init__(self, App):
        Preguntas.__init__(self, App)
        
        self.state = 'A'
        self.App.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.App.events()
            self.checkstate()
            self.App.screen.blit(fondo, frect)
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
        if self.App.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.App.farriba:
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
        if self.App.enter:
            if self.state == 'A':
                self.App.var1 = 2
            elif self.state == 'B':
                self.App.var1 = 1  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.App.esc:
            self.rundisplay = False
 
class Preguntas5(Preguntas):
    
    def __init__(self, App):
        Preguntas.__init__(self, App)
        
        self.state = 'A'
        self.App.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.App.events()
            self.checkstate()
            self.App.screen.blit(fondo, frect)
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
        if self.App.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.App.farriba:
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
        if self.App.enter:
            if self.state == 'A':
                self.App.var1 = 2
            elif self.state == 'B':
                self.App.var1 = 1  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.App.esc:
            self.rundisplay = False
            
class Preguntas6(Preguntas):
    
    def __init__(self, App):
        Preguntas.__init__(self, App)
        
        self.state = 'A'
        self.App.var1 = 0
        self.cursorrect.midtop = (self.Ex , self.ry1)
    
    def displaypreg(self):
        
        fondo = pygame.image.load("fondo.png")
        fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        frect = fondo.get_rect()
        
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.App.events()
            self.checkstate()
            self.App.screen.blit(fondo, frect)
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
        if self.App.fabajo:
            if self.state=='A':
                self.cursorrect.midtop = (self.Ex , self.ry2)
                self.state='B'
            elif self.state=='B':
                self.cursorrect.midtop = (self.Ex  , self.ry1)
                self.state='A'
            #elif self.state=='C':
                #self.cursorrect.midtop = (self.Ex  , self.ry1)
                #self.state='A'
        elif self.App.farriba:
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
        if self.App.enter:
            if self.state == 'A':
                self.App.var1 = 1
            elif self.state == 'B':
                self.App.var1 = 2  
            #elif self.state == 'C':
                #self.Preg.var1 = 2
                
        if self.App.esc:
            self.rundisplay = False
 
#-----------------------------------------------------------------------------#      

class App():
    
    def __init__(self):
        pygame.init()
        
        pygame.mixer.music.load("audio1.mp3")
        pygame.mixer.music.play(3)
        
        self.running = True
        self.playing = False
        self.dialoguing = False
        self.preguntass = False
        
        
        self.fabajo, self.farriba, self.enter, self.borrar, self.esc = False, False, False, False, False
        
        self.display = pygame.Surface((0,0))
        self.screen = pygame.display.set_mode((0,0), FULLSCREEN)
        self.w, self.h = self.screen.get_width(), self.screen.get_height()
        
        pygame.display.set_caption("hm")
        ic = pygame.image.load("Imagenes/Icono.png")
        pygame.display.set_icon(ic)
              
        self.mainmenu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.curr_menu = self.mainmenu #Menú actual
        
        self.diag1p = Dial_1p(self)
        self.diag2p = Dial_2p(self)
        self.diag3p = Dial_3p(self)
        self.diag4p = Dial_4p(self)
        self.curr_diag = self.diag3p
        
        self.var1 = 0
        self.preg1 = Preguntas1(self)
        self.preg2 = Preguntas2(self)
        self.preg3 = Preguntas3(self)
        self.preg4 = Preguntas4(self)
        self.preg5 = Preguntas5(self)
        self.preg6 = Preguntas6(self)
        self.curr_preg = self.preg6 # Sección de preguntas actual
        
        
    def juego(self):
        
        while self.dialoguing:
            pygame.mixer.music.stop()
            
            self.curr_diag.displaydial()
        
        
        while self.playing:
            pygame.mixer.music.stop()
            
            #self.events()
            #if self.enter or self.atras:
            #    self.playing = False
            
            self.screen.fill(Color(71, 75, 78))
            self.asd = Text('aquí va la simulación', (self.w/2, self.h/2))
            self.asd.draw()
            pygame.display.update()
            self.events()
            
            #self.playing = PlanoInclinado.main()
            #self.reiniciark()
            #pygame.mixer.music.play(4)
           
        while self.preguntass:
            pygame.mixer.music.stop()
            
            self.curr_preg.displaypreg()
            
            
    
    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                self.playing = False
                self.curr_menu.rundisplay = False
                self.curr_diag.rundisplay = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.esc = True
                    #self.running = False
                    self.playing = False 
                if event.key == K_DOWN:
                    self.fabajo = True
                if event.key == K_UP:
                    self.farriba = True
                if event.key == K_RETURN:
                    self.enter = True
                if event.key == K_BACKSPACE:
                    self.borrar = True

    def reiniciark(self):
        self.fabajo, self.farriba, self.enter, self.borrar, self.esc = False, False, False, False, False

#-----------------------------------------------------------------------------#  

a = App()

while a.running:
    a.curr_menu.displaymenu()
    a.juego()
    

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

    def __init__(self, text, pos, fontsize=90, fontname='BebasNeue.otf', color='black', cfondo=(0, 75, 78), time=55):
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
        #self.tfin()        
        
        
        
#-----------------------------------------------------------------------------------#

class Dialogos():
    
    def __init__(self, Introd):
        
        self.Introd = Introd
        self.mw , self.mh = self.Introd.w/2 , self.Introd.h/2
        
        self.rundisplay = True
        
    def diabox(self):
        R = Rect((self.Introd.w*0.03 , self.Introd.h*0.06), (self.Introd.w*0.95, self.Introd.h*0.25))
        pygame.draw.rect(self.Introd.screen, (0, 75, 78), R)
        
    def diaboxPI(self):
        R = Rect((self.Introd.w*0.03 , self.Introd.h*0.07), (self.Introd.w*0.75, self.Introd.h*0.25))
        pygame.draw.rect(self.Introd.screen, (0, 75, 78), R)  
        
    def diabox2(self): #hacer otro cuadro de texto ahora como globo de diálogo más abajo que
        # muestre lo que galileo está diciendo
        nube = pygame.image.load("Imagenes/Nube.png")
        nube = pygame.transform.scale(nube, (round(self.Introd.w*0.67), round(self.Introd.h*0.42)))
        nrect = nube.get_rect()
        nrect.topleft = (self.Introd.w*0.35 , self.Introd.h*0.38)
        self.Introd.screen.blit(nube, nrect)
         
    def diabox3(self): #nube galileo en Tut pI
        nube = pygame.image.load("Imagenes/Nube.png")
        nube = pygame.transform.scale(nube, (round(self.Introd.w*0.67), round(self.Introd.h*0.42)))
        nrect = nube.get_rect()
        nrect.topleft = (self.Introd.w*0.001 , self.Introd.h*0.02)
        self.Introd.screen.blit(nube, nrect)
         
        #R = Rect((self.Introd.w*0.4 , self.Introd.h*0.45), (self.Introd.w*0.55, self.Introd.h*0.25))
        #pygame.draw.rect(self.Introd.screen, (125, 96, 114), R)
        
    def drawdp(self): #muestra el mensaje presione enter para continuar
        self.msj = Text('Presione enter para continuar', (self.mw*1.50 , self.mh*0.7), fontsize=round(self.Introd.w*0.021))
        Re = Rect((self.msj.pos[0]-20, self.msj.pos[1]-10),(self.msj.rect.width+40, self.msj.rect.height+10))
        pygame.draw.rect(self.Introd.screen, (0, 0, 0), Re)
        self.msj.draw()
        
    def drawdpPI(self): #muestra el mensaje presione enter para continuar
        self.msj = Text('Presione enter para continuar', (self.Introd.w*0.74 , self.Introd.h*0.92), fontsize=round(self.Introd.w*0.021))
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
        self.stop = False
        
    def displaydial(self):
        
        #fondo = pygame.image.load("fondo.png")        #---> para poner el fondo 
        #fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        #frect = fondo.get_rect()
        self.x100 = self.Introd.w*0.069
        self.y100 = self.Introd.h*0.11
        self.f50 = round(self.Introd.w*0.034)
        
        self.rundisplay = True
        while self.rundisplay:
            
            self.Introd.events()
            self.checkstate()
            #print(self.state)
            
            if self.state == '1':
                
                self.Introd.screen.fill(Color(71, 75, 78))
                self.diabox()
                self.drawdp()
                
                if self.stop == False:
                
                    self.d1 = TextM('Corre el siglo XVI. Despertaste en los recuerdos del maestro Galileo Galilei,', (self.x100, self.y100), fontsize= self.f50, color='white')
                    self.d12 = TextM('y estoy aquí para ayudarte a entender qué está pasando.', (self.x100, self.y100+self.f50), fontsize= self.f50, color='white')
                
                self.d1.draw()
                self.stop = self.d12.draw()
                
                self.Introd.reiniciark()
                
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
                        
                self.Introd.reiniciark()
                
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
                
                self.Introd.reiniciark()
                
            elif self.state == 'Juego':
                self.Introd.reiniciark()
                self.Introd.curr_diag = self.Introd.diag2p
                self.rundisplay = False
    
            
    def checkstate(self):
        
        if self.Introd.esc:
            self.Introd.running = False
            self.rundisplay = False
        
        elif self.Introd.enter:
            if self.state == '1':
                self.state = '2'
                self.stop = False
            elif self.state == '2':
                self.state = '3'
                self.stop = False
            elif self.state == '3':
                self.state = 'Juego'
                self.stop = False
                
        elif self.Introd.borrar:
            if self.state == 'Juego':
                self.state == '3'
                self.stop = False
            elif self.state == '3':
                self.state = '2'
                self.stop = False
            elif self.state == '2':
                self.state = '1'
                self.stop = False
       
#-----------------------------------------------------------------------------------#           
       
class Dial_2p(Dialogos):
    
    def __init__(self, Introd):   
        Dialogos.__init__(self, Introd)
        
        self.state = '1'
        self.stop = False
        
    def displaydial(self):
        
        #fondo = pygame.image.load("fondo.png")        -----> para poner el fondo 
        #fondo = pygame.transform.scale(fondo,(self.App.w, self.App.h))
        #frect = fondo.get_rect()
        
        self.x100 = self.Introd.w*0.069
        self.y100 = self.Introd.h*0.11
        self.f50 = round(self.Introd.w*0.034)
        
        self.xdg = self.Introd.w*0.42
        self.ydg = self.Introd.h*0.47
        self.f40 = round(self.Introd.w*0.027)
              
        
        self.Introd.screen.fill(Color(71, 75, 78))  
        self.rundisplay = True
        while self.rundisplay:
            
            self.Introd.events()
            self.checkstate()
            
            if self.state == '1':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
                
                
                if self.stop == False :
                    
                    self.d1 = TextM('Mira, ahí está Galileo, ¿puedes leer su mente?         ', (self.x100, self.y100), fontsize= self.f50, color='white')
                    self.g1 = TextM('  .     .     .  ', (self.xdg, self.ydg), fontsize= self.f50, cfondo=(255, 255, 255))
                
                self.d1.draw()
                self.stop = self.g1.draw()
                
                self.Introd.reiniciark()
                
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
                     
                self.Introd.reiniciark()
                
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
              
                self.Introd.reiniciark()
            
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
                
                self.Introd.reiniciark()  
            
            
            elif self.state == 'Juego':
                self.Introd.playing = True
                self.rundisplay = False
    
            
    def checkstate(self):
        
        if self.Introd.esc:
            self.Introd.running = False
            self.rundisplay = False
        
        elif self.Introd.enter:
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
                
        elif self.Introd.borrar:
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
            
#------------------------------------------------------------------------------------#


    
# "Modificar su altura y longitud (y de esta forma variar el ángulo de inclinación),"(flechas)

# "Y usar diferentes materiales para las esferas que van a caer, cada material tiene un rango
# de masa distinto ¡Empecemos!

#Narrador : “Por facilidad hemos añadido un reloj que te puede ayudar. Trata de entender 
# qué pasa con cada objeto y toma nota de si la caída de cada objeto depende de su masa o no. 
# O si del ángulo de inclinación. Recuerda que Galileo dejará caer cada objeto.”

class Dial_3p(Dialogos):
    
    def __init__(self, Introd):   
        Dialogos.__init__(self, Introd)
        
        self.state = '1'
        self.stop = False
        
    def displaydial(self):
        
        fondo = pygame.image.load("Imagenes/ftutpi.png")       # -----> para poner el fondo 
        fondo = pygame.transform.scale(fondo,(self.Introd.w, self.Introd.h))
        frect = fondo.get_rect()
        
        self.x100 = self.Introd.w*0.069
        self.y100 = self.Introd.h*0.11
        self.f50 = round(self.Introd.w*0.034)
        
        self.xda = self.Introd.w*0.55
        self.yda = self.Introd.h*0.88
        
        self.xdg = self.Introd.w*0.42
        self.ydg = self.Introd.h*0.47
        self.f40 = round(self.Introd.w*0.027)
        self.f60 = round(self.Introd.w*0.04)
              
        
        self.Introd.screen.fill(Color(71, 75, 78))  
        self.rundisplay = True
        while self.rundisplay:
            
            self.Introd.events()
            self.checkstate()
            
            if self.state == '6':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
                    
                if self.stop == False :
                    
                    self.d1 = TextM('- - -    ', (self.x100, self.y100), fontsize= self.f50, color='white')
                    
                    self.g1 = TextM('Sé que la caída de los objetos no ocurre a velocidad ', (self.xdg, self.ydg), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g11 = TextM('constante, ya que he visto que cuando un objeto ', (self.xdg, self.ydg+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g12 = TextM('cae por una colina su velocidad va aumentando.', (self.xdg, self.ydg+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    #self.g13 = TextM(' ...', (self.xdg, self.ydg+3*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                  
                self.d1.draw()
                self.g1.draw()
                self.g11.draw()
                #self.g12.draw()
                self.stop = self.g12.draw()
                
                self.Introd.reiniciark()
            
            elif self.state == '1.5':
                
                self.diabox()
                self.diabox2()
                self.drawdp()
                    
                if self.stop == False :
                    
                    self.d1 = TextM('- - -    ', (self.x100, self.y100), fontsize= self.f50, color='white')
                    
                    self.g1 = TextM('¿Cómo puedo estudiar este movimiento?     ', (self.xdg, self.ydg), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g11 = TextM('  .    .    .             ', (self.xdg, self.ydg+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g12 = TextM('  ¡Tengo una idea!   ', (self.xdg, self.ydg+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    
                  
                self.d1.draw()
                self.g1.draw()
                self.g11.draw()
                self.stop = self.g12.draw()
                
                self.Introd.reiniciark()
                
            elif self.state == '2':
                       
                self.Introd.screen.fill(Color(71, 75, 78))     
                
                if self.stop == False :
                    
                    self.d2 = TextM('  .     .     .  ', (self.Introd.w*0.35, self.Introd.h*0.4), fontsize= round(self.Introd.w*0.1), color='white', cfondo=(71, 75, 78), time=70)
                    self.pe = TextM('Presione enter para continuar', (self.xda, self.yda), fontsize= self.f60, color='white', cfondo=(71, 75, 78)) #fontsi 60
                 
                self.d2.draw()
                self.stop = self.pe.draw()
                
                self.Introd.reiniciark()
                
            elif self.state == '3':
                            
                self.Introd.screen.blit(fondo, frect)
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
                     
                self.Introd.reiniciark()
                
            elif self.state == '4':
                
                self.Introd.screen.blit(fondo, frect)
                self.diabox3()
                self.drawdpPI()
            
                #Modificar su altura y longitud (y de esta forma variar el ángulo de inclinación),
                if self.stop == False :
                    
                    self.g4 = TextM('  Por ejemplo puedo modificar su altura y ', (self.x100, self.y100), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g41 = TextM(' longitud, (y de esta forma variar el ángulo ', (self.x100, self.y100+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g42 = TextM(' de inclinación)', (self.x100, self.y100+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                               
                
                self.g4.draw()
                self.g41.draw()
                self.stop = self.g42.draw()
                     
                self.Introd.reiniciark()
            
            elif self.state == '5':
                
                self.Introd.screen.blit(fondo, frect)
                self.diabox3()
                self.drawdpPI()
                
                
                if self.stop == False :
                    
                    self.g5 = TextM('  Y también puedo usar diferentes materiales para  ', (self.x100, self.y100), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g51 = TextM(' las esferas que van a caer, cada material tiene  ', (self.x100, self.y100+self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g52 = TextM(' un rango de masa distinto. ', (self.x100, self.y100+2*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))
                    self.g53 = TextM('    ¡Empecemos!   ', (self.x100, self.y100+3*self.f40), fontsize= self.f40, cfondo=(255, 255, 255))           
                
                self.g5.draw()
                self.g51.draw()
                self.g52.draw()
                self.stop = self.g53.draw()
                     
                self.Introd.reiniciark()
                
            elif self.state == '1':
                
                self.Introd.screen.blit(fondo, frect)
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
                     
                self.Introd.reiniciark()    
            
            elif self.state == 'Juego':
                self.Introd.playing = True
                self.rundisplay = False
    
            
    def checkstate(self):
        
        if self.Introd.esc:
            self.Introd.running = False
            self.rundisplay = False
        
        elif self.Introd.enter:
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
                
        elif self.Introd.borrar:
            
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
        self.diag3p = Dial_3p(self)
        self.curr_diag = self.diag3p #parte de diálogos actual
    
    
    def juego(self):
        
        while self.playing:
            
            self.screen.fill(Color(71, 75, 78))
            self.asd = Text('aquí va la simulación', (self.w/2, self.h/2))
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
  



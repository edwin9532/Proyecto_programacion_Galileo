
import pygame, pymunk,time,Boton_,pygame.gfxdraw#,relog

def main():
    pygame.init()

    display = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#display = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    space = pymunk.Space()
    space.gravity = 0, 500
    FPS = 80
    ms = clock.tick(FPS)
    background = pygame.image.load("Imagenes/Fondo_12.jpg").convert()
     

    def convert_coordinates(point):
        return point[0], 600-point[1]

    def crear(space,pos):
        body = pymunk.Body(1,100,body_type =pymunk.Body.DYNAMIC)
        body.position = pos
        shape = pymunk.Circle(body,40)
        shape.density = 1
        space.add(body,shape)
        return shape

    def dibujar(bola,image):
            pos_x = int(bola.body.position.x)
            pos_y = int(bola.body.position.y)
            objeto_rect = image.get_rect(center=(pos_x,pos_y))
            display.blit(image,objeto_rect)
        
        

    segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_shape = pymunk.Segment(segment_body, (0,710),(2000,710),10)
    space.add(segment_body,segment_shape)
#perfect inelastic collition

#apple_surface =pygame.image.load("Bola_Madera.png")
    image = pygame.image.load("Imagenes/Bola_Madera.png")
    image = pygame.transform.scale(image, (80,80))


#pygame.mixer.init()
    b = pygame.font.Font("Fonts/BebasNeue.otf", 30)
    c = pygame.font.Font("Fonts/BebasNeue.otf", 40)
    
    
    
    info = pygame.display.Info()
    
    B = pygame.image.load('Imagenes/Boton.png')
    Bp = pygame.image.load('Imagenes/Boton_p.png')
    
    material = Boton_.Boton(info.current_w-90,370, B, Bp, 0.25,"Material",font_size=27)
    
    t,escogido = False,False
    Tipos = ["Imagenes/Bola_Madera.png","Imagenes/Bola_Roca.png","Imagenes/Bola_Metal.png"]
    
    bola_= crear(space, (0,0))
    
    class Bola_T:
        def __init__(self, tipo, i, tipo_n,font_name="Fonts/BebasNeue.otf",font_size=33,pos=(info.current_w-330,520)):
            self.pos_i = pos
            self.tipo = i
            self.pos = convert_coordinates((pos[0]+4*30*i,pos[1]+40))
            self.nombre = tipo_n
            self.font = pygame.font.SysFont(font_name, font_size, False)
            self.image = pygame.image.load(tipo)
            self.image = pygame.transform.scale(self.image, (2*40,2*40))
            self.rect = self.image.get_rect()
            self.rect.center = (self.pos[0]+40,self.pos[1]+40)
            self.clicked = False
            
        def draw(self):
            mpos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mpos):
                self.image = pygame.transform.scale(self.image, (2*(40+5),2*(40+5)))
                display.blit(self.image, (self.pos[0]-5,self.pos[1]-5))
                
                txt = self.font.render(self.nombre, 1, (0,0,0))
                txt_rect = txt.get_rect(center=(self.rect.x+self.image.get_width()/2 -5, self.rect.y+self.image.get_height()/2 -5))
                display.blit(txt, txt_rect)
                t = True
                
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:                
                    self.clicked = True
                    t = False
            else:
                self.image = pygame.transform.scale(self.image, (2*40,2*40))
                display.blit(self.image, self.pos)
                t = True
        
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
            return t, self.tipo, self.clicked   
    
    def Tipo():
        
        bola_Ma = Bola_T(Tipos[0],0,"Madera")
        bola_R = Bola_T(Tipos[1],1,"Roca")
        bola_Me = Bola_T(Tipos[2],2,"Metal")
        
        bolas = [bola_Ma,bola_R,bola_Me]
        
        for bolat in bolas:
            t, tipo, escogido = bolat.draw()
            if not t: break
        
        
        return t, tipo, escogido, False
    
    inicio = True
    
    tiempo = 0
    fontcro = pygame.font.Font("Fonts/Digital-7.ttf", 35)
    pulse = 0
    ps = 0
    crono_p = pygame.image.load("Imagenes/Crono_p.png")
    crono_ = pygame.image.load("Imagenes/Crono.png")
    simulando = False
    
    
    #Plano = pygame.image.load("Imagenes/Plano1.jpg")
    #Plano = pygame.image.load("Imagenes/Plano2.jpg")
    Plano = pygame.image.load("Imagenes/Plano3.jpg")
    
    
    dialogo1_0 = b.render("ALTURA DE LA TORRE: 57 m:", 1, (110,0,100))  
    relog1 = b.render("El tiempo",1,(0,0,0))
    relog2 = b.render("de ca??da es:",1,(0,0,0))
    final = c.render("Presione  X",1,(250,0,0))
    final2 = c.render("para continuar",1,(250,0,0))
    a1 = b.render("3 m",1,(0,0,0))
    a2 = b.render("6 m",1,(0,0,0))
    a3 = b.render("9 m",1,(0,0,0))
    a4 = b.render("12 m",1,(0,0,0))
    a5 = b.render("15 m",1,(0,0,0)) 

    cont=[0,0]
    bc=0
    sig = 0
    fin = False



    while True:
            for event in pygame.event.get():  #revisar lo ingresado
                if event.type == pygame.QUIT:  #para cerrar el juego
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: return
                    if event.key == pygame.K_x:
                        if fin: return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (bola_._id in space._shapes): space.remove(bola_)
                    bola_ = crear(space,event.pos)
                    simulando, tiempo = True, 0
                    inicio = False
                    cont[0]+=1
        #display.fill((255,255,255))
            
        
            display.blit(background, [-200,-55])    
            
            
            if (material.draw(display) or t):
                # fondo                
                t, tipo, escogido, simulando = Tipo()
                bc+=1
                if bc==1:
                    cont[0]-=1
            else:
                bc=0
                # fondo
                if escogido:
                    image = pygame.image.load(Tipos[tipo])
                    image = pygame.transform.scale(image, (80,80))
                    space.remove(bola_)
                    escogido = False
                    simulando = False
                    cont[0]-=1
                    cont[1]+=1
        
            if inicio: fontcro = pygame.font.Font("Fonts/Digital-7.ttf", 35)
            if simulando:
                tiempo+=ms
                fontcro = pygame.font.Font("Fonts/Digital-7.ttf", 35)
                pulse = 0
                ps = 0
                c_image=crono_p
            if not simulando: c_image=crono_
            if not simulando and not inicio and ps<=10:
                if pulse >= 10 and pulse <20:
                    fontcro = pygame.font.Font("Fonts/Digital-7.ttf", 35)
                    pulse+=1
                elif pulse <10:
                    fontcro = pygame.font.Font("Fonts/Digital-7.ttf", 38)
                    pulse+=1
                elif pulse == 20:
                    pulse=0
                    ps+=1
        
        
            if bola_.body.position.y >= 660:
                simulando, ini = False, False
        
        
        
        
            start = time.time()
       # x, y = convert_coordinates(pos)
     #   pygame.draw.circle(display,(10,110,10),(int(x),int(y)),10)
        
            pygame.draw.line(display,(143, 37, 14),(0,710),(2000,710),20)
            pygame.gfxdraw.textured_polygon(display, [(0,info.current_h),(0,705),(info.current_w,705),(info.current_w,info.current_h)],Plano,0,0)
        
      
      #      display.blit(dialogo1_0,(360,450))
            display.blit(relog1,(info.current_w-140,200))
            display.blit(relog2,(info.current_w-140,225))
            
            if sig != 2:
                for co in cont:
                    if co>=3: sig+=1
                    else: sig = 0
            if sig == 2:
                fin = True
                display.blit(final,(1145,500))
                display.blit(final2,(1145,535))
            else: sig=0
            
            display.blit(a1,(300,573))
            display.blit(a2,(300,460))
            display.blit(a3,(300,347))
            display.blit(a4,(290,225))
            display.blit(a5,(290,110))            
            
            
            
            c_image = pygame.transform.scale(c_image, (int(c_image.get_width()*0.2),int(c_image.get_height()*0.2)))
            c_rect = c_image.get_rect()
            c_rect.center = (info.current_w-140+c_image.get_width()//2, 290) # Esto para cambiar posici??n del reloj
            display.blit(c_image, (c_rect.x, c_rect.y))
            
            crono = fontcro.render(str(round(tiempo/1000,2)), 1, (57,255,20))
            display.blit(crono, (info.current_w-140+c_image.get_width()//4, 280)) # Esto para cambiar posici??n de los n??meros en el reloj
            
            
            #print(cont)
                
            
            if bola_._id in space._shapes and not inicio and not t:
                dibujar(bola_,image)
            
            pygame.display.update()
            clock.tick(FPS)
            space.step(1/FPS)
            
            
            stop = time.time()
            #print("El tiempo de caida es:", stop - start)
    
  #  start = time.time()
    #relog    
 #   stop = time.time()
   

#    print("El tiempo de caida es:", stop - start)
    pygame.quit()
#main()

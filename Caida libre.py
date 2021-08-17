
import pygame, pymunk,time,Boton_#,relog

def main():
    pygame.init()

    display = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#display = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    space = pymunk.Space()
    space.gravity = 0, 500
    FPS = 80
    background = pygame.image.load("Imagenes/Fondo_11.jpg").convert()
     

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
    a = pygame.font.Font(None, 60)
    b = pygame.font.Font(None, 40)
    c = pygame.font.Font(None, 20)
    
    
    info = pygame.display.Info()
    
    B = pygame.image.load('Imagenes/Boton.png')
    Bp = pygame.image.load('Imagenes/Boton_p.png')
    
    material = Boton_.Boton(info.current_w-80,365, B, Bp, 0.25,"Material")
    
    t,escogido = False,False
    Tipos = ["Imagenes/Bola_Madera.png","Imagenes/Bola_Roca.png","Imagenes/Bola_Metal.png"]
    
    bola_= crear(space, (0,0))
    
    class Bola_T:
        def __init__(self, tipo, i, tipo_n,font_name="BebasNeue.otf",font_size=33,pos=(info.current_w//5,350)):
            self.pos_i = pos
            self.tipo = i
            self.pos = convert_coordinates((pos[0]+4*40*i,pos[1]+40))
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
        
        
        return t, tipo, escogido
    


    def game(t,escogido,image,inicio,bola_):
        while True:
            for event in pygame.event.get():  #revisar lo ingresado
                if event.type == pygame.QUIT:  #para cerrar el juego
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (bola_._id in space._shapes): space.remove(bola_)
                    bola_ = crear(space,event.pos)
                    inicio = False
        #display.fill((255,255,255))
            start = time.time()
            display.blit(background, [-200,-55])    
       # x, y = convert_coordinates(pos)
     #   pygame.draw.circle(display,(10,110,10),(int(x),int(y)),10)
        
            pygame.draw.line(display,(0,0,0),(0,710),(2000,710),20)
        
      
            display.blit(dialogo1_0,(360,450))
            display.blit(titulo,(470,10))
            display.blit(relog,(470,550))
            display.blit(final,(1010,540))
            display.blit(final2,(1010,565))
            
            if (material.draw(display) or t):
                # fondo                
                t, tipo, escogido = Tipo()
            else:
                # fondo
                if escogido:
                    image = pygame.image.load(Tipos[tipo])
                    image = pygame.transform.scale(image, (80,80))
                    space.remove(bola_)
                    escogido = False
                
            
            if bola_._id in space._shapes and not inicio and not t:
                dibujar(bola_,image)
            
            pygame.display.update()
            clock.tick(FPS)
            space.step(1/FPS)
            
            
            stop = time.time()
            print("El tiempo de caida es:", stop - start)
    
    dialogo1_0 = b.render("ALTURA DE LA TORRE: 57 m:", 1, (110,0,100))  
    titulo = a.render("CAÍDA LIBRE",1,(0,100,0))
    relog = c.render("El tiempo de caída es:",1,(0,0,0))
    final = b.render("Presione X",1,(250,0,0))
    final2 = b.render("para continuar",1,(250,0,0))
    
  #  start = time.time()
    game(t,escogido,image,True,bola_)
    #relog    
 #   stop = time.time()
   

#    print("El tiempo de caida es:", stop - start)
    pygame.quit()
main()

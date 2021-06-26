import Boton_, Sliders, pygame, pymunk,pygame.gfxdraw, numpy as np

def main():

    pygame.init()
    screen,running = pygame.display.set_mode((0,0),pygame.FULLSCREEN),True
    #pygame.display.set_caption("hm")
    #ic = pygame.image.load("Imagenes/1.png")
    #pygame.display.set_icon(ic)
    pygame.display.flip()
    info = pygame.display.Info()
    fondo = pygame.image.load("Imagenes/Fondo_11B.jpg")
    fondo = pygame.transform.scale(fondo, (info.current_w, info.current_h))
    fondo_b = fondo
    fondo = pygame.image.load("Imagenes/Fondo_11.jpg")
    fondo = pygame.transform.scale(fondo, (info.current_w, info.current_h))
    fondo_i = fondo
    
        
    class Bola_T:
        def __init__(self, pos, r, tipo, i, tipo_n,font_name="BebasNeue.otf",font_size=33):
            self.pos_i = pos
            self.tipo = i
            self.pos = conv_coord((pos[0]+4*rm*i,pos[1]+rm))
            self.nombre = tipo_n
            self.font = pygame.font.SysFont(font_name, font_size, False)
            self.r = r
            self.image = pygame.image.load(tipo)
            self.image = pygame.transform.scale(self.image, (2*rm,2*rm))
            self.rect = self.image.get_rect()
            self.rect.center = (self.pos[0]+rm,self.pos[1]+rm)
            self.clicked = False
            
        def draw(self):
            mpos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mpos):
                self.image = pygame.transform.scale(self.image, (2*(rm+5),2*(rm+5)))
                screen.blit(self.image, (self.pos[0]-5,self.pos[1]-5))
                
                txt = self.font.render(self.nombre, 1, (0,0,0))
                txt_rect = txt.get_rect(center=(self.rect.x+self.image.get_width()/2 -5, self.rect.y+self.image.get_height()/2 -5))
                screen.blit(txt, txt_rect)
                t = True
                
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:                
                    self.clicked = True
                    t = False
            else:
                self.image = pygame.transform.scale(self.image, (2*rm,2*rm))
                screen.blit(self.image, self.pos)
                t = True
        
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
            return t, self.tipo, self.clicked
            
            
        
            
    
    def conv_coord(pos):
        return pos[0], info.current_h-pos[1]
    
    def bola(space,pos,r,m,):
        body = pymunk.Body(m,200,body_type= pymunk.Body.DYNAMIC)
        body.position = pos
        shape = pymunk.Circle(body, r)
        #shape.elasticity = 1
        space.add(body,shape)
        return shape
    
    def draw_bola(bola,r,tipo):
        bola_im = pygame.image.load(Tipos[tipo])
        pos_x,pos_y = conv_coord(bola.body.position)
        bola_im = pygame.transform.scale(bola_im, (2*r,2*r))
        screen.blit(bola_im, (int(pos_x)-r,int(pos_y)-r))
        
    
    def plano(space,pos_plano,w):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, pos_plano[0], pos_plano[1], w)
        #shape.elasticity = 1
        space.add(body,shape)
        return shape
        
    def draw_plano(plano):
        pygame.draw.line(screen, (143, 37, 14), conv_coord(pos_plano[0]), conv_coord(pos_plano[1]),5)
    
    def masa_radio(m):
        l = np.linspace(20,40,100)
        r = int(l[m-1])
        return r
    
    def nums(s,y,u):
            if s==masa: l=int(s.val)
            else: l=int(s.val)/100
            txt = font.render(str(l)+u, 1, (0,0,0))
            screen.blit(txt, (info.current_w-210, y))
    
    def Tipo(r,pos):
        if (bola_._id in space._shapes): space.remove(bola_)
        
        bola_Ma = Bola_T(pos,r,Tipos[0],0,"Madera")
        bola_R = Bola_T(pos,r,Tipos[1],1,"Roca")
        bola_Me = Bola_T(pos,r,Tipos[2],2,"Metal")
        
        bolas = [bola_Ma,bola_R,bola_Me]
        
        for bolat in bolas:
            t, tipo, escogido = bolat.draw()
            if not t: break
        
        return t, tipo, escogido
        
        
    t = False
    Tipos = ["Imagenes/Bola_Madera.png","Imagenes/Bola_Roca.png","Imagenes/Bola_Metal.png"]
    tipo = 0
    
    font = pygame.font.SysFont("BebasNeue.otf", 23, False)
    clock = pygame.time.Clock()
    space = pymunk.Space()
    space.gravity = (0,-981)
    fps = 50
    pos_plano = [(0,0),(info.current_w,0)]
    
    
    c = True
    aj = np.linspace(1.1,.67,info.current_h)
    block = plano(space,[(1,1),(1,2)],0)
    rm = 40
    
    # Sliders
    masa = Sliders.Slider("Masa", 50, 100, 1, 20, info.current_w-120, font, screen)
    altura = Sliders.Slider("Altura", info.current_h//2, info.current_h-(2*rm)*0.85, 0, 80, info.current_w-120, font, screen)
    longitud = Sliders.Slider("Longitud", info.current_w//2, info.current_w, rm*2, 140, info.current_w-120, font, screen)
    slides = [masa,altura,longitud]
    inicio = True
    
    # Botones
    B = pygame.image.load('Imagenes/Boton.png').convert_alpha()
    Bp = pygame.image.load('Imagenes/Boton_p.png').convert_alpha()
    
    start = Boton_.Boton(info.current_w-70,230, B, Bp, 0.25,"Simular")
    restart = Boton_.Boton(info.current_w-70,275, B, Bp, 0.25,"Reiniciar")
    material = Boton_.Boton(info.current_w-70,320, B, Bp, 0.25,"Material")
    
    # Objetos iniciales y de borde
    bola_ = bola(space,(rm,rm),rm,masa.val)
    plano_ = plano(space,pos_plano,2.5)
    pared = plano(space,[(info.current_w,0),(info.current_w,info.current_h)],0)
    suelo = plano(space,[(0,0),(info.current_w,0)],0)
    
    # Relleno del plano, tres opciones
    
    #Plano = pygame.image.load("Imagenes/Plano1.jpg")
    Plano = pygame.image.load("Imagenes/Plano2.jpg")
    #Plano = pygame.image.load("Imagenes/Plano3.jpg")
    
    simulando = False
    escogido = False
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                s_pos = pygame.mouse.get_pos()
                for s in slides:
                    if s.button_rect.collidepoint(s_pos) and not t:
                        s.hit,c = True,False
            elif event.type == pygame.MOUSEBUTTONUP and not t:
                for s in slides:
                    s.hit,c = False,True
                    
        r = masa_radio(int(masa.val))
        
        
        screen.blit(fondo,(0,0))
        for s in slides:
            if (s.hit or inicio) and not t:
                inicio = False
                space.remove(bola_,plano_)
                if (block._id in space._shapes): space.remove(block)
                if c == False: s.move()
                pos_plano = [(0,int(altura.val)),(int(longitud.val),0)]
                plano_ = plano(space,pos_plano,2.5)
                bola_ = bola(space,(r,int(altura.val)+r*aj[int(altura.val)]),r,masa.val)
                block = plano(space,[(r*2,int(altura.val)+r),(r*2,0)],0)
                simulando = False
                
        nums(masa,30," kg")
        nums(altura,90," m")
        nums(longitud,150," m")
        
        for s in slides:
            s.draw()
            
        if (material.draw(screen) or t):
            
            if (bola_._id in space._shapes):
                pt = ((r,int(altura.val)+r*aj[int(altura.val)]))
                if block._id not in space._shapes:
                    block = plano(space,[(r*2,int(altura.val)+r),(r*2,0)],0)
                t, tipo, escogido = Tipo(r,pt)                
                fondo = fondo_b
            else:
                t, tipo, escogido = Tipo(r,pt)
        else:
            fondo = fondo_i
            if escogido:
                bola_ = bola(space,(r,int(altura.val)+r*aj[int(altura.val)]),r,masa.val)
                escogido = False
        
        if start.draw(screen) and not t:
            if block._id in space._shapes:
                space.remove(block)
                simulando = True
        if restart.draw(screen) and not t:
            masa.hit = True
            simulando = False
            
        pygame.gfxdraw.textured_polygon(screen, [conv_coord((0,0)),conv_coord(pos_plano[0]),conv_coord(pos_plano[1])],Plano,0,0)
            
        
        ms = clock.tick(fps)
        if (bola_._id in space._shapes) or not t: draw_bola(bola_,r,tipo)
        draw_plano(plano_)
        space.step(1/fps)
        pygame.display.update()
        #print(ms)
    return False

#main()
import Boton_, Sliders, pygame, pymunk,pygame.gfxdraw, numpy as np

def main():

    pygame.init()
    screen,running = pygame.display.set_mode((0,0),pygame.FULLSCREEN),True
    pygame.display.set_caption("Mente Brillante")
    ic = pygame.image.load("Imagenes/Icono.png")
    pygame.display.set_icon(ic)
    pygame.display.flip()
    info = pygame.display.Info()
    
    fondo = pygame.image.load("Imagenes/Fondo_11B.jpg")
    fondo = pygame.transform.scale(fondo, (info.current_w, info.current_h))
    fondo_b = fondo
    fondo = pygame.image.load("Imagenes/Fondo_11.jpg")
    fondo = pygame.transform.scale(fondo, (info.current_w, info.current_h))
    fondo_i = fondo
    
    crono_p = pygame.image.load("Imagenes/Crono_p.png")
    crono_ = pygame.image.load("Imagenes/Crono.png")
    notepad = pygame.image.load("Imagenes/Notepad.png")
    notepad = pygame.transform.scale(notepad, (int(notepad.get_width()*0.68),int(notepad.get_height()*0.68)))
    np_rect = notepad.get_rect()
    np_rect.center = (info.current_w-notepad.get_width()//2,500)
    
        
    class Bola_T:
        def __init__(self, pos, r, tipo, i, tipo_n,font_name="Fonts/BebasNeue.otf",font_size=33):
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
    
    def masa_radio(m,n,max,min):
        lr = np.arange(min,max + 1)
        l = np.linspace(20,40,n)
        r = int(l[list(lr).index(m)])
        return r, list(lr).index(m)
    
    def nums(s,y,u):
            if s==masa: l=int(s.val)
            else: l=int(s.val)/100
            txt = font.render(str(l)+u, 1, (0,0,0))
            screen.blit(txt, (info.current_w-220, y))
    
    def Tipo(r,pos,n,max,min,mia):
        if (bola_._id in space._shapes): space.remove(bola_)
        
        bola_Ma = Bola_T(pos,r,Tipos[0],0,"Madera")
        bola_R = Bola_T(pos,r,Tipos[1],1,"Roca")
        bola_Me = Bola_T(pos,r,Tipos[2],2,"Metal")
        
        bolas = [bola_Ma,bola_R,bola_Me]
        
        for bolat in bolas:
            t, tipo, escogido = bolat.draw()
            if not t: break
        
        if tipo == 0 and not t:
            masa.refresh(np.arange(1,21)[int(mia*20/(max-min +1))], 20, 1)
            n,max,min = 20,20,1
        elif tipo == 1 and not t:
            masa.refresh(np.arange(20,61)[int(mia*41/(max-min +1))], 60, 20)
            n,max,min = 41,60,20
        elif tipo == 2 and not t:
            masa.refresh(np.arange(60,101)[int(mia*41/(max-min +1))], 100, 60)
            n,max,min = 41,100,60
        
        return t, tipo, escogido, n, max, min
        
        
    t = False
    Tipos = ["Imagenes/Bola_Madera.png","Imagenes/Bola_Roca.png","Imagenes/Bola_Metal.png"]
    tipo = 0
    
    font = pygame.font.SysFont("Fonts/BebasNeue.otf", 23, False)
    font.set_underline(True)
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
    masa = Sliders.Slider("Masa", 20, 20, 1, 65, info.current_w-130, font, screen)
    altura = Sliders.Slider("Altura", info.current_h//2, info.current_h-(2*rm)*0.85, 0, 125, info.current_w-130, font, screen)
    longitud = Sliders.Slider("Longitud", info.current_w//2, info.current_w, rm*2, 185, info.current_w-130, font, screen)
    slides = [masa,altura,longitud]
    inicio = True
    n,max,min = 20,20,1
    
    # Botones
    B = pygame.image.load('Imagenes/Boton.png').convert_alpha()
    Bp = pygame.image.load('Imagenes/Boton_p.png').convert_alpha()
    B1 = pygame.image.load('Imagenes/Boton1.png').convert_alpha()
    Bp1 = pygame.image.load('Imagenes/Boton1_p.png').convert_alpha()
    
    start = Boton_.Boton(info.current_w-80,275, B, Bp, 0.25,"Simular")
    restart = Boton_.Boton(info.current_w-80,320, B, Bp, 0.25,"Reiniciar")
    material = Boton_.Boton(info.current_w-80,365, B, Bp, 0.25,"Material")
    siguiente = Boton_.Boton(info.current_w-80, 445, B1, Bp1, 0.3, "Avanzar",font_size=30,font_color=(255,255,255)) # No sé si se vea mejor negro que blanco.
    
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
    cont = [0,0,0,0,0]
    sig = 0
    escogido = False
    
    tiempo = 0
    fontcro = pygame.font.Font("Fonts/Digital-7.ttf", 35)
    pulse = 0
    ps = 0
    ini = True
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
                if event.key == pygame.K_x: running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                s_pos = pygame.mouse.get_pos()
                for s in slides:
                    if s.button_rect.collidepoint(s_pos) and not t:
                        if not s.hit:
                            cont[slides.index(s)]+=1
                        s.hit,c = True,False
            elif event.type == pygame.MOUSEBUTTONUP and not t:
                for s in slides:
                    s.hit,c = False,True
                    
        r, mia = masa_radio(int(masa.val),n,max,min)
        
        
        screen.blit(fondo,(0,0))
        for s in slides:
            if (s.hit or inicio) and not t:
                inicio = False
                space.remove(plano_)
                if (bola_._id in space._shapes): space.remove(bola_)
                if (block._id in space._shapes): space.remove(block)
                if c == False: s.move()
                pos_plano = [(0,int(altura.val)),(int(longitud.val),0)]
                plano_ = plano(space,pos_plano,2.5)
                bola_ = bola(space,(r,int(altura.val)+r*aj[int(altura.val)]),r,masa.val)
                block = plano(space,[(r*2,int(altura.val)+r),(r*2,0)],0)
                simulando = False
                ini = True
        
        screen.blit(notepad,(info.current_w-notepad.get_width(),0))
        
        nums(masa,75," kg")
        nums(altura,135," m")
        nums(longitud,195," m")
        
        for s in slides:
            s.draw()
            
        if (material.draw(screen) or t):
            
            if (bola_._id in space._shapes):
                pt = ((r,int(altura.val)+r*aj[int(altura.val)]))
                if block._id not in space._shapes:
                    block = plano(space,[(r*2,int(altura.val)+r),(r*2,0)],0)
                t, tipo, escogido, n, max, min = Tipo(r,pt,n,max,min,mia)
                fondo = fondo_b
            else:
                t, tipo, escogido, n, max, min = Tipo(r,pt,n,max,min,mia)
        else:
            fondo = fondo_i
            if escogido:
                if (bola_._id in space._shapes): space.remove(bola_)
                bola_ = bola(space,(r,int(altura.val)+r*aj[int(altura.val)]),r,masa.val)
                escogido = False
                cont[3]+=1
        
        if start.draw(screen) and not t:
            if block._id in space._shapes:
                space.remove(block)
                simulando, tiempo = True, 0
                cont[4]+=1
        if restart.draw(screen) and not t:
            masa.hit = True
            simulando, ini = False, True
            
        if sig != 5:
            for co in cont:
                if co>=2: sig+=1
                else: sig = 0
        if sig == 5:
            if siguiente.draw(screen) and not t:
                running = False
                # Aquí pasaría al siguiente nivel. 
                # Se activa el botón una vez se haya modificado mínimo 2 veces la masa, la altura, la longitud, y el material, y se haya simluado mínimo 2 veces.
        else: sig=0
            
        pygame.gfxdraw.textured_polygon(screen, [conv_coord((0,0)),conv_coord(pos_plano[0]),conv_coord(pos_plano[1])],Plano,0,0)
        
        angulo = font.render("Ángulo: "+str(round(np.arctan(altura.val/longitud.val)*180/np.pi,1))+"°", 1, (0,0,0))
        screen.blit(angulo, (info.current_w-245, 240))
        
        ms = clock.tick(fps)
        
        
        if ini: fontcro = pygame.font.Font("Fonts/Digital-7.ttf", 35)
        if simulando:
            tiempo+=ms
            fontcro = pygame.font.Font("Fonts/Digital-7.ttf", 35)
            pulse = 0
            ps = 0
            c_image=crono_p
        if not simulando: c_image=crono_
        if not simulando and not ini and ps<=10:
            if pulse >= 10 and pulse <20:
                fontcro = pygame.font.Font("Fonts/Digital-7.ttf", 35)
                pulse+=1
            elif pulse <10:
                fontcro = pygame.font.Font("Fonts/Digital-7.ttf", 38)
                pulse+=1
            elif pulse == 20:
                pulse=0
                ps+=1
            
        
        if bola_.body.position.y <= r or (bola_.body.position.x >= longitud.val-r and longitud.val > info.current_w-2.5*r):
            simulando, ini = False, False
        
        c_image = pygame.transform.scale(c_image, (int(c_image.get_width()*0.2),int(c_image.get_height()*0.2)))
        c_rect = c_image.get_rect()
        c_rect.center = (info.current_w-250+c_image.get_width()//2, 345)
        screen.blit(c_image, (c_rect.x, c_rect.y))
        
        crono = fontcro.render(str(round(tiempo/1000,2)), 1, (57,255,20))
        # El tiempo de simulaciones idénticas difiere en el segundo decimal, no sé si dejarlo con 2 decimales o solo 1.
        screen.blit(font.render("Tiempo", 1, (0,0,0)), (info.current_w-225, 280))
        screen.blit(font.render("de caída:", 1, (0,0,0)), (info.current_w-230, 295))
        screen.blit(crono, (info.current_w-250+c_image.get_width()//4, 335))
            
        
        if (bola_._id in space._shapes) or not t: draw_bola(bola_,r,tipo)
        draw_plano(plano_)
        space.step(1/fps)
        pygame.display.update()
        #print(ms)
    return False

#main()
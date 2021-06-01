import pygame, pymunk, numpy as np

def main():

    pygame.init()
    screen,running = pygame.display.set_mode((0,0),pygame.FULLSCREEN),True
    pygame.display.set_caption("hm")
    #ic = pygame.image.load("Imagenes/1.png")
    #pygame.display.set_icon(ic)
    pygame.display.flip()
    info = pygame.display.Info()
    
    
    class Slider():
        def __init__(self, name, val, max, min, pos):
            self.val = val
            self.max = max
            self.min = min
            self.xpos = info.current_w-120
            self.ypos = pos
            self.surf = pygame.surface.Surface((100, 50))
            self.hit = False
            
            self.txt_surf = font.render(name, 1, (0,0,0))
            self.txt_rect = self.txt_surf.get_rect(center=(50, 15))
    
            self.surf.fill((255, 204, 153))
            pygame.draw.rect(self.surf, (200, 200, 200), [0, 0, 100, 50], 3)
            pygame.draw.rect(self.surf, (204, 204, 179), [10, 10, 80, 14], 0)
            pygame.draw.rect(self.surf, (255,255,255), [10, 30, 80, 5], 0)
            
            self.surf.blit(self.txt_surf, self.txt_rect)
    
            self.button_surf = pygame.surface.Surface((20, 20))
            self.button_surf.fill((1, 1, 1))
            self.button_surf.set_colorkey((1, 1, 1))
            pygame.draw.circle(self.button_surf, (0,0,0), (10, 10), 6, 0)
            pygame.draw.circle(self.button_surf, (200, 100, 50), (10, 10), 4, 0)
            
        def draw(self):
            surf = self.surf.copy()
    
            pos = (10+int((self.val-self.min)/(self.max-self.min)*80), 33)
            self.button_rect = self.button_surf.get_rect(center=pos)
            surf.blit(self.button_surf, self.button_rect)
            self.button_rect.move_ip(self.xpos, self.ypos)
    
            screen.blit(surf, (self.xpos, self.ypos))
    
        def move(self):
            self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.max - self.min) + self.min
            if self.val < self.min:
                self.val = self.min
            if self.val > self.max:
                self.val = self.max
    
    class Boton():
        def __init__(self, txt, location, action, bg=(255,255,255), fg=(0,0,0), size=(80, 30), font_name="Verdana", font_size=14):
            self.color = bg
            self.bg = bg
            self.fg = fg
            self.size = size
    
            self.font = pygame.font.SysFont(font_name, font_size, True)
            self.txt = txt
            self.txt_surf = self.font.render(self.txt, 1, self.fg)
            self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])
    
            self.surface = pygame.surface.Surface(size)
            self.rect = self.surface.get_rect(center=location)
    
            self.call_back_ = action
    
        def draw(self):
            self.mouseover()
    
            self.surface.fill(self.bg)
            self.surface.blit(self.txt_surf, self.txt_rect)
            screen.blit(self.surface, self.rect)
    
        def mouseover(self):
            self.bg = self.color
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.bg = (100,100,100)
    
        def call_back(self):
            self.call_back_()
    
    
    def conv_coord(pos):
        return pos[0], info.current_h-pos[1]
    
    def bola(space,pos,r,m):
        body = pymunk.Body(m,200,body_type= pymunk.Body.DYNAMIC)
        body.position = pos
        shape = pymunk.Circle(body, r)
        #shape.elasticity = 1
        space.add(body,shape)
        return shape
    
    def draw_bola(bola,r):
        pos_x,pos_y = conv_coord(bola.body.position)
        pygame.draw.circle(screen, (255,255,255), (int(pos_x),int(pos_y)), r)
    
    def plano(space,pos_plano,w):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, pos_plano[0], pos_plano[1], w)
        #shape.elasticity = 1
        space.add(body,shape)
        return shape
        
    def draw_plano(plano):
        pygame.draw.line(screen, (255,255,255), conv_coord(pos_plano[0]), conv_coord(pos_plano[1]),5)
    
    def masa_radio(m):
        l = np.linspace(10,30,100)
        r = int(l[m-1])
        return r
    
    def nums(s,y,u):
            if s==masa: l=int(s.val)
            else: l=int(s.val)/100
            surf = pygame.surface.Surface((100, 50))
            txt_surf = font.render(str(l)+u, 1, (255,255,255))
            txt_rect = txt_surf.get_rect(center=(50, 15))
            surf.blit(txt_surf, txt_rect)
            screen.blit(surf, (info.current_w-210, y))
            
    def Boton_mouse():
        pos = pygame.mouse.get_pos()
        for b in bs:
            if b.rect.collidepoint(pos):
                b.call_back()
    
    def start_():
        if block._id in space._shapes: space.remove(block)
    
    def restart_():
        masa.hit = True
    
    font = pygame.font.SysFont("Verdana", 12, True)
    clock = pygame.time.Clock()
    space = pymunk.Space()
    space.gravity = (0,-981)
    fps = 50
    pos_plano = [(0,0),(info.current_w,0)]
    
    
    c = True
    aj = np.linspace(1.1,.67,info.current_h)
    block = plano(space,[(1,1),(1,2)],0)
    r = 30
    masa = Slider("Masa", 100, 100, 1, 20)
    altura = Slider("Altura", 0, info.current_h-60*0.85, 0, 80)
    longitud = Slider("Longitud", info.current_w, info.current_w, r*2, 140)
    slides = [masa,altura,longitud]
    
    
    start = Boton("Simular", (info.current_w-70,240), start_)
    restart = Boton("Reiniciar",(info.current_w-70,280), restart_)
    bs = [start,restart]
    
    bola_ = bola(space,(r,r),r,masa.val)
    plano_ = plano(space,pos_plano,2.5)
    pared = plano(space,[(info.current_w,0),(info.current_w,info.current_h)],0)
    suelo = plano(space,[(0,0),(info.current_w,0)],0)
    
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Boton_mouse()
                s_pos = pygame.mouse.get_pos()
                for s in slides:
                    if s.button_rect.collidepoint(s_pos):
                        s.hit,c = True,False
            elif event.type == pygame.MOUSEBUTTONUP:
                for s in slides:
                    s.hit,c = False,True
                    
        r = masa_radio(int(masa.val))
        
        
        screen.fill((0,0,0))
        for s in slides:
            if s.hit:
                space.remove(bola_,plano_)
                if (block._id in space._shapes): space.remove(block)
                if c == False: s.move()
                pos_plano = [(0,int(altura.val)),(int(longitud.val),0)]
                plano_ = plano(space,pos_plano,2.5)
                bola_ = bola(space,(r,int(altura.val)+r*aj[int(altura.val)]),r,masa.val)
                block = plano(space,[(r*2,int(altura.val)+r),(r*2,0)],0)
                
        nums(masa,20," kg")
        nums(altura,80," m")
        nums(longitud,140," m")
        
        for s in slides:
            s.draw()
        
        for b in bs:
            b.draw()
        
        ms = clock.tick(fps)
        draw_bola(bola_,r)
        draw_plano(plano_)
        space.step(1/fps)
        pygame.display.update()
        #print(ms)
    return False

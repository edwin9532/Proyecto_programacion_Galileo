import pygame, pymunk, numpy as np

pygame.init()
screen,running = pygame.display.set_mode((0,0),pygame.FULLSCREEN),True
pygame.display.set_caption("hm")
ic = pygame.image.load("Imagenes/1.png")
pygame.display.set_icon(ic)
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



def conv_coord(pos):
    return pos[0], info.current_h-pos[1]

def bola(space,pos,r,m):
    body = pymunk.Body(m,20,body_type= pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, r)
    space.add(body,shape)
    return shape

def draw_bola(bola,r):
    pos_x,pos_y = conv_coord(bola.body.position)
    pygame.draw.circle(screen, (255,255,255), (int(pos_x),int(pos_y)), r)

def plano(space,pos_plano,w):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, pos_plano[0], pos_plano[1], w)
    space.add(body,shape)
    return shape
    
def draw_plano(plano):
    pygame.draw.line(screen, (255,255,255), conv_coord(pos_plano[0]), conv_coord(pos_plano[1]),5)

def masa_radio(m):
    l = np.linspace(10,30,100)
    r = int(l[m-1])
    return r


font = pygame.font.SysFont("Verdana", 12, True)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,-392.4)
fps = 50
pos_plano = [(0,0),(info.current_w,0)]

r = 20
masa = Slider("Masa", r, 100, 1, 20)
altura = Slider("Altura", 0, info.current_h, 0, 80)
slides = [masa,altura]

bola_ = bola(space,(r,r),r,masa.val)
plano_ = plano(space,pos_plano,2.5)
pared = plano(space,[(info.current_w,0),(info.current_w,info.current_h)],0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            s_pos = pygame.mouse.get_pos()
            for s in slides:
                if s.button_rect.collidepoint(s_pos):
                    s.hit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for s in slides:
                s.hit = False
                
    r = masa_radio(int(masa.val))
    
    for s in slides:
        if s.hit:
            space.remove(bola_)
            space.remove(plano_)
            s.move()
            pos_plano = [(0,int(altura.val)),(info.current_w,0)]
            plano_ = plano(space,pos_plano,2.5)
            bola_ = bola(space,(r,int(altura.val)+r),r,masa.val)
            
    
    screen.fill((0,0,0))
    for s in slides:
        s.draw()
    
    clock.tick(fps)
    draw_bola(bola_,r)
    draw_plano(plano_)
    space.step(1/fps)
    pygame.display.update()

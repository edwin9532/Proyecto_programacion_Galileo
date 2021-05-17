import pygame, pymunk

pygame.init()
screen,running = pygame.display.set_mode((0,0),pygame.FULLSCREEN),True
pygame.display.set_caption("hm")
ic = pygame.image.load("Imagenes/1.png")
pygame.display.set_icon(ic)
pygame.display.flip()
info = pygame.display.Info()

def conv_coord(pos):
    return pos[0], info.current_h-pos[1]

def bola(space,pos):
    body = pymunk.Body(10,20,body_type= pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 10)
    space.add(body,shape)
    return shape

def draw_bola(bola):
    pos_x,pos_y = conv_coord(bola.body.position)
    pygame.draw.circle(screen, (255,255,255), (int(pos_x),int(pos_y)), 10)

def plano(space,pos_plano,w):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, pos_plano[0], pos_plano[1], w)
    space.add(body,shape)
    return shape
    
def draw_plano(plano):
    pygame.draw.line(screen, (255,255,255), conv_coord(pos_plano[0]), conv_coord(pos_plano[1]),5)
    
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,-200)
fps = 50
pos_plano = [(0,0),(info.current_w,0)]

bola_ = bola(space,(0,0))
plano_ = plano(space,pos_plano,2.5)
pared = plano(space,[(info.current_w,0),(info.current_w,info.current_h)],0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            space.remove(bola_)
            space.remove(plano_)
            mouse_pos = conv_coord(event.pos)
            pos_plano = [(0,mouse_pos[1]),(info.current_w,0)]
            plano_ = plano(space,pos_plano,2.5)
            bola_ = bola(space,(5,mouse_pos[1]+15))
            
    
    screen.fill((0,0,0))
    clock.tick(fps)
    draw_bola(bola_)
    draw_plano(plano_)
    space.step(1/fps)
    pygame.display.update()

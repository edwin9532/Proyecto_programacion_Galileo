import pygame, pymunk

pygame.init()
screen,running = pygame.display.set_mode((800,600)),True
pygame.display.set_caption("hm")
ic = pygame.image.load("Imagenes/1.png")
pygame.display.set_icon(ic)
pygame.display.flip()

def bola(space):
    body = pymunk.Body(10,20,body_type= pymunk.Body.DYNAMIC)
    body.position = (100,100)
    shape = pymunk.Circle(body, 10)
    space.add(body,shape)
    return shape

def draw_bola(bola):
    pos_x = int(bola.body.position.x)
    pos_y = int(bola.body.position.y)
    pygame.draw.circle(screen, (255,255,255), (pos_x,pos_y), 5)

clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,100)
fps = 50

bola = bola(space)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False
    screen.fill((0,0,0))
    clock.tick(fps)
    draw_bola(bola)
    space.step(1/fps)
    pygame.display.update()

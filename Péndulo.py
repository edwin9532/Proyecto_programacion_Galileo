import pygame, pymunk, numpy as np

pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,-900)
fps = 50



def conv_coord(pos):
    return int(pos[0]), int(600-pos[1])

class Ball():
    def __init__(self, x, y):
        self.body               = pymunk.Body()
        self.body.position      = x, y 
        self.shape              = pymunk.Circle(self.body,0)
        self.shape.density      = 1
        self.shape.elasticity   = 1
        space.add(self.body, self.shape)
    def draw(self):
        pygame.draw.circle(screen,(255, 0, 0), conv_coord(self.body.position),10)
      
class pendu():
    def __init__(self, body1, identifier = "body"):
        self.body1 = body1
        if identifier == "body":
            self.body1 = attachment
        elif identifier == "position":
            self.body1 =pymunk.Body(body_type = pymunk.Body.STATIC)
            self.body1.position = attachment
        joint = pymunk.PinJoint(self.body1) 
        space.add(joint)
    def draw(self):
        pos1 = conv_coord(self.body1.position)
        pygame.draw.line(screen, (0,0,0), pos1, 2)
            
      
        
def game():
    bola_1 = Ball(300,450)
    pendulo = pendu(bola_1.body, (300,350), "position")
    pendulo_1 = pendu(bola_1.body)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return
        screen.fill((250,250,250))
        bola_1.draw()
        pendulo.draw()
        pendulo_1.draw()
        pygame.display.update()
        clock.tick(FPS)
        space.estep(1/FPS)

game()
pygame.quit()
        

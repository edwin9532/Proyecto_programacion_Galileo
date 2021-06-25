import pygame

# imagen= botón normal, imagen_p= Botón cuando mouse encima, scale= Factor para ajustar el tamaño de la imagen

class Boton():
    def __init__(self, x, y, imagen, imagen_p, scale, txt, font_name="BebasNeue.otf",font_size=25):
        self.txt = txt
        self.font_name = font_name
        self.font_size = font_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size, False)
        self.scale = scale
        width = imagen.get_width()
        height = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen, (int(width * scale), int(height * scale)))
        self.imagen_p = pygame.transform.scale(imagen_p, (int(width * scale), int(height * scale)))
        self.rect = self.imagen.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            surface.blit(self.imagen_p, (self.rect.x, self.rect.y))
            self.font = pygame.font.SysFont(self.font_name, self.font_size+2, False)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:                
                self.clicked = True
                action = True
        else:
            surface.blit(self.imagen, (self.rect.x, self.rect.y))
            self.font = pygame.font.SysFont(self.font_name, self.font_size, False)

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        txt = self.font.render(self.txt, 1, (0,0,0))
        txt_rect = txt.get_rect(center=(self.rect.x+self.imagen.get_width() /2, self.rect.y+self.imagen.get_height()/2))
        surface.blit(txt, txt_rect)
        
        return action



import pygame

class Slider():
    def __init__(self, name, val, max, min, posy, posx, font, surface):
        self.surface = surface
        self.val = val
        self.max = max
        self.min = min
        self.xpos = posx
        self.ypos = posy
        self.surf = pygame.surface.Surface((100, 50))
        self.hit = False
        
        self.txt_surf = font.render(name, 1, (0,0,0))
        self.txt_rect = self.txt_surf.get_rect(center=(50, 17))

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

        self.surface.blit(surf, (self.xpos, self.ypos))

    def move(self):
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.max - self.min) + self.min
        if self.val < self.min:
            self.val = self.min
        if self.val > self.max:
            self.val = self.max
    

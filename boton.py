import pygame
import sys

pygame.init()
pantalla= pygame.display.set_mode((800,600))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 50)
SPACE=pygame.image.load("space.png")
SPACE=pygame.transform.scale(SPACE,(800,600))
button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (250, 100))


class Boton():
	def _init_(self, image, x_pos, y_pos, texto):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.texto = texto
		self.text = main_font.render(self.texto, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def entrada(self):
		pantalla.blit(self.image, self.rect)
		pantalla.blit(self.text, self.text_rect)

	def presionar(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("HOLA")

	def cambiar_color(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.texto, True, "red")
		else:
			self.text = main_font.render(self.texto, True, "white")

def main():
    boton = Boton(button_surface, 400, 300, "JUGAR")
    run=True
    while run:
    	for event in pygame.event.get():
           if event.type == pygame.QUIT:
                 run=False
           if event.type == pygame.MOUSEBUTTONDOWN:
                boton.presionar(pygame.mouse.get_pos())
    	pantalla.fill("white"),pantalla.blit(SPACE,(0,0))
    	boton.entrada()
    	boton.cambiar_color(pygame.mouse.get_pos())
    	pygame.display.update()  
    pygame.quit()
if __name__=="_main_": 
    main()
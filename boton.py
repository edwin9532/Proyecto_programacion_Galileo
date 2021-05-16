import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 50)


class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def presionar(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

	def cambio_color(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "blue")
def draw_windows():
    screen.fill("white")
    screen.blit(SPACE,(0,0))
    pygame.display.update()
    
def main():
    button=Button(button_surface, 400, 300, "JUGAR")
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                button.presionar(pygame.mouse.get_pos())
        
        button.update()
        draw_windows()
        button.cambio_color(pygame.mouse.get_pos())
    pygame.quit()
if __name__=="__mein__":
    main()
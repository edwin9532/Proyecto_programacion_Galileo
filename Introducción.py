import pygame



pygame.init()
#Crear textos y poder visualizarlos
pygame.font.init()

#Tamaño pantalla
screen,running = pygame.display.set_mode((0,0),pygame.FULLSCREEN),True
#Nombre y logo del juego
pygame.display.set_caption("hm")
ic = pygame.image.load("Imagenes/1.png")
pygame.display.set_icon(ic)
pygame.display.flip()
#info = pygame.display.Info()


#ejecutar el juego a 50 FPS
FPS = 50
clock = pygame.time.Clock(FPS)

a = pygame.font.SysFont('comicsans', 100)

#Esta función dbuja lo que quiero que se vea
def draw_window():
    #Fondo/escenario
    
    #Galileo
    
    #Dialogos
    dialogo1 = a.render("Narrador: Corre el siglo XVI. Despertaste en los recuerdos del maestro Galileo Galilei, y estoy aquí para ayudarte a entender qué está pasando. Estás aquí gracias a tu curiosidad. Y bueno, porque estás dormido en tu comedor mientras hacías la tarea de física y pensaste en ¿por qué los cuerpos caen?", 1, WHITE)
    screen.blit(dialogo1, (10,10))
    pygame.display.update()
    pygame.time.delay(5000)  #milisegundos
    
    
#Para escribir los dialogos, tipo de letra y tamaño
#def dialogos(text):
    #draw_text = a.render(text, 1, white)
    #screen.blit(draw_text, (400,400)
    #pygame.display.update()
    #pygame.time.delay(5000)  #milisegundos
    
    



#Para cerrar el programa
def main():
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    running = False
                    pygame.quit()
                
        if pygame.time.delay(10000):
            dialogos("Corre el siglo XVI. Despertaste en los recuerdos del maestro Galileo Galilei, y estoy aquí para ayudarte a entender qué está pasando. Estás aquí gracias a tu curiosidad. Y bueno, porque estás dormido en tu comedor mientras hacías la tarea de física y pensaste en ¿por qué los cuerpos caen?")          
        
        draw_window(dialogo1)

    main()

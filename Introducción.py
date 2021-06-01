import pygame



pygame.init()

pygame.mixer.init()
pantalla = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()


a = pygame.font.Font(None, 40)
dialogo1_0 = a.render("Narrador: Corre el siglo XVI. Despertaste en los recuerdos", 1, (255,255,255))  
dialogo1_1 = a.render("del maestro Galileo Galilei, y estoy aquí para ayudarte a", 1, (255,255,255))
dialogo1_2 = a.render("entender qué está pasando. Estás aquí gracias a tu curiosidad.", 1, (255,255,255)) 
dialogo1_3 = a.render("Y bueno, porque estás dormido en tu comedor mientras hacías", 1, (255,255,255))
dialogo1_4 = a.render("la tarea de física y pensaste en ¿por qué los cuerpos caen?", 1, (255,255,255))


    

# intento de desaparecer el dialogo transcurridos 30000 milisegundos
def dibujador_de_dialogos(text):
    dialogo1 = a.render("Narrador: Corre el siglo XVI. Despertaste en los recuerdos del maestro Galileo Galilei, y estoy aquí para ayudarte a entender qué está pasando. Estás aquí gracias a tu curiosidad. Y bueno, porque estás dormido en tu comedor mientras hacías la tarea de física y pensaste en ¿por qué los cuerpos caen?", 1, (255,255,255))
    pantalla.blit(dialogo1,(1,500))
    pygame.display.update()
    pygame.time.delay(30000)
                          

#Otra manera de escribir el codigo principal. Que me funciona y cierra bien :,v

def main():
    salir = False
    while salir!= True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                salir = True


        clock.tick(15)          
        pantalla.fill((0,0,0))
        pantalla.blit(dialogo1_0,(200,450))
        pantalla.blit(dialogo1_1,(200,480))
        pantalla.blit(dialogo1_2,(200,510))
        pantalla.blit(dialogo1_3,(200,540))
        pantalla.blit(dialogo1_4,(200,570))
        pygame.display.update()
    
    pygame.quit()
main()

import pygame

#Inicializar el motor de pygame

pygame.init()

screen= pygame.display.set_mode((400,400))

seguir=True

x=200
y=200

direccion="arriba"

while seguir:
    
    clock= pygame.time.Clock()
    clock.tick(120)
    screen.fill((255,255,255))
    
    #Revisar los eventos y mirar si oprimen el boton cerrar
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            seguir=False
            
    tecla=pygame.key.get_pressed()
    
    if tecla[pygame.K_UP]:
         y=y-1
         direccion="arriba"
         
    if tecla[pygame.K_DOWN]:
         y=y+1
         direccion="abajo"
    
    if tecla[pygame.K_RIGHT]:
         x=x+1
         direccion="derecha"
         
    if tecla[pygame.K_LEFT]:
         x=x-1
         direccion="izquierda"
            
    if tecla[pygame.K_UP]==False and tecla[pygame.K_DOWN]==False and tecla[pygame.K_RIGHT]==False and tecla[pygame.K_LEFT]==False:
        if direccion=="arriba": y-=1
        if direccion=="abajo": y+=1
        if direccion=="derecha": x+=1
        if direccion=="izquierda": x-=1
        
    pygame.draw.rect(screen,(0,0,255),(x,y,20,20))
    
    #Actualizar la ventana
    pygame.display.flip()
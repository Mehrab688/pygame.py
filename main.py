



import pygame

pygame.init()

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Add Image Example")

image = pygame.image.load("Grass_Block.png")



image = pygame.transform.scale(image,(400,400))

x,y = 200,150



running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  screen.fill((0,0,0))
  screen.blit(image,(x,y))
  
  
  
  pygame.display.update()
  
pygame.quit()











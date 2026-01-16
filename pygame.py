import pygame

pygame.init()

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Rectangle")


BLUE = (0,0,225)
rect = pygame.Rect(150,120,200,100)



running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  screen.fill((255,255,255))
  pygame.draw.rect(screen,BLUE,rect)
  
  
  
  
  pygame.display.update()
  
pygame.quit()



import pygame 

#calendar class


#calendar class init
pygame.init()
screen_resolution = (800,600)
game_display = pygame.display.set_mode(screen_resolution)
pygame.display.set_caption('calendar')
clock = pygame.time.Clock()
#

#calendar class update sceen
def update_screen():
  pygame.display.draw_line(game_display, (0,0,0),True,[(0,0),(screen_resolution)],1)
  pygame.display.update()
#

#logic loop
running = True
while running:
  for event in pygame.event.get()
  if event.type is pygame.QUIT:
    running = False
  #print event
  update_screen()
  clock.tick(60)
pygame.quit()

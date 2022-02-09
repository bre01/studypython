import pygame 
import sys 

def check_events(screen,tank):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            check_keydown_events(event,tank)
        if event.type==pygame.KEYUP:
            tank.moving_left=False
            tank.moving_right=False
            tank.moving_up=False 
            tank.moving_down=False 
            


def update_screen(settings,screen,tank):
    screen.fill(settings.bg_color)
    
    tank.image=pygame.transform.flip(tank.image,False,False)
    tank.blitme()
    pygame.display.flip()

def check_keydown_events(event,tank):
    if event.key==pygame.K_a:
        tank.direction=4
        tank.moving_left=True 
        tank.moving_right=False
        tank.moving_up=False 
        tank.moving_down=False 
    elif event.key==pygame.K_d:
        tank.direction=2
        tank.moving_left=False  
        tank.moving_right=True 
        tank.moving_up=False 
        tank.moving_down=False 
    elif event.key== pygame.K_w:
        tank.direction=1
        tank.moving_left=False 
        tank.moving_right=False
        tank.moving_up=True  
        tank.moving_down=False 
    elif event.key==pygame.K_s:
        tank.direction=3
        tank.moving_left=False 
        tank.moving_right=False
        tank.moving_up=False 
        tank.moving_down=True 
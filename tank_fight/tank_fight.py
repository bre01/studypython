import pygame 
from settings import Settings 
from function import check_events, update_screen
from tank import Tank 
def run_game():
    pygame.init()
    settings=Settings()
    
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption('Tank Fight')
    tank=Tank(settings,screen)
    while True: 
        tank.update()
        check_events(screen,tank)
        update_screen(settings,screen,tank)

run_game()

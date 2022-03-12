import pygame
from settings import Settings
import functions
import sys
from pygame.sprite import Group
from background import Background
from bullet import Bullet
from person import Person 
def run_game():
    pygame.init() 
    settings=Settings() 
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption('Mario')

    background=Background(settings,screen)
    person=Person(screen,settings)
    bullets=Group()
    
    while True:
        background.update()
        if settings.active:
            functions.generate_bullet(screen,settings,bullets)
        

        
        functions.check_events(screen,settings,person)
        
        functions.update_screen(screen,settings,background,bullets,person)
        
run_game()
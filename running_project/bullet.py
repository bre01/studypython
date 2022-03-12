import pygame
from  pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,screen,settings,pos):
        super(Bullet,self).__init__()
        self.screen=screen
        self.settings=settings
        self.image=pygame.image.load('bullet (1) (Custom) (1).bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.right=self.screen_rect.right
        self.rect.top=pos

    def update(self):
        
        self.rect.centerx-=3    
        
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
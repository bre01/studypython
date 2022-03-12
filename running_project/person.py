import pygame 
from pygame.sprite import Sprite 
class Person(Sprite):
    def __init__(self,screen,settings):
        super(Person,self).__init__()
        self.screen=screen
        self.settings=settings
        self.image=pygame.image.load('mario_normal (Custom) (2).bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.left=self.screen_rect.left+100
        self.rect.bottom=750
        self.onland=True
        self.jumping=False
        self.high=False
        self.moving_right=False
        self.moving_left=False
    def update(self):
        if self.moving_right:
            self.rect.centerx +=2
        if self.moving_left:
            self.rect.centerx -=2
        if self.jumping and not self.high:
            self.rect.centery -=3
            if self.rect.centery<=450:
                self.high=True
        if self.high:
            self.rect.centery+=3
            if self.rect.bottom>= 750:
                self.onland=True
                self.high=False
                self.jumping=False

    def jump(self):
        if self.onland:
            self.jumping=True
    def blitme(self):

        self.screen.blit(self.image,self.rect)
        

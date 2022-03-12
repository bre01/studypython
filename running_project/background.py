import pygame
class Background():
    def __init__(self,settings,screen):
        self.settings=settings
        self.screen=screen
        self.image=pygame.image.load('background2.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.left=self.screen_rect.left
        self.rect.bottom=self.screen_rect.bottom
    def update(self):
        if self.rect.centerx < self.screen_rect.left:
            self.rect.left=self.screen_rect.left

        self.rect.centerx-=2
    

    def painting(self):
        
            
        self.screen.blit(self.image,self.rect)
        

       
        
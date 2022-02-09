import pygame
class Tank():
    def __init__(self,settings,screen):
        self.settings=settings 
        self.screen =screen 
        self.direction=1 
        self.image = pygame.image.load(str(self.direction) + 'tank (Custom) (1).bmp')
        self.rect = self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom =self.screen_rect.bottom
        
        self.moving_right=False 
        self.moving_left=False 
        self.moving_up=False 
        self.moving_down=False 

    def update(self):
        if self.moving_down:
            self.rect.centery += self.settings.moving_speed
        elif self.moving_up:
            self.rect.centery -= self.settings.moving_speed
        elif self.moving_left:
            self.rect.centerx -= self.settings.moving_speed
        elif self.moving_right:
            self.rect.centerx += self.settings.moving_speed
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)

        


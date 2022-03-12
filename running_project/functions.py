from turtle import back
import pygame 
import sys
from random import randint 
from bullet import Bullet 
def update_screen(screen,settings,background,bullets,person):
    screen.fill(settings.bg_color)
    background.painting()
    person.update()
    if pygame.sprite.spritecollideany(person,bullets):
        settings.active=False
    for bullet in bullets:
        if bullet.rect.right<bullet.screen_rect.left:
            bullets.remove(bullet)
        else:
            bullet.blitme()
            bullet.update()
    person.blitme()
    pygame.display.flip()
    

def check_events(screen,settings,person):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if settings.active:
            if event.type==pygame.KEYDOWN:
                check_keydown_event(event,person)
            if event.type==pygame.KEYUP:
                check_keyup_event(event,person)
def check_keyup_event(event,person):
    if event.key==pygame.K_d:
        person.moving_right=False
    if event.key==pygame.K_a:
        person.moving_left=False

    

def check_keydown_event(event,person):
    if event.key==pygame.K_w:
        person.jump()
    if event.key==pygame.K_d:
        person.moving_right=True
    if event.key==pygame.K_a:
        person.moving_left=True


def generate_bullet(screen,settings,bullets):
    for bullet in bullets:
        
        if bullet.rect.centerx<bullet.screen_rect.centerx and len(bullets)<=1:
            
            pos=randint(600,750)
            new_bullet=Bullet(screen,settings,pos)
            bullets.add(new_bullet)
    if len(bullets)<=0:
        pos=randint(600,750)
        new_bullet=Bullet(screen,settings,pos)
        bullets.add(new_bullet)
    

    

import pygame 
from pygame.sprite import Group  
from settings import Settings 
from ship import Ship
import game_functions 

from game_stats import GameStats	
from button import Button 
from scoreboard import Scoreboard
def run_game():
	pygame.init() #初始化pygame 
	ai_settings=Settings()  #一个Settings实例
	screen=pygame.display.set_mode((ai_settings.screen_width, #生成一个屏幕surface
		ai_settings.screen_height))	 #一个元组 屏幕长宽    
	pygame.display.set_caption('Alien Invasion')  #设置游戏名字 
	play_button=Button(ai_settings,screen,'play')
	stats=GameStats(ai_settings)
	ship=Ship(ai_settings,screen) #传给Ship类 一个屏幕 生成ship实例
	bullets=Group() #生成bullets实例 
	scoreboard=Scoreboard(ai_settings,screen,stats)
	aliens=Group()
	game_functions.creat_fleet(ai_settings,screen,ship,aliens)
	while True:
		game_functions.check_events(ai_settings,screen,stats,play_button,ship,bullets,aliens,scoreboard) #不断的调用check_events方法 
		game_functions.hide_mouse(stats)
		if stats.game_active:
			
			ship.update()#调用ship的update方法 
			
			game_functions.update_bullets(ai_settings,screen,stats,scoreboard,ship,aliens,bullets)
			game_functions.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,scoreboard)
		
		
		game_functions.update_screen(ai_settings,screen,stats,scoreboard,ship,bullets,aliens,play_button) #调用更新屏幕（check_update)的方法 
	

run_game()


# 游戏过程 1.不断地运行 check_events,对ship和bullets的标志进行修改  
#		  2.不断的根据自身的标志 改变自身的位置 属性 等
#         3.根据ship和bullets的位置 刷新屏幕 

		 
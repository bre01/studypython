import pygame 
from pygame.sprite import Sprite 
class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		super().__init__()
		self.ai_settings=ai_settings #ai_settings属性是一个Settings实例 
		#load the image and get the around rectangle 
		self.screen = screen #screen属性是一个 
		self.image=pygame.image.load('images/ship.bmp')  #传给ship类 一个图片 
		self.rect=self.image.get_rect() #ship类的实例的矩形等于 那个图片取矩形 
		self.screen_rect=screen.get_rect() #ship类里面的屏幕矩形 等于屏幕取矩形 这个用于之后设置实例的位置
		# put ship at the bottom of screen 
		self.rect.centerx=self.screen_rect.centerx #设置实例的位置 实例的x中心等于获取的屏幕的x中心
		self.rect.bottom=self.screen_rect.bottom #设置实例的位置 实例的底部等于获取的屏幕的底部
		self.center=float(self.rect.centerx) #获取实例的x中心 ，并且转为浮点数 之后改变self.center，根据self.center改变实例位置
		self.moving_right=False #设置两个标志 
		self.moving_left=False
	def update(self):
		'''更新飞船位置  虽然最后会把self.center取成整数,但是self.center的变化是通过小数变化的,不会有太大的误差'''
		if self.moving_right and self.screen_rect.right> self.rect.right :
			self.center+= self.ai_settings.ship_speed_factor 
		elif self.moving_left and self.rect.left> self.screen_rect.left :
			self.center+= -(self.ai_settings.ship_speed_factor )
		self.rect.centerx=self.center #根据self.center改变实例位置


	def blitme(self):

		self.screen.blit(self.image,self.rect) #将得到的屏幕 显示实例  两个参数 一个图像 一个位置 
	def center_ship(self):
		self.center=self.screen_rect.centerx 
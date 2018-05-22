import pygame
import random

enemy1 = pygame.image.load('Enemy1.png')

def CortarImagen (image, x, y, eX, eY):
	info=image.get_rect()
	an_image = info[2]	
	al_image = info[3]
	an_corte = int(an_image/eX) 
	al_corte = int(al_image/eY)
	cuadro = image.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
	return cuadro


class Enemy(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.cut = CortarImagen(enemy1, 6, 1, 7, 4)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = px
		self.rect.y = py
		self.vel_x = 0
		self.vel_y = 0
		self.disp = False
		self.health = 500
		self.sangre = 0
		self.dparada = 1000
		self.disparar = False
		self.parar = False
		self.tespera = random.randrange(100, 1000)
		self.tdisparo = random.randrange(10, 1000)
		self.r = random.randrange(1,3)

	def update(self):
		self.image = self.cut
		if(not self.parar):
			if self.tdisparo >0:
				self.vel_x = -10
				self.tdisparo -=1
				self.rect.x += self.vel_x
				self.tespera = random.randrange(100, 1000) 
			else:
				if(self.tespera>=0):
					self.disparar = True
					self.tdisparo = random.randrange(100, 1000)
				self.vel_x = 0
				self.tespera -= 1
		else:
			self.vel_x = 0

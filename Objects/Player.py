import pygame
import random

luke1 = pygame.image.load('Luke.png')


def CortarImagen (image, x, y, eX, eY):
	info=image.get_rect()
	an_image = info[2]	
	al_image = info[3]
	an_corte = int(an_image/eX) 
	al_corte = int(al_image/eY)
	cuadro = image.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
	return cuadro
class Player(pygame.sprite.Sprite):
	def __init__(self, px, py):
		pygame.sprite.Sprite.__init__(self)
		self.health = 800
		self.cut = CortarImagen(luke1, 0, 0, 8, 3)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = px
		self.rect.y = py
		self.vel_x = 0
		self.vel_y = 0
		self.limitx = False
		self.limitxx = False
		self.simr = False
		self.siml = False
		self.cerca = False
		self.posy = 0
		self.posx = 0
		self.disp = False
		self.vel_n = self.vel_x
		self.vel_m = self.vel_y
	def update(self):
		self.disp = False
		self.rect.y += self.vel_m
		self.rect.x += self.vel_n
		self.image = self.cut

		# ____________Limites para el Fondo_______________
		if(self.rect.x >= 430):
			self.rect.x = 429
			self.vel_n = 0
			self.limitx = True
			self.posx -= self.vel_x
		else:
			self.vel_n = self.vel_x
			self.limitx = False
		if(self.rect.x <= 10):
			self.rect.x = 11
			self.vel_n = 0
			self.limitxx = True
			self.posx -= self.vel_x
		else:
			self.vel_n = self.vel_x
			self.limitxx = False
		# ____________Limites para el Fondo_______________
		if(self.rect.y<=80):
			self.rect.y = 79
			self.vel_m = 0
		else:
			self.vel_m = self.vel_y
		if(self.rect.y >=360):
			self.rect.y = 359
			self.vel_m = 0
		else:
			self.vel_m = self.vel_y

import pygame
import random


vader1 = pygame.image.load('vader1.png')

f0 = 0

def CortarImagen (image, x, y, eX, eY):
	info=image.get_rect()
	an_image = info[2]	
	al_image = info[3]
	an_corte = int(an_image/eX) 
	al_corte = int(al_image/eY)
	cuadro = image.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
	return cuadro


class Boss(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.cut = CortarImagen(vader1, 4, 0, 9, 4)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = px
		self.rect.y = py
		self.vel_x = 0
		self.vel_y = 0
		self.health = 2000
		self.sangre = 0
		self.disparar = False
		self.diri = False
		self.dird = False
	def update(self):
		self.image = self.cut
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y
		self.disparar = False
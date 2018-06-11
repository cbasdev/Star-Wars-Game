import pygame
import random

#Image nave
nave1 = pygame.image.load('nave.png')


def CortarImagen (image, x, y, eX, eY):
	info=image.get_rect()
	an_image = info[2]	
	al_image = info[3]
	an_corte = int(an_image/eX) 
	al_corte = int(al_image/eY)
	cuadro = image.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
	return cuadro


class Nave(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.cut = CortarImagen(nave1, 0, 0, 1, 1)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = px
		self.rect.y = py
		self.vel_x = -10
		self.vel_y = 0
		self.tiempo = 20
		self.disparar = False
		self.diri = False
	def update(self):
		self.image = self.cut
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y
		if(self.tiempo >0):
			self.tiempo -= 1
			self.disparar = False
		else:
			self.disparar = True
			self.tiempo = 20

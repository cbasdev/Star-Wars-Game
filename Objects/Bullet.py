import pygame
import random

def CortarImagen (image, x, y, eX, eY):
	info=image.get_rect()
	an_image = info[2]	
	al_image = info[3]
	an_corte = int(an_image/eX) 
	al_corte = int(al_image/eY)
	cuadro = image.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
	return cuadro

class Bullet (pygame.sprite.Sprite):
	def __init__(self, px, py):
		self.l = 25
		self.a = 5
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([self.l,self.a])
		self.image.fill([255,0,0])
		self.rect = self.image.get_rect()
		self.rect.x= px
		self.rect.y = py
		self.vel_x = -20
		self.vel_y = 0

	def update(self):
		self.image = pygame.Surface([self.l,self.a])
		self.image.fill([255,0,0])
		
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y

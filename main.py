# BY: SebasttianVelez
import pygame
import random
from Objects.Player import *  
from Objects.Enemy import *
from Objects.Bullet import *
from Objects.Life import *
from Objects.Boss import *
from Objects.Nave import *

#Variables globales
ancho = 700
alto = 500
close = False
fondo1 = pygame.image.load('Mapa1.png')
reloj = pygame.time.Clock()
luke1 = pygame.image.load('Luke.png')
life1 = pygame.image.load('life1.png')
life2 = pygame.image.load('life2.png')
nave1 = pygame.image.load('nave.png') 
enemy1 = pygame.image.load('Enemy1.png')
vader1 = pygame.image.load('vader1.png')
vader2 = pygame.image.load('vader2.png')
vader3 = pygame.image.load('vader3.png')



#_____________________________________
i0 = 0
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
j0 = 0
j1 = 0
j2 = 0
j3 = 0
j4 = 0
j5 = 0
k1 = 4
k2 = 0
d1 = 0
d2 = 0
d3 = 0
f0 = 0
f1 = 3
f2 = 0
f3 = 3
f4 = 0
f5 = 0
np = -1700
pg = True
pg2 = True
pg3 = True
ACTboss = False
#_____________________________________
espera1 = True
#_____________________________________
pospx = 0
pospy = 0
disp = False
disp2 = False
dir1 = True
dir2 = True
V = False
nene = 3
activate = False
l1c = 800
l2c = 1500
ln = 1500
t = 20
def CortarImagen (image, x, y, eX, eY):
	info=image.get_rect()
	an_image = info[2]	
	al_image = info[3]
	an_corte = int(an_image/eX) 
	al_corte = int(al_image/eY)
	cuadro = image.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
	return cuadro

print
#Inicializacion de Pygame
if __name__ == '__main__':
	#Definicion de Variables
	pygame.init()

	#Crear variables locales
	Pantalla = pygame.display.set_mode([ancho, alto])
	pygame.mixer.init()
	sonido = pygame.mixer.Sound("Music/Across.wav")
	sonido2 = pygame.mixer.Sound("Music/Imperial.wav")

	pygame.font.init()
	path = "./fonts/FluoGums.ttf"
	size = 17
	fuente = pygame.font.Font(path,size)
	fuente2 = pygame.font.Font(path, 40)
	#Grupos
	todos = pygame.sprite.Group()
	Players = pygame.sprite.Group()
	Enemys = pygame.sprite.Group()
	Bullets = pygame.sprite.Group()
	Lifes = pygame.sprite.Group()
	Bosses = pygame.sprite.Group()
	Naves = pygame.sprite.Group()

	Luke2 = Player(21,150)
	Players.add(Luke2)
	todos.add(Luke2)

	Luke = Player(21, 300)
	Players.add(Luke)
	todos.add(Luke)
	#1850X 225Y


	time = 50
	Life1 = Life(20, 450)
	Lifes.add(Life1)
	todos.add(Life1)

	Life2 = Life(400, 450)
	Lifes.add(Life2)
	todos.add(Life2)

	Vader = Boss(2300, 225)
	Bosses.add(Vader)
	todos.add(Vader)



#Iniciar el juego
while not close:
	if(not ACTboss):
		sonido.play()
	else:
		sonido.stop()
		sonido2.play()

	#Gestion de Eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			close = True

		if event.type == pygame.KEYDOWN:
#___________________________TECLAS J2____________________________
			if event.key == pygame.K_RIGHT:
				Luke.vel_x = 10
				Luke.vel_y = 0
				dir1 = True
				i1 = 0

			elif event.key == pygame.K_LEFT:
				Luke.vel_x = -10
				Luke.vel_y = 0
				dir1 = False
				i2 = 0

			elif event.key == pygame.K_DOWN:
				Luke.vel_y = 10
				Luke.vel_x = 0
				i3 = 0

			elif event.key == pygame.K_UP:
				Luke.vel_y = -10
				Luke.vel_x = 0
				i4 = 0
			if event.key == pygame.K_l:
				disp = True
				Luke.disp = True
#_________________________Teclas J2_____________________________
			if event.key == pygame.K_d:
				Luke2.vel_x = 10
				Luke2.vel_y = 0
				dir2 = True	
				j1 = 0

			elif event.key == pygame.K_a:
				Luke2.vel_x = -10
				Luke2.vel_y = 0
				dir2 = False
				j2 = 0

			elif event.key == pygame.K_s:
				Luke2.vel_y = 10
				Luke2.vel_x = 0
				j3 = 0

			elif event.key == pygame.K_w:
				Luke2.vel_y = -10
				Luke2.vel_x = 0
				j4 = 0
			if event.key == pygame.K_g:
				disp2 = True
				Luke2.disp = True

#_____________________________________________________________________________
		if event.type == pygame.KEYUP:
			if (event.key == pygame.K_RIGHT)or(event.key == pygame.K_LEFT)or(event.key == pygame.K_UP)or(event.key == pygame.K_DOWN):
				Luke.vel_y = 0
				Luke.vel_x = 0
				i0 = 0
			if (event.key == pygame.K_s)or(event.key == pygame.K_w)or(event.key == pygame.K_a)or(event.key == pygame.K_d):
				Luke2.vel_y = 0
				Luke2.vel_x = 0
				i0 = 0				
#-------------------JUGADOR 1 DEZPLAZADO A LA DERECHA------------------		
	if Luke.vel_x==10:
		t = 20
		Luke.cut=CortarImagen(luke1,i1,0,6,6)
	
		if i1 >= 3:
			i1 = 0
		else:
			i1 += 1

#-------------------JUGADOR 1 DEZPLAZADO A LA IZQUIERDA------------------
	if Luke.vel_x==-10:
		t = 20
		Luke.cut=CortarImagen(luke1,i2,1,6,6)
		if i2 <= 0:
			i2 = 3
		else:
			i2 -=1

#-------------------JUGADOR 1 DEZPLAZADO A LA ABAJO------------------
	if Luke.vel_y==10:
		
		t = 20
		Luke.cut=CortarImagen(luke1,i3,2,6,6)
		if i3 >=3:
			i3 = 0
		else:
			i3 += 1
#-------------------JUGADOR 1 DEZPLAZADO A LA ARRIBA------------------
	if Luke.vel_y==-10:
		t = 20
		Luke.cut=CortarImagen(luke1,i4,3,6,6)
		if i4 >=3:
			i4 = 0
		else:
			i4 += 1
#-------------------JUGADOR 1 NO SE DEZPLAZA ------------------
	if (Luke.vel_x==0) and (Luke.vel_y==0) and (disp == False) and (not Luke.siml):
		if dir1:
			Luke.cut=CortarImagen(luke1,4,0,6,6)
		else:
			Luke.cut=CortarImagen(luke1,4,1,6,6)

#-------------------JUGADOR 1	 ACTIVA LASER ------------------
	if (disp):
		t = 20
		if dir1:
			Luke.cut=CortarImagen(luke1, i5, 4, 6, 6)
		else:
			Luke.cut=CortarImagen(luke1, i5, 5, 6, 6)
		if(i5>=2):
			i5 = 0
			disp= False	
		else:
			i5 +=1

		ls_cl7 = pygame.sprite.spritecollide(Luke, Enemys, False)

		for e in ls_cl7:
			#falta mejorar el limite superior de la espada
			if(Luke.rect.top>= e.rect.top - 20)and(Luke.rect.bottom >= e.rect.bottom + 20)and(e.rect.bottom > Luke.rect.top+100):
				#print "enem ", e.rect.bottom
				#print "luke ",Luke2.rect.top
				#print e.health
				if(e.health<= 0):
					todos.remove(e)
					Enemys.remove(e)
				else:
					e.sangre += 1
					e.health -= 50


		#for e in ls_cl5:
		#	Luke2.health -= 20
		#	print  Luke2.health
#________________________________________________________________________
#-------------------JUGADOR 2 DEZPLAZADO A LA DERECHA------------------		
	if Luke2.vel_x==10:
		t = 20
		Luke2.cut=CortarImagen(luke1,j1,0,6,6)
	
		if j1 >= 3:
			j1 = 0
		else:
			j1 += 1

#-------------------JUGADOR 2 DEZPLAZADO A LA IZQUIERDA------------------
	if Luke2.vel_x==-10:
		t = 20
		Luke2.cut=CortarImagen(luke1,j2,1,6,6)
		if j2 <= 0:
			j2 = 3
		else:
			j2 -=1

#-------------------JUGADOR 2 DEZPLAZADO A LA ABAJO------------------
	if Luke2.vel_y==10:
		
		t = 20
		Luke2.cut=CortarImagen(luke1,j3,2,6,6)
		if j3 >=3:
			j3 = 0
		else:
			j3 += 1
#-------------------JUGADOR 2 DEZPLAZADO A LA ARRIBA------------------
	if Luke2.vel_y==-10:
		t = 20
		Luke2.cut=CortarImagen(luke1,j4,3,6,6)
		if j4 >=3:
			j4 = 0
		else:
			j4 += 1
#-------------------JUGADOR 2 NO SE DEZPLAZA ------------------
	if (Luke2.vel_x==0) and (Luke2.vel_y==0) and (disp2 == False) and (not Luke2.siml):
		if dir2:
			Luke2.cut=CortarImagen(luke1,4,0,6,6)
		else:
			Luke2.cut=CortarImagen(luke1,4,1,6,6)

#-------------------JUGADOR 2	 ACTIVA LASER ------------------
	if (disp2):
		t = 20
		if dir2:
			Luke2.cut=CortarImagen(luke1, j5, 4, 6, 6)
		else:
			Luke2.cut=CortarImagen(luke1, j5, 5, 6, 6)
		if(j5>=2):
			j5 = 0
			disp2= False	
		else:
			j5 +=1		
		ls_cl6 = pygame.sprite.spritecollide(Luke2, Enemys, False)

		for e in ls_cl6:
			#falta mejorar el limite superior de la espada
			if(Luke2.rect.top>= e.rect.top - 20)and(Luke2.rect.bottom >= e.rect.bottom + 20)and(e.rect.bottom > Luke2.rect.top+100):
				#print "enem ", e.rect.bottom
				#print "luke ",Luke2.rect.top
				#print e.health
				if(e.health<= 0):
					todos.remove(e)
					Enemys.remove(e)
				else:
					e.sangre += 1
					e.health -= 50

#-------------------GENERAR ENEMIGOS CONTINUAMENTE--------------------
	#l1c = 400
	#l2c = 1500
	#ln = 1300 
	
	if(pospx<=-100)and(pg == True):
		Luke.simr = False
		Luke2.simr = False
		espera1 = False
		NumNaves = 1
		for i in range(NumNaves):
			jet = Nave(ln, -40)
			Naves.add(jet)
			todos.add(jet)
		
		Clones = nene
		for i in range(Clones):
		
			Clon = Enemy(300, 100)
			Clon.rect.x = random.randrange(l1c,l2c)
			Clon.rect.y = random.randrange(79, 359)
			Enemys.add(Clon)
			todos.add(Clon)
		pg = False

	if(len(Enemys)<=0):
		espera1 = True
	if(pospx<=-600)and(pg2 == True):
		pg = True
		pg2 = False
		l1c += 500
		l2c += 500
		ln += 500
		nene *= 2
	if(pospx<=-1100)and(pg3 == True):
		pg = True
		pg3 = False
		l1c += 500
		l2c += 500
		ln += 500
		nene += 4
	

#______________________Comportamiento Enemigo_________________________#
	
#-------------------Movimiento ENemigos ------------------
	for clon in Enemys:
		if (clon.vel_x==-10):
			clon.cut = CortarImagen(enemy1, k1, 1, 7, 4)
			if k1 <= 0:
				k1 = 3
			else:
				k1 -=1
#-------------------DIsparar ENemigos ------------------
	for clon in Enemys:
		if (clon.vel_x==0) and (not clon.parar):
			clon.cut = CortarImagen(enemy1, k2, 1, 7, 4)
			if k2 >=6:
				K2 = 5
			else:
				k2 += 1
			b = Bullet(clon.rect.x+20, clon.rect.y+55)
			Bullets.add(b)
			todos.add(b)
	for clon in Enemys:
		distancia = clon.rect.x - Luke.rect.x
		distancia2 = clon.rect.x - Luke2.rect.x
		if(clon.r == 1):
			clon.dparada = distancia
		else:
			clon.dparada = distancia2
		if (clon.dparada<=100): # distancia en donde paran los enemigos
			clon.vel_x = 0
			clon.parar = True


	for clon in Enemys:
		if (clon.parar and clon.vel_x ==0):
			clon.cut = CortarImagen(enemy1, 5, 1, 7, 4)
			if(time > 0):
				time -= 1
			else:
				b = Bullet(clon.rect.x+20, clon.rect.y+ 55)
				Bullets.add(b)
				todos.add(b)
				time = 50
	for clon in Enemys:
		if (clon.sangre>0):
			clon.cut = CortarImagen(enemy1, 5, 2, 7, 4)
			clon.sangre = 0
#____________________________________________________________________________________________NAVES

	for n in Naves:
		if(n.disparar == True):
			b = Bullet(n.rect.x+40, n.rect.y+90)
			b.l = 5
			b.a = 40
			b.vel_x = 0
			b.vel_y = 10
			Bullets.add(b)
			todos.add(b)

#____________________________________________________________________________________________VADER
# _____________________________________________________________________________________PELEA FINAL

	for L in Players:	
		if (pospx <= np):
			ACTboss = True
			#print "VADER: ", Vader.health
			activate = True
			#print "activar boss"
			#---boss prioriza matar al jugador 1
			#---jugador en la derecha
			if(Vader.rect.x > L.rect.x):
				Vader.dird = True
				Vader.diri = False
				if(Vader.rect.x - L.rect.x<= 80):
					Vader.vel_x = 0
					Vader.disparar = True
					L.cerca = True
				else:
					Vader.disparar = False
					L.cerca = False
					Vader.vel_x = -6
				if(L.disp)and(L.cerca):
					Vader.health -=5
			#---jugador en la izquierda
			else:
				Vader.dird = False
				Vader.diri = True
				if(L.rect.x - Vader.rect.x <= 50):
					Vader.vel_x = 0
					Vader.disparar = True
					L.cerca = True
				else:
					Vader.disparar = False
					L.cerca = False
					Vader.vel_x = 6
				if(L.disp)and(L.cerca):
					Vader.health -=20

			#jugador arriba
			if(Vader.rect.y > L.rect.y):
				if(Vader.rect.y- L.rect.y <= 30):
					Vader.vel_y = 0
					Vader.disparar = True
					L.cerca = True 
				else:
					Vader.disparar = False
					L.cerca = False
					Vader.vel_y = -6
				if(L.disp)and(L.cerca):
					Vader.health -=20
			else:
				if(L.rect.y - Vader.rect.y<= 30):
					Vader.vel_y = 0
					Vader.disparar = True
					L.cerca = True
				else:
					Vader.disparar = False
					L.cerca = False
					Vader.vel_y = 6
				if(L.disp)and(L.cerca):
					Vader.health -=20
		else:
			Vader.vel_x = 0
			Vader.disparar = False
			Vader.cut = CortarImagen(vader1, 4, 2, 9, 4)
			if(activate):
				np = Vader.rect.x - 1000
#___________________________________________________________________SPRITES VADER
	
	if(Vader.vel_x >0):
		Vader.cut = CortarImagen(vader1, f0, 1, 9,4)
		if(f0 >= 2):
			f0 = 0
		else:
			f0 += 1
	if(Vader.vel_x<0):
		Vader.cut = CortarImagen(vader1, f1, 0, 9, 4)
		if(f1 <=0):
			f1 = 3
		else:
			f1 -= 1
	if(Vader.vel_y>0):
		Vader.cut = CortarImagen(vader1, f2, 2, 9, 4)
		if(f2 >= 3):
			f2 = 0
		else:
			f2 += 1
	if(Vader.vel_y<0):
		Vader.cut = CortarImagen(vader1, f3, 3, 9, 4)
		if(f3 <= 0):
			f3 = 3
		else:
			f3 -= 1
	if(Vader.vel_x == 0)and(Vader.vel_y == 0)and(Vader.disparar == True):
		if(Vader.dird):
			Vader.cut = CortarImagen(vader2, f4, 0, 4, 1)
			if(f4 >= 3):
				f4 = 0
			else:
				f4 += 1
		else:
			Vader.cut = CortarImagen(vader3, f5, 0, 4, 1)
			if(f5 >= 3):
				f5 = 0
			else:
				f5 += 1
		if(Luke.health>0):
			Luke.health -= 2
		else:
			if(Luke2.health>0):
				Luke2.health-= 2


#____________________________________________________________________BARRAS DE SALUD

	if (Luke.health>0):
		if (Luke.health>500):
			Life1.cut = CortarImagen(life1, 0, 0, 1, 6)
		elif (Luke.health>400 and Luke.health<500):
			Life1.cut = CortarImagen(life1, 0, 1, 1, 6)
		elif (Luke.health>300 and Luke.health<400):
			Life1.cut = CortarImagen(life1, 0, 2, 1, 6)
		elif (Luke.health>200 and Luke.health<300):
			Life1.cut = CortarImagen(life1, 0, 3, 1, 6)
		elif (Luke.health>100 and Luke.health<200):
			Life1.cut = CortarImagen(life1, 0, 4, 1, 6)
		elif (Luke.health>=1 and Luke.health<100):
			Life1.cut = CortarImagen(life1, 0, 5, 1, 6)


	if (Luke2.health>0):
		if (Luke2.health>500):
			Life2.cut = CortarImagen(life2, 0, 0, 1, 6)
		elif (Luke2.health>400 and Luke2.health<500):
			Life2.cut = CortarImagen(life2, 0, 1, 1, 6)
		elif (Luke2.health>300 and Luke2.health<400):
			Life2.cut = CortarImagen(life2, 0, 2, 1, 6)
		elif (Luke2.health>200 and Luke2.health<300):
			Life2.cut = CortarImagen(life2, 0, 3, 1, 6)
		elif (Luke2.health>100 and Luke2.health<200):
			Life2.cut = CortarImagen(life2, 0, 4, 1, 6)
		elif (Luke2.health>=1 and Luke2.health<100):
			Life2.cut = CortarImagen(life2, 0, 5, 1, 6)





#------------------SIMULACIONES CON EL FONDO-----------------

#---------------JUgadores desplazandose unos a otros--------------------

	if(Luke2.simr):
		Luke2.cut=CortarImagen(luke1,j1,0,6,6)
		if j1 >= 3:
			j1 = 0
		else:
			j1 += 1

	if(Luke.simr):
		Luke.cut=CortarImagen(luke1,d1,0,6,6)
		if d1 >= 3:
			d1 = 0
		else:
			d1 += 1

	if(Luke2.siml):
		Luke2.cut=CortarImagen(luke1,d3,1,6,6)
		if d3 <= 0:
			d3 = 3
		else:
			d3 -=1
	if(Luke.siml):
		Luke.cut=CortarImagen(luke1,d2,1,6,6)
		if d2 <= 0:
			d2 = 3
		else:
			d2 -=1

#__________________________VIda de los jugadores_____________________"


#_______________________________________________________#


#________________________COLICIONES_______________________________

	ls_cl = pygame.sprite.spritecollide(Luke, Enemys, False)

	for e in ls_cl:
		e.disp = True


	ls_cl2 = pygame.sprite.spritecollide(Luke2, Enemys, False)

	for e in ls_cl:
		e.disp = True

	ls_cl3 = pygame.sprite.spritecollide(Luke, Bullets, True)

	for b in ls_cl3:
		if(Luke.siml):
			Luke.cut=CortarImagen(luke1,4,2,6,6)
		else:
			Luke.cut=CortarImagen(luke1,4,3,6,6)
		Luke.health -= 20 ##cambiar<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		todos.remove(b)
		Bullets.remove(b)

	ls_cl4 = pygame.sprite.spritecollide(Luke2, Bullets, True)

	for b in ls_cl4:
		if(Luke2.siml):
			Luke2.cut=CortarImagen(luke1,4,2,6,6)
		else:
			Luke2.cut=CortarImagen(luke1,4,3,6,6)
		Luke2.health -= 50 ##cambiar<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		todos.remove(b)
		Bullets.remove(b)
		
#____________________________________________________________________

	#Refresco de Pantalla
#________________________________________________________________________SI ALGUIEN MUERE
	if(Luke.health<=0):
		#Vader.vel_x = 0
		todos.remove(Luke)
		Players.remove(Luke)
		Lifes.remove(Life1)
		todos.remove (Life1)

	if(Luke2.health<=0):
		todos.remove(Luke2)
		Players.remove(Luke2)
		Lifes.remove(Life2)
		todos.remove (Life2)
		#Vader.vel_x = 10
	if(Luke.health<=0)and(Luke2.health<=0):
		Vader.vel_x = 0
		Vader.disparar = False
		Vader.cut = CortarImagen(vader1, 4, 2, 9, 4)

	if(Vader.health<=0):
		Vader.rect.x = 1000

		Vader.disparar = False
		Vader.health = 0
		todos.remove(Vader)
		Bosses.remove(Vader)

#______________________________________________________________SI la nave sobrepasa el limite

	for n in Naves:
		if (n.rect.x <= -100):
			Naves.remove(n)
			todos.remove(n)
#____________________________________________________________________

#
	#Limites con el fondo --------
	#print pospx
	if(pospx > 0):
		pospx -= 1
		Luke.vel_x = 0
		Luke2.vel_x = 0
	elif(pospx<-1810):
		pospx +=1
		Luke.vel_x = 0
		Luke2.vel_x = 0
	else:
		##limit jugador 1
		if(espera1):
			if(Luke.limitx):
				pospx -= Luke.vel_x
				Vader.rect.x -= Luke.vel_x
				Luke2.simr = True
				for e in Enemys:
					e.rect.x -= Luke.vel_x
			else:
				Luke2.simr = False
			if(Luke.limitxx):
				pospx -= Luke.vel_x
				Vader.rect.x -= Luke.vel_x

				Luke2.siml = True
				for e in Enemys:
					e.rect.x -= Luke.vel_x
			else:
				Luke2.siml = False
			#limit jugador 2
			if(Luke2.limitx):
				pospx -= Luke2.vel_x
				Vader.rect.x -= Luke2.vel_x

				Luke.simr = True
				for e in Enemys:
					e.rect.x -= Luke2.vel_x
			else:
				Luke.simr = False

			if(Luke2.limitxx):
				pospx -= Luke2.vel_x
				Vader.rect.x -= Luke2.vel_x

				Luke.siml = True
				for e in Enemys:
					e.rect.x -= Luke2.vel_x
			else:
				Luke.siml = False
	#-----------------------DIBUJAR EN PANTALLA TODO------------------------------------------------

	#print Luke.health
	#print Luke2.health		
	info=fondo1.get_rect()
	todos.update()
	Pantalla.fill([0,0,0])
	Pantalla.blit(fondo1, [pospx,pospy])
	texto = fuente.render("H1      H2", True, [0, 0, 0])
	
#____________________________________________________________________________GAME OVER -- si mueren los dos

	if(Luke.health<=0)and(Luke2.health<=0):
		over = fuente2.render("GAME OVER", True, [0, 0, 0])
		Pantalla.blit(over, [180,300])
#____________________________________________________________________________GAME WIN
	if(Vader.health<=0):
		ACTboss = False
		over2 = fuente2.render("YOU WIN", True, [0, 0, 0])
		Pantalla.blit(over2, [180,300])

#_______________________________________________________________________________________
	Pantalla.blit(texto, [290,459])
	todos.draw(Pantalla)
	pygame.display.flip()
	reloj.tick(t)

	#-------------------------------------------------------------------------------------

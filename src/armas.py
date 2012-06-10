#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       armas.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

import sys
from mechsSBT import *
from mapaSBT import *
from defmechSBT import *
from configSBT import *
from iniSBT import *
from utils import *

#~ import DefMech
from math import *
import os

class Armas:
	def __init__ (self, playerN):
		# Número del jugador automático
		self.playerN = playerN
		# Fichero mechsJx.sbt
		self.mechs = MechsSBT(self.playerN)
		self.mechs.leeFichero()
		# Fichero mapaJx.sbt
		self.mapa = MapaSBT(self.playerN)
		self.mapa.leeMapa()
		self.fichMapa = 'mapaJ'+str(playerN)+'.sbt'
		# Fichero iniciativaJx.sbt
		self.ini = Iniciativa(self.playerN)
		# Fichero de configuración
		self.conf = ConfigSBT(self.playerN)
		# Ficheros defMechJx-i.sbt
		self.dmech = []
		dm_fich = 'defmechJ'+str(playerN)+'-'
		for i in range(len(self.mechs.mechs)+1):
			sub_dm = dm_fich+str(i)+'.sbt'
			dm = DefMech()
			dm.readDefMech(sub_dm)
			self.dmech.append(dm)
		print "Dmechs = ",len(self.dmech)
		# Lista de enemigos en linea de vision
		self.enemigosVista = []
		# Mech del jugador
		self.jugador = self.mechs.jugador
		# Lista de armas usadas en el ataque con armas
		self.armasUsadas = []
		# Garrote cogido al final del ataque con armas
		self.garrote = False
		# Lista de enemigos
		self.enemigos = []
		for i in range(len(self.mechs.mechs)):
			if self.mechs.mechs[i].nombre != self.playerN and self.mechs.mechs[i].operativo:
				self.enemigos.append(self.mechs.mechs[i])
	
	def physicalAttack(self):
		f = "accionJ" + str(self.playerN)+".sbt"
		f = open(f, "w")
		choiseEnemy = None
		distance = 0
		enemy = None
		print "Realizamos ataque fisico"
		#Creamos una lista de enemigos atacables
		for i in range(len(self.enemigos))  :
			attack = self.visionLine(self.enemigos[i])
			if attack == True :
				self.enemigosVista.append(self.enemigos[i])
		
		if len(self.enemigosVista) > 0 :
			choiseEnemy = int(self.enemyMoreNear())
			# Si son adyacentes
			if self.areAdjacent((int(self.jugador.hexagono[2:4]), int(self.jugador.hexagono[:2])), (int(self.enemigosVista[choiseEnemy].hexagono[2:4]), int(self.enemigosVista[choiseEnemy].hexagono[:2]))) == True :
				print "Adyacentes!!"
				if self.garrote:
					print "ataque con garrote"
					f.write("1\n")
					f.write("BIBD\n")
					f.write("3000\n")
					f.write(self.enemigosVista[choiseEnemy]+"\n")
					f.write("Mech\n")
				# Si no tenemos garrote pegamos golpes
				else :
					print "Ataque con extremidades"
					# Debemos estimar que ataques se realizaron en el turno de ataqueArmas para saber que extremidad se puede usar
					enemy = self.enemigosVista[choiseEnemy]
					
					# Comprobamos qué armas se pueden usar contra el enemigo elegido
					choiseWeapons = self.choiseWeapons(enemy)
					# Eleccion temperatura
					temp = self.choiseTemperature(self.enemigosVista[choiseEnemy])
					# Eleccion definitiva de las armas a lanzar
					self.armasUsadas = self.shootWeapons(enemy, temp, choiseWeapons)
					
					# Si no tenemos armas.
					if len(self.armasUsadas) <= 0:
						if not enemy.suelo:
							# Realizamos un combo.
							f.write("3\n")
							f.write("BI\n")
							f.write("1000\n")
							f.write(enemy.hexagono)
							f.write("Mech\n")
							
							f.write("BD\n")
							f.write("1000\n")
							f.write(enemy.hexagono)
							f.write("Mech\n")
						else:
							f.write("1\n")
						
						f.write("PD\n")
						f.write("2000\n")
						f.write(enemy.hexagono)
						f.write("Mech\n")
					else:
						BI = False
						PI = False
						BD = False
						PD = False
						used = 0
						for i in range(len(self.armasUsadas)):
							# Localizacion del arma
							itemLocation = self.armasUsadas[i].getItemLocation()
							if itemLocation == 0 :
								BI = True
							elif itemLocation == 2:
								PI = True
							elif itemLocation == 3:
								PD = True
							elif itemLocation == 5:
								BD = True
							
							# No se pueden dar dos patadas en el mismo turno (pegaremos con la pierna derecha)
							if PI == False and PD == False :
								PD = True
							# Numero de extremidades que se usaran para el ataque
							if BI == False :
								used += 1
							if PI == False :
								used += 1
							if BD == False :
								used += 1
							if PD == False :
								used += 1
							f.write(str(used) + "\n")
							print "usos",used
							if not enemy.suelo:
								if BI == False :
									print "ATTT"
									f.write("BI\n")
									f.write("1000\n")
									f.write(enemy.hexagono)
									f.write("Mech\n")
								
								if BD == False :
									print "ATTT"
									f.write("BD\n")
									f.write("1000\n")
									f.write(enemy.hexagono)
									f.write("Mech\n")
							
							if PI == False :
								print "ATTT"
								f.write("PI\n")
								f.write("2000\n")
								f.write(enemy.hexagono)                               
								f.write("Mech\n")
							
							if PD == False :
								print "ATTT"
								f.write("PD\n")
								f.write("2000\n")
								f.write(enemy.hexagono)
								f.write("Mech\n")
				print "Hecho"
			# No se ataca
			else:
				f.write("0\n")
		# Nno se ataca
		else:
			f.write("0\n")
		f.close()
		
	
	def weaponsAttack(self):
		attack = False
		choiseEnemy = None
		distance = None
		finalChoise = None
		choiseWeapons = None
		temp = 0
		f = "accionJ" + str(self.playerN)+".sbt"
		print "Fichero creado"
		print " Hay garrote? ",self.mapa.mapa[int(self.jugador.hexagono[2:])][int(self.jugador.hexagono[:2])].getGarrote()
		# Creamos una lista de enemigos atacables
		for i in range(len(self.enemigos)):
			attack = self.visionLine(self.enemigos[i])
			if attack == True :
				self.enemigosVista.append(self.enemigos[i])
		print "Enemigos a la vista ",len(self.enemigosVista)
		# ¿Tenemos enemigos a la vista?
		if len(self.enemigosVista) > 0 :
			# Seleccionamos el enemigo disponible más cercano
			choiseEnemy = self.enemyMoreNear()
			print "Objetivo seleccionado = ",choiseEnemy
			# Comprobamos qué armas nos convienen
			choiseWeapons = self.choiseWeapons(self.enemigosVista[choiseEnemy])
			print "Armas: ",choiseWeapons
			# Eleccion temperatura
			temp = self.choiseTemperature(self.enemigosVista[choiseEnemy])
			print "Temperatura ",temp
			# Escogemos las armas a disparar
			self.armasUsadas = self.shootWeapons(self.enemigosVista[choiseEnemy], temp, choiseWeapons)
			print "Vamos a atacar"
			# Escribimos el ataque que vamos a realizar en el fichero de AccionJ
			self.writeWeaponsAttack(self.armasUsadas, self.enemigosVista[choiseEnemy], f)
			print "Ataque realizado"
		# Si no se puede atacar lo escribimos en el fichero de AccionJ
		else :
			print "No atacamos"
			self.writeNoAttack(f)
			
	
	def choiseTemperature(self, Enemy):
		tempPlayer = self.jugador.temperatura
		if tempPlayer < 10:
			temp = 12
		elif (15 > tempPlayer >= 10):
			temp = 9
		elif (20 > tempPlayer >= 15):
			temp = 6
		elif (26 > tempPlayer >= 20):
			temp = 4
		elif (tempPlayer >= 26):
			temp = 2
		
		#~ if Enemy.getWounds() <= 40 : WeakEnemy = True
		WeakEnemy = True
		print self.jugador.heridas
		if self.jugador.heridas <= 40 : WeakPlayer = True
		
		if WeakPlayer and WeakEnemy : temp = temp * 1.5
		if WeakPlayer and (not WeakEnemy) : temp = temp * 1.25
		if (not WeakPlayer) and WeakEnemy : temp = temp * 1.25
		
		return temp
	
	def writeWeaponsAttack(self, finalWeapons, Enemy, f):
		# Si no tenemos armas, No atacamos
		if len(finalWeapons) == 0:
			self.writeNoAttack(f)
		else :
			fich = open (f, "w")
			# No cogemos el garrote porque vamos a atacar.
			fich.write("False\n")
			# Hexagono objetivo
			fich.write(Enemy.hexagono[:4]+"\n")
			# Número de armas a disparar
			fich.write(str(len(finalWeapons))+"\n")
			
			numComponents = self.dmech[self.playerN].mech.getEquippedComponentsNumber() 
			numActuators = self.dmech[self.playerN].mech.getActuatorsNumber()
			
			for i in range(len(finalWeapons)):
				# Localizacion del arma
				itemLocation = finalWeapons[i].getItemLocation()
				if itemLocation == 0 :
					fich.write("BI\n")
				elif itemLocation == 1:
					fich.write("TI\n")
				elif itemLocation == 2:
					fich.write("PI\n")
				elif itemLocation == 3:
					fich.write("PD\n")
				elif itemLocation == 4:
					fich.write("TD\n")
				elif itemLocation == 5:
					fich.write("BD\n")
				elif itemLocation == 6:
					fich.write("TC\n")
				elif itemLocation == 7:
					fich.write("CA\n")
				
				# Número de slot donde está equipada el arma
				loca = self.dmech[self.playerN].mech.location[itemLocation]
				encontrado = False
				j = 0
				while j < loca.getSlotNumber() and not(encontrado):
					if loca.slot[j].getCode() == finalWeapons[i].getCode():
						encontrado = True
						fich.write(str(j)+"\n")
					j += 1
				
				# Disparo a doble cadencia -> siempre false, no es buena estrategia
				fich.write("False\n")
				
				# Si el arma es de tipo energía
				if finalWeapons[i].getWeaponType()[0:5] == "Energ":
					fich.write("-1\n")
					fich.write("-1\n")
				# Si no, buscamos donde esta la munición
				else:
					k = 0
					encontrado1 = False
					while k < numComponents and not(encontrado1):
						if self.dmech[self.playerN].mech.component[k].getWeaponCode() == finalWeapons[i].getCode():
							ammunitionCode = self.dmech[self.playerN].mech.component[k].getCode()
							encontrado1 = True
							h = 0
							encontrado2 = False
							while (h < numComponents) and (not encontrado2):
								if self.dmech[self.playerN].mech.component[h].getCode() == ammunitionCode:
									encontrado2 = True
									itemLocation = self.dmech[self.playerN].mech.component[h].getItemLocation()
									if itemLocation == 0 :
										fich.write("BI\n")
									elif itemLocation == 1:
										fich.write("TI\n")
									elif itemLocation == 2:
										fich.write("PI\n")
									elif itemLocation == 3:
										fich.write("PD\n") 
									elif itemLocation == 4:
										fich.write("TD\n")
									elif itemLocation == 5:
										fich.write("BD\n")
									elif itemLocation == 6:
										fich.write("TC\n")
									elif itemLocation == 7:
										fich.write("CAB\n")
									# Número de slot donde está la munición
									loca = self.dmech[self.playerN].mech.location[itemLocation]
									encontrado3 = False
									j = 0
									while (j < loca.getSlotNumber()) and (not encontrado3):
										if loca.slot[j].getCode() == ammunitionCode :
											encontrado3 = True
											fich.write(str(j)+"\n")
										j += 1
								else:
									h += 1
						k += 1
				# Hexágono objetivo del arma
				fich.write(Enemy.hexagono[:4]+"\n")
				fich.write("Mech\n")
			fich.close()
	
	def shootWeapons(self, Enemy, temp, choiseWeapons) :
		cumulativeTemp=0
		#ordenamos las armas lanzables por calidad
		for i in range(len(choiseWeapons)):        
			"""Ordena la lista por el metodo burbuja mejorado y 
			 ademas sale del ciclo de pasadas, en cuanto detecta 
			 que al final de una pasada no se realizaron 
			 intercambios."""
			intercambios=1 
			pasada=1 
			while pasada<len(choiseWeapons) and intercambios==1 : 
				intercambios=0 
				for i in range(len(choiseWeapons)-pasada):  
					if (choiseWeapons[i].getHarm()/choiseWeapons[i].getHeat()) > (choiseWeapons[i+1].getHarm()/choiseWeapons[i+1].getHeat()):
						choiseWeapons[i], choiseWeapons[i+1] = choiseWeapons[i+1], choiseWeapons[i]
						intercambios=1
					pasada += 1
		# ¿Cuántas armas podemos disparar sin sobrecalentar?
		finalWeapons = []
		numWeapons = 0
		for i in range(len(choiseWeapons)):
			if not(cumulativeTemp + choiseWeapons[i].getHeat() > temp):
				cumulativeTemp = cumulativeTemp + choiseWeapons[i].getHeat()
				finalWeapons.append(choiseWeapons[i])
		return finalWeapons
	
	def writeNoAttack(self,f):
		fich = open(f, "w")
		# Comprobamos si hay un garrote en la casilla del jugador
		if self.mapa.mapa[int(self.jugador.hexagono[2:])][int(self.jugador.hexagono[:2])].getGarrote() == True:
			fich.write("True\n")
			self.garrote = True
		# Si no hay garrote, no hacemos nada
		else:
			fich.write("False\n")
			fich.write("0000\n")
			fich.write("0\n")
		fich.close()
	
	def choiseWeapons(self, enemigo):
		disWeapons = []
		print len(self.dmech)," indice ",self.playerN
		for  i in range(self.dmech[self.playerN].mech.getEquippedComponentsNumber()):
			if self.dmech[self.playerN].mech.component[i].getType() == "ARMA":
				distance = self.euclideanDis(self.jugador.hexagono, enemigo.hexagono)
				if (distance <= self.dmech[self.playerN].mech.component[i].longDistance) and self.dmech[self.playerN].mech.component[i].operativeTeam :
					disWeapons.append(self.dmech[self.playerN].mech.component[i])
		return disWeapons
	
	def enemyMoreNear(self):
		minimo = 0
		distancia = self.dist2((int(self.jugador.hexagono[:2]),int(self.jugador.hexagono[2:])),(int(self.enemigosVista[0].hexagono[:2]),int(self.enemigosVista[0].hexagono[2:])))
		i = 1
		while i < len(self.enemigosVista):
			if (distancia > self.dist2((int(self.jugador.hexagono[:2]),int(self.jugador.hexagono[2:])),(int(self.enemigosVista[i].hexagono[:2]),int(self.enemigosVista[i].hexagono[2:])))):
				distancia = self.dist2((int(self.jugador.hexagono[:2]),int(self.jugador.hexagono[2:])),(int(self.enemigosVista[i].hexagono[:2]),int(self.enemigosVista[i].hexagono[2:])))
				minimo = i
			i+=1
		return int(minimo)
	
	def euclideanDis(self, c1, c2):
		return sqrt(((int(c2[:2])-int(c1[:2]))*(int(c2[:2])-int(c1[:2])))+((int(c2[2:])-int(c1[2:]))*(int(c2[2:])-int(c1[2:]))))
	
	def visionLine(self, enemy):
		if self.jugador.suelo == True:
			GroundPlayer = "1"
		else: 
			GroundPlayer = "0"
		
		if enemy.suelo == True:
			GroundEnemy = "1"
		else:
			GroundEnemy = "0"
		
		cellGoal = enemy.hexagono
		cellSource = self.jugador.hexagono
		
		# LDVyC.exe <nombre_fichero_mapa> <hexágono_origen> <suma_de_nivel_origen> <hexágono_destino> <suma_de_nivel_destino>
		execute = "LDVyC.exe "+self.fichMapa+" "+cellSource[:-1]+" "+GroundPlayer+" "+cellGoal[:-1]+" "+GroundEnemy
		
		# Ejecutar el programa de LineaVison
		os.system(execute)
		
		
		try:
			file = open("LDV.sbt", "r")
		except IOError:
			print "No existe el archivo LDV.sbt "
			raise SystemExit
		
		file.readline(); 
		hayLDV = str2bool(file.readline())
		file.close()
		return hayLDV
	
	def areAdjacent(self,c,c2):
		slist=[]
		for i in (-1,0,1):
			for j in (-1,0,1):
				if ((c[1]+1)%2 == 0): #columnas pares
					if (i == -1 and j == -1) or (i == 0 and j == 0) or (i == 1 and j == -1):
						continue
				else:
					if (i == 1 and j == 1) or (i == 0 and j == 0) or (j == 1 and i == -1):
							continue
				newFil = (c[0]) +j
				newCol = (c[1]) +i
				slist.append((newFil, newCol))
		return c2 in slist
	
	def dist2(self,c1,c2):
		Vx = abs(c2[0]-c1[0])
		Vy = abs(c2[1]-c1[1])
		if Vy%2 != 0:
			factor = 0
		elif c1[1] < c2[1]:
			factor = (c1[0]-1)%2
		else:
			factor = (c2[0]-1)%2
		return (Vx + max(0, Vy- (Vx/2) - factor))
		
	# Escribe en el fichero accionJx.sbt los pasos a realizar para 
	#	lograr llegar al objetivo del mech jugador.
	#~ def fileAccion(self):
		#~ # Apertura del fichero. Modo escritura
		#~ file = open("accionJ"+ str(self.playerN)+".sbt","w")
		#~ 
		#~ # Cerramos el fichero
		#~ file.close()

# COMPROBACIÓN
def main():
	acc = Armas(0)
	acc.weaponsAttack()
	print "correcto"
	return 0

if __name__ == '__main__':
	main()

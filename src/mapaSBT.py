#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       mapaSBT2.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

import celda
from math import fabs
from mechsSBT import *
from pathfinder import Pos
from utils import *


class MapaSBT(object):
	def __init__ (self, numJ = 0):
		self.__numJ = numJ
		self.__ancho = 0
		self.__alto = 0
		self.mapa = []
		self.nombre = 'mapaSBT'
		self.leeMapa()
		# Fichero mechsJx.sbt
		mechs = MechsSBT(self.__numJ)
		mechs.leeFichero()
		self.posiciones_mechs = []
		for m in mechs.mechs:
			self.posiciones_mechs.append(m.hexagono)
		
	def getAncho(self):
		return self.__ancho
	
	def setAncho(self, ancho):
		if ancho >= 0:
			self.__ancho = ancho
		else:
			print "Error: Ancho no válido."
			error("Ancho no válido.")
	ancho = property(getAncho, setAncho)
	
	def getAlto(self):
		return self.__alto
	
	def setAlto(self, alto):
		if alto >= 0:
			self.__alto = alto
		else:
			print "Error: Alto no válido."
			error("Alto no válido.")
	alto = property(getAlto, setAlto)
	
	def leeMapa(self):
		try:
			file = open('mapaJ'+str(self.__numJ)+'.sbt', 'r')
		except:
			print "Error: No se pudo abrir el fichero de mapa."
			error("No se pudo abrir el fichero de mapa.")
		
		# Buscamos la cabecera
		cabecera = file.readline()
		if string.find(cabecera,self.nombre) == -1:
			file.close()
			error("No es un fichero mapaSBT.")
		else:
			# Tamaño del mapa
			self.__alto = int(file.readline())
			self.__ancho = int(file.readline())
			
			self.mapa = [[0] * self.__ancho for i in range(self.__alto)]
			nCeldas = range(self.__ancho*self.__alto)
			nCaras = range (6)
			# Leemos las casillas del mapa
			for x in nCeldas:
				# Inicialización auxiliar de la celda y su posición
				cell = celda.Celda()
				col =(x%self.__alto)
				fil = (x//self.__alto)
				cell.x = col+1
				cell.y = fil+1
				# Lectura del fichero
				cell.nivel = int(file.readline())
				cell.terreno = int(file.readline())
				cell.objeto = int(file.readline())
				cell.fce = int(file.readline())
				cell.edificioDerrumbado = str2bool(file.readline())
				cell.fuego = str2bool(file.readline())
				cell.humo = str2bool(file.readline())
				cell.garrote = int(file.readline() )
				
				for y in nCaras:
					cell.rios.append(str2bool( file.readline()) )
				for y in nCaras:
					cell.carreteras.append(str2bool( file.readline()) )
				# Agregación al mapa
				self.mapa[col][fil] = cell
				cell = None
			# Cerramos el fichero.
			file.close()
	
	""" Calcula el coste de un movimiento desde una casilla c1 a otra c2
		adyacente.
		@param c1 Celda origen. Tipo Pos
		@param c2 Celda destino. Tipo Pos
		@param movType Tipo de movimiento (0-andar, 1-correr, 2-saltar)
		@return Coste total, cara
	"""
	def moveCost(self, c1, c2, movType = 0):
		p1 = c1.pos
		p2 = c2.pos
		lado = 0
		costeCara = 0
		costeCelda = 0
		lado = facing_side(p1, p2)
		# Si Andar o Correr
		if movType == 0 or movType == 1:
			# Coste total de orientarse a la cara correcta
			costeCara = min( (c1.face - lado)%6, (lado - c1.face)%6 )
			# Tipo de obstáculo.
			obj = self.mapa[p2[0]][p2[1]].objeto
			# Si hay agua
			if (self.mapa[p2[0]][p2[1]].terreno == 2):
				# Comprobamos el nivel
				if (self.mapa[p2[0]][p2[1]].nivel == -1):
					costeCelda = 2
				elif (self.mapa[p2[0]][p2[1]].nivel <= -2):
					costeCelda = 4
				else:
					costeCelda = 1
			# Si el tipo de obstáculo es:
			# Escombros, edificio pequeño o bosque ligero
			elif ((obj == 3) or (obj== 0) or (obj==1)):
				costeCelda = 2
			# Edificio mediano o bosque denso
			elif ((obj == 4) or (obj == 2)):
				costeCelda = 3
			# Edificio grande
			elif obj==5:
				costeCelda = 4
			# Edificio reforzado
			elif obj==6:
				costeCelda = 5
			# Si no hay obstáculo
			else:
				if abs(self.mapa[p1[0]][p1[1]].nivel - self.mapa[p2[0]][p2[1]].nivel) != 0:
					costeCelda = 2
				else:
					costeCelda = 1
		# Si Saltar, 1 PM
		elif movType==2:
			costeCelda = 1
		return (int(costeCara+costeCelda), lado)
	
	""" Calcula los sucesores de la coordenada c.
		@param c Coordenada de la que queremos conocer sus posibles sucesores.
		@param movType Tipo de movimiento a realizar.
		@param PM Posibles movimientos.
	"""
	def sucesores(self, c, movType = 0, PM = 15):
		slist = []
		
		# Obtenemos todas las casillas adyacentes
		for i in (-1,0,1):
			for j in (-1,0,1):
				# Columnas pares
				if ((c[1]+1)%2 == 0):
					if (i == -1 and j == -1) or (i == 0 and j == 0) or (i == 1 and j == -1):
						continue
				# Columnas impares
				else:
					if (i == 1 and j == 1) or (i == 0 and j == 0) or (j == 1 and i == -1):
						continue
				newFil = (c[0]) +j
				newCol = (c[1]) +i
				# Comprobamos que no nos salimos del mapa.
				if ((0 <= newFil < self.__alto) and (0 <= newCol < self.__ancho)):
					# Comprobamos que el movimiento entre celdas es correcto.
					if (self.checkCelda(c, (newFil,newCol), movType, PM)):
						slist.append((newFil, newCol))
		#~ print "sucesores de (",c[0],",",c[1],")"
		#~ print slist
		return slist
	
	
	""" Comprueba si se permite un movimiento de c1 a c2 con PM para mover.
		@param c1 Coordenada origen.
		@param c2 Coordenada destino.
		@param moveType Tipo de movimiento: 0-Andar, 1-Correr, 2-Saltar
	"""
	def checkCelda(self, c1, c2, moveType = 0, PM = 15):
		vale = False
		mech = False
		for m in self.posiciones_mechs:
			if (int(m[2:4])-1 == c2[0]) and (int(m[:2])-1 == c2[1]):
				mech = True
		
		# Si no hay un mech
		if not mech:
			# Si Correr o Andar y hay Fuego o un obstáculo o un mech
			#~ if ((self.mapa[c2[0]][c2[1]].fuego or (self.mapa[c2[0]][c2[1]].objeto != 1 and self.mapa[c2[0]][c2[1]].objeto != 255)) and (moveType == 1 or moveType == 0)):
			if ((self.mapa[c2[0]][c2[1]].objeto != 1 and self.mapa[c2[0]][c2[1]].objeto != 255)) and (moveType == 1 or moveType == 0):
				print "No puede!"
				return False
			# Si Correr y la profundidad del agua es < -1
			if (self.mapa[c1[0]][c1[1]].terreno == 2 and self.mapa[c1[0]][c1[1]].nivel < -1 and moveType == 1):
				return False
			diff = abs( self.mapa[c1[0]][c1[1]].nivel - self.mapa[c2[0]][c2[1]].nivel )
			# Si la diferencia de nivel <= 2 y Correr o Andar
			if ( diff <= 2 and (moveType == 0 or moveType == 1)):
				vale = True
			# Si Saltar y la diferencia de nivel <= PM
			elif ( diff <= PM and moveType == 2):
				vale = True
		else:
			vale = False
		return vale
	
	""" Heurística - Estimación del coste en distancia real de un
		desplazamiento en una malla hexagonal.
		@param c1 Pos
		@param c2 Pos
		@return coste
	"""
	def heuristic_to_goal(self,c1,c2):
		Vx = abs(c2.pos[0]-c1.pos[0])
		Vy = abs(c2.pos[1]-c1.pos[1])
		if Vy%2 != 0:
			factor = 0
		elif c1.pos[1] < c2.pos[1]: 
			factor = (c1.pos[0]-1)%2
		else:
			factor = (c2.pos[0]-1)%2
		return Vx + max(0, Vy- (Vx/2) - factor)

""" Obtiene el lado desde el que orientarnos de una casilla a otra.
	@param p1 Posición 1
	@param p2 Posición 2
	@return A qué cara orientarnos para mirar desde p1 a p2 en el mapa.
"""
def facing_side (p1, p2):
	y = - (p1[0] - p2[0])
	x = - (p1[1] - p2[1])
	face = 0 
	if ((p1[1]+1)%2 == 1): #columnas impares
		if (x == 0 and y == -1): # N
			face = 0
		elif (x == 1 and y == -1): # NE
			face = 1
		elif (x == 1 and y == 0): # SE
			face = 2
		elif (x == 0 and y == 1): # S
			face = 3
		elif (x == -1 and y == 0): # SO
			face = 4
		elif (x == -1 and y == -1): # NO
			face = 5
	else: #columnas pares
		if (x == 0 and y == -1): # N
			face = 0
		elif (x == 1 and y == 0): # NE
			face = 1
		elif (x == 1 and y == 1): # SE
			face = 2
		elif (x == 0 and y == 1): # S
			face = 3
		elif (x == -1 and y == 1): # SO
			face = 4
		elif (x == -1 and y == 0): # NO
			face = 5
	return face

""" Obtiene la celda adyacente a una posición y una cara.
	@param p Posición en el mapa
	@param face Cara de la que queremos obtener adyacentes.
	@return La casilla adyacente a la posición p y la cara face.
"""
def adjacent_cells(p, face):
	r1 = 0
	r0 = 0
	if ((p[1]+1)%2 == 1): #columnas impares
		if face == 0: # N
			r0 = p[0] -1
			r1 = p[1] 
		elif face == 1: # NE
			r0 = p[0] -1
			r1 = p[1] +1
		elif face == 2: # SE
			r0 = p[0] 
			r1 = p[1] +1
		elif face == 3: # S
			r0 = p[0] +1
			r1 = p[1] 
		elif face == 4: # SO
			r0 = p[0] 
			r1 = p[1] -1
		elif face == 5: # NO
			r0 = p[0] -1
			r1 = p[1] -1
	else: #columnas pares
		if face == 0: # N
			r0 = p[0] -1
			r1 = p[1] 
		elif face == 1: # NE
			r0 = p[0] 
			r1 = p[1] +1
		elif face == 2: # ES
			r0 = p[0] +1
			r1 = p[1] +1
		elif face == 3: # S
			r0 = p[0] +1
			r1 = p[1] 
		elif face == 4: # SO
			r0 = p[0] +1
			r1 = p[1] -1
		elif face == 5: # NO
			r0 = p[0] 
			r1 = p[1] -1
	return r0,r1

""" Comprueba si dos casillas son adyacentes.
	@param c Celda 1
	@param c2 Celda 2
	@return True Si son adyacentes, False en caso contrario
"""
def areAdjacent(c,c2):
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


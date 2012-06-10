#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       movimiento.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

import sys
from pathfinder import *
from mechsSBT import *
from mapaSBT import *
from configSBT import *
from iniSBT import *
from utils import *

# Diccionarios para el tipo de movimiento y los pasos.
mov = {0: 'Andar', 1: 'Correr', 2: 'Saltar', 3: 'Inmovil'}
step = {0: 'Adelante', 1: 'Atras', 2: 'Izquierda', 3: 'Derecha', 4: 'Levantarse', 5: 'Cuerpo a Tierra'}

class Movimiento:
	def __init__ (self, playerN):
		# Número del jugador automático
		self.playerN = playerN
		# Fichero mechsJx.sbt
		self.mechs = MechsSBT(self.playerN)
		self.mechs.leeFichero()
		# Fichero mapaJx.sbt
		self.board = MapaSBT(self.playerN)
		self.board.leeMapa()
		# Fichero iniciativaJx.sbt
		self.ini = Iniciativa(self.playerN)
		# Fichero de configuración
		self.conf = ConfigSBT(self.playerN)
		self.conf.leeFichero()
		
		self.movType = None
		self.nextCell = None
		self.nextFace = None
		self.masc = False
		self.stepNumber = None
		"""
		(stepType, times/face)
		 stepType: 1-adelante 2-atras 3-izquierda
		 4-derecha 5-levantarse 6-cuerpo a tierra
		"""
		self.stepCell = []
		
		self.path = None
		self.jugador = self.mechs.jugador
		self.jugadorCell = int(self.jugador.hexagono[2:4])-1,int(self.jugador.hexagono[0:2])-1
		self.jugadorLado = self.jugador.lado -1
		self.getUp = False
	
	""" Encuentra el jugador al que aproximarse.
		@return Número del mech enemigo, distancia del enemigo
	"""
	def setTarjet(self):
		t = 0
		distance = sys.maxint
		d = sys.maxint
		for m in self.mechs.mechs:
			if m.nombre != self.playerN and m.operativo:
				d = dist2((int(self.jugador.hexagono[0:2]),
					int(self.jugador.hexagono[2:4])),(int(m.hexagono[0:2]),
					int( m.hexagono[2:4])))
			if d < distance:
				t = m.nombre
				distance = d
		return t, distance
	
	""" Calcula el siguiente movimiento a realizar por el mech jugador.
		Escribe los pasos en el fichero accionJx.sbt
	"""
	def nextMove(self):
		# Obtenemos un objetivo.
		enemy,distance = self.setTarjet()
		# Obtenemos su localización y orientación
		for m in self.mechs.mechs:
			if m.nombre == enemy:
				faceTorsoEnemy = (m.lado+2)%6
				cellEnemy = int(m.hexagono[2:4])-1,int(m.hexagono[0:2])-1
		
		# Si estamos en el suelo -> Nos levantamos
		if self.jugador.suelo and self.jugador.andar >= 2:
			self.getUp = True
			# Obtenemos nuestra posición relativa respecto del enemigo.
			face = relative_position(self.jugadorCell, cellEnemy)
			# Nos levantamos andando.
			self.movType = 0
			self.nextCell = self.jugadorCell
			self.nextFace = face
			self.stepCell.append((4,face))
		
		# Si nuestro turno es antes que el del enemigo -> Hide
		#~ if self.ini.posiciones.index(self.playerN)< self.ini.posiciones.index(enemy):
		if self.ini.posiciones.index(self.playerN) == 0:
			self._hide()
		else: # Si nuestro turno es después -> Nos acercamos por detrás
			
			self.path, self.movType = self._approach(cellEnemy,faceTorsoEnemy)
			print "Desde ",self.jugadorCell,"Lado ",self.jugadorLado," Hasta ",cellEnemy
			print self.path,self.movType
		self.fileAccion()
	
	""" Permanecer inmóvil.
	"""
	def _hide (self):
		print "HIDE"
		self.movType = 3
	
	""" Calcula el camino mínimo para acercarse al hexágono en el que se
		encuentra el enemigo por el lado de su espalda.
		
		@param enemy Localización del enemigo.
		@param faceTorsoEnemy Orientación del enemigo.
		@return (camino mínimo,tipo de movimiento)
	"""
	def _approach (self, enemy, faceTorsoEnemy):
		# Obtenemos las celdas adyacentes a la posición del enemigo.
		x = adjacent_cells(enemy, faceTorsoEnemy)
		
		# Preparamos el algoritmo A*
		pf = PathFinder(self.board.sucesores, self.board.moveCost, self.board.heuristic_to_goal)
		A = Pos(self.jugadorCell, self.jugadorLado)
		B = Pos(x, facing_side(x, enemy))
		can = False
		#~ print "hex =",self.jugador.hexagono
		#~ print "Andar =",self.jugador.andar,"\nCorrer =",self.jugador.correr,"\nSaltar =",self.jugador.saltar
		# Obtenemos un path andando.
		#~ if self.jugador.andar != 0:
		print "Andando"
		path, can, cost = pf.compute_path_until_PM(A, B, 0,self.jugador.andar)
		#~ print 'Path=',path,'\nCAN=',can,'\nCost=',cost
		if can == False and self.jugador.correr != 0:
			# Obtenemos un path corriendo
			print "Corriendo"
			path2, can2, cost2 = pf.compute_path_until_PM(A, B, 1, self.jugador.correr)
			print 'Path=',path2,'\nCAN=',can2,'\nCost=',cost2
			if can2 == True:
				print (path2,1)
				return (path2, 1)
		if can == False and self.jugador.saltar != 0:
			# Obtenemos un path saltando
			print "Saltando"
			path3, can3, cost3 = pf.compute_path_until_PM(A, B, 2, self.jugador.saltar)
			print 'Path=',path3,'\nCAN=',can3,'\nCost=',cost3
			if can3 == True:
				print (path3,2)
				return (path3,2)
		#~ print "Can=",can,"\nPath: ",path
		#~ print "Objetivo = ",x
		return (path, 0)
	
	""" Calcula los pasos necesarios para realizar un movimiento en el
		simulador de BattleTech.
		
		@return Lista de movimientos, número de movimientos
	"""
	def calculate_steps(self):
		moves = []
		s = 0
		i = 1
		while i < len(self.path):
			y = self.path[i-1]
			x = self.path[i]
			if y.face != x.face:
				costFace = min((x.face - y.face)%6,(y.face - x.face)%6)
				if (y.face - costFace) % 6 == x.face:
					moves.append((2,costFace))
					s+=1
					if i+1 !=len(self.path):
						moves.append((0,1))
						s+=1
				else:
					moves.append((3, costFace))
					s+=1
					if i+1 !=len(self.path):
						moves.append((0,1))
						s+=1
				i+=1
			else:
				aux=1
				i+=1
				while i < len(self.path):
					y = self.path[i-1]; x = self.path[i]
					if x.face == y.face:
						aux+=1
					else: break
					i+=1
				moves.append((0,aux))
				s+=1
		return moves,s
	
	""" Escribe en el fichero accionJx.sbt los pasos a realizar para 
		lograr llegar al objetivo del mech jugador.
	"""
	def fileAccion(self):
		global mov, step
		# Apertura del fichero. Modo escritura
		file = open("accionJ"+ str(self.playerN)+".sbt","w")
		
		# Si no hemos encontrado un camino.
		# Inmóvil
		if self.path == [] or self.path == None:
			print "LAST PATH=",self.path
			self.movType = 3
		elif len(self.path) == 1:
			if int(self.jugador.hexagono[:2]) == self.path[0].pos[1]+1 and int(self.jugador.hexagono[2:4]) == self.path[0].pos[0]+1:
				self.movType = 3
				
		# Tipo de movimiento a realizar
		file.write(str(mov[self.movType])+"\n")
		# Si es Levantarse
		if self.getUp == True:
			p = Pos(self.nextCell, self.nextFace)
			# Hexágono destino
			file.write(str(p.printPos())+"\n")
			# Lado final
			file.write(str(p.printFace())+"\n")
			# MASC
			file.write(str(self.masc)+"\n")
			# Tipo de movimiento
			file.write(str(1)+"\n")
			# Tipo de paso
			file.write(str(step[4])+"\n")
			# Lado del paso
			file.write(str(p.printFace())+"\n")
		# Si es Andar o Correr
		elif self.movType == 0 or self.movType == 1:
			p = self.path[len(self.path)-1]
			# Hexágono destino
			file.write(str(p.printPos())+"\n")
			# Lado final
			file.write(str(p.printFace())+"\n")
			# MASC
			file.write(str(self.masc)+"\n")
			# Calculamos los pasos a seguir
			move,s = self.calculate_steps()
			# Número de pasos
			file.write(str(s)+"\n")
			# Para cada paso
			for x in move:
				# Tipo de paso
				file.write(str(step[x[0]])+"\n")
				# Veces que lo aplicamos
				file.write(str(x[1])+"\n")
		# Si es Saltar
		elif self.movType == 2:
			p = self.path[len(self.path)-1]
			file.write(str(p.printPos())+"\n")
			file.write(str(p.printFace())+"\n")
		# Cerramos el fichero
		file.close()

# COMPROBACIÓN
def main():
	mov = Movimiento(0)
	mov.nextMove()
	print "correcto"
	return 0

if __name__ == '__main__':
	main()


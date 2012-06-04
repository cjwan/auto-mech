#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       reaccion.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

import sys
from mechsSBT import *
from utils import *

class Reaccion:
	def __init__ (self, playerN):
		# Número del jugador automático
		self.playerN = playerN
		# Fichero mechsJx.sbt
		self.mechs = MechsSBT(self.playerN)
		self.mechs.leeFichero()
		
		self.facing = None
		self.jugador = self.mechs.jugador
		self.jugadorLado = self.jugador.lado -1
	
	def reacciona(self):
		blindaje_izq = 0
		# BI
		blindaje_izq+=self.jugador.blindaje[0]
		# TI
		blindaje_izq+=self.jugador.blindaje[1]
		# PI
		blindaje_izq+=self.jugador.blindaje[2]
		# PATI
		blindaje_izq+=self.jugador.blindaje[8]
		
		blindaje_der = 0
		# BD
		blindaje_der+=self.jugador.blindaje[3]
		# TD
		blindaje_der+=self.jugador.blindaje[4]
		# PD
		blindaje_der+=self.jugador.blindaje[5]
		# PATD
		blindaje_der+=self.jugador.blindaje[9]
		
		if blindaje_izq < blindaje_der:
			self.facing = "Izquierda"
		elif blindaje_der < blindaje_izq:
			self.facing = "Derecha"
		else:
			self.facing = "Igual"
		
		self.fileAccion()
	
	
	""" Escribe en el fichero accionJx.sbt los pasos a realizar para 
		lograr llegar al objetivo del mech jugador.
	"""
	def fileAccion(self):
		# Apertura del fichero. Modo escritura
		file = open("accionJ"+ str(self.playerN)+".sbt","w")
		# Dirección hacia la que girar el torso
		file.write(str(self.facing)+"\n")
		# Cerramos el fichero
		file.close()

# COMPROBACIÓN
def main():
	rea = Reaccion(0)
	rea.reacciona()
	print "correcto"
	return 0

if __name__ == '__main__':
	main()

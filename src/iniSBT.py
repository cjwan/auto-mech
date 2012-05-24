#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       iniSBT.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

from utils import error

class Iniciativa:
	def __init__(self, num):
		self.posiciones = []
		fileName = 'iniciativaJ'+str(num)+'.sbt'
		try:
			file = open(fileName, "r")
		except:
			error("No se ha podido abrir el fichero "+fileName)
		else:
			self.jugadores = int(file.readline())
			for i in range (self.jugadores):
				self.posiciones.append(int(file.readline()))
			file.close()


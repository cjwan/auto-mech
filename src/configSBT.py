#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       configSBT.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

import string
from utils import error,str2bool

class ConfigSBT:
	"""
		Clase manejadora del fichero configJX.sbt
	"""
	def __init__(self,numJ=0):
		self.nombre = 'configSBT'
		self.numJ = int(numJ)
		try:
			self.file = open('configJ'+str(self.numJ)+'.sbt','r')
		except:
			error("No se ha podido abrir el fichero configJ"+str(self.numJ)+".sbt .")
	
	def leeFichero(self):
		# Comprobamos la cabecera para asegurar que es correcto.
		cabecera = self.file.readline()
		if string.find(cabecera,self.nombre) == -1:
			self.file.close()
			error("No es un fichero configSBT . ")
		else:
			# Incendios permitidos
			self.fuego = str2bool(self.file.readline())
			# Viento permitido
			self.viento = str2bool(self.file.readline())
			# Dirección del viento
			self.dir_viento = int(self.file.readline())
			# Ataque físico permitido
			self.at_fisico = str2bool(self.file.readline())
			# Fase de comprobación del calor
			self.fase_calor = str2bool(self.file.readline())
			# Se permite devastar bosques
			self.dest_bosque = str2bool(self.file.readline())
			# Se permite devastar Edificios
			self.dest_edificio = str2bool(self.file.readline())
			# Chequeo de pilotaje
			self.pilotCheck = str2bool(self.file.readline())
			# Chequeo de daños
			self.damageCheck = str2bool(self.file.readline())
			# Chequeo de desconexión
			self.disconnectionCheck = str2bool(self.file.readline())
			# Daños críticos permitidos
			self.criticos = str2bool(self.file.readline())
			# Explosión de la munición permitida
			self.explosion_municion = str2bool(self.file.readline())
			# Se pueden apagar radiadores
			self.apagar_radiadores = str2bool(self.file.readline())
			# Chequeo de límite de tiempo
			self.timeLimitCheck = str2bool(self.file.readline())
			# Límite de tiempo
			self.timeLimit = int(self.file.readline())
			self.file.close()
		



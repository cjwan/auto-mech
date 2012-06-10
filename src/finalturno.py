#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       finalturno.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

from mechsSBT import *
from mapaSBT import *
from configSBT import *
from defmechSBT import *

class EndTurn:
	""" End of Turn File"""
	
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
		# Fichero de configuración
		self.conf = ConfigSBT(self.playerN)
		self.conf.leeFichero()
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
		# Lista de enemigos
		self.enemigos = []
		for i in range(len(self.mechs.mechs)):
			if self.mechs.mechs[i].nombre != self.playerN :
				self.enemigos.append(self.mechs.mechs[i])
	
	def printAction(self):
		file = open("accionJ"+ str(self.playerN)+".sbt", "w")
		if self.conf.apagar_radiadores:
			file.write(str(0)+"\n")
			file.write(str(self.jugador.rad_apagados)+'\n')
			if self.jugador.garrote:
				file.write("True\n")
			else:
				file.write("False\n")
			file.write(str(self.jugador.soltar_municion)+'\n')
			if self.jugador.soltar_municion > 0:
				for mun in self.jugador.municiones:
					file.write(mun[0]+'\n')
					file.write(str(mun[1])+'\n')
		else:
			file.write(str(0) +"\n")
			file.write(str(0) +"\n")
			file.write("False\n")
			file.write(str(0) +"\n")
		file.close()
	

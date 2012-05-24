#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       celda.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>

class Celda(object):
	def __init__(self):
		self.__x = None
		self.__y = None
		self.__nivel = None
		""" Tipo de terreno:
			0 - Terreno abierto
			1 - Terreno pavimentado
			2 - Agua
			3 - Terreno pantanoso """
		self.__terreno = None
		""" Tipo de obstáculo:
			0 - escombros
			1 - bosque ligero
			2 - bosque denso
			3 - edificio ligero
			4 - edificio medio
			5 - edificio pesado
			6 - edificio reforzado
			7 - bunker
			255 - NADA - ningun objeto """
		self.__objeto = None
		self.__fce = None
		self.__edificioDerrumbado = None
		self.__fuego = None
		self.__humo = None
		self.__garrote = None
		self.rios = []
		self.carreteras = []
		
	def getX (self):
		return self.__x
	
	def setX (self, x):
		self.__x = x
	x = property(getX, setX)
	
	def getY (self):
		return self.__y
	
	def setY (self, y):
		self.__y = y
	y = property(getY, setY)
	
	def getNivel (self):
		return self.__nivel
	
	def setNivel (self, nivel):
		self.__nivel = nivel
	nivel = property(getNivel, setNivel)
	
	def getTerreno (self):
		return self.__terreno
	
	def setTerreno (self, terreno):
		if terreno >= 0:
			self.__terreno = terreno
		else:
			print "Error: terreno no válido."
	terreno = property(getTerreno, setTerreno)
	
	def getObjeto (self):
		return self.__objeto
	
	def setObjeto (self, objeto):
		if objeto >= 0:
			self.__objeto = objeto
		else:
			print "Error: objeto no válido."
	objeto = property(getObjeto, setObjeto)
	
	def getFce (self):
		return self.__fce
	
	def setFce (self, fce):
		if fce >= 0:
			self.__fce = fce
		else:
			print "Error: fce no válido."
	fce = property(getFce, setFce)
	
	def getEdificioDerrumbado(self):
		return self.__edificioDerrumbado
	
	def setEdificioDerrumbado (self, edificioDerrumbado):
		self.__edificioDerrumbado = edificioDerrumbado
	edificioDerrumbado = property(getEdificioDerrumbado, setEdificioDerrumbado)
	
	def getFuego (self):
		return self.__fuego
	
	def setFuego (self, fuego):
		self.__fuego = fuego
	fuego = property(getFuego, setFuego)
	
	def getHumo (self):
		return self.__humo
	
	def setHumo (self, humo):
		self.__humo = humo
	humo = property(getHumo, setHumo)
	
	def getGarrote (self):
		return self.__garrote
	
	def setGarrote (self, garrote):
		if garrote >= 0:
			self.__garrote = garrote
		else:
			print "Error: garrote no válido."
	garrote = property(getGarrote, setGarrote)


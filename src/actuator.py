#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       actuator.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

class Actuator(object):
	
	def __init__(self):
		self.__code = None 
		self.__name = None  
		self.__itemLocation = None  
		self.__operative = None  
		self.__impactsNumber = None 
	
	
	def getCode (self):
		return self.__code
	
	def setCode (self, code):
		if isinstance(code, int):
			self.__code = code
		else:
			print "Error, incorrect code!"
	code = property(getCode, setCode)
	
	def getName (self):
		return self.__name
	
	def setName (self, name):
		if isinstance(name, str):
			self.__name = name
		else:
			print "Error, incorrect name!"
	name = property(getName, setName)
	
	def getItemLocation (self):
		return self.__itemLocation
	
	def setItemLocation (self, itemLocation):
		if isinstance(itemLocation, int):
			self.__itemLocation = itemLocation
		else:
			print "Error, incorrect itemLocation!"
	itemLocation = property(getItemLocation, setItemLocation)
	
	def getOperative (self):
		return self.__operative
	
	def setOperative (self, operative):
		if isinstance(operative, bool):
			self.__operative = operative
		else:
			print "Error, incorrect operative!"
	operative = property(getOperative, setOperative)
	
	def getImpactsNumber (self):
		return self.__impactsNumber
	
	def setImpactsNumber (self, impactsNumber):
		if isinstance(impactsNumber, int):
			self.__impactsNumber = impactsNumber
		else:
			print "Error, incorrect impactsNumber!"
	impactsNumber = property(getImpactsNumber, setImpactsNumber)
	

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       location.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

class Location(object):
	
	def __init__(self):
		self.__slotNumber = None 
		self.slot = []
	
	
	def getSlotNumber (self):
		return self.__slotNumber
	
	def setSlotNumber (self, slotNumber):
		if isinstance(slotNumber, int):
			self.__slotNumber = slotNumber
		else:
			print "Error, incorrect slotNumber!"
	slotNumber = property(getSlotNumber, setSlotNumber)
	

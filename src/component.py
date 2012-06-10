#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       component.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

class Component(object):
	
	def __init__(self):
		self.__code = None 
		self.__name = None
		self.__type = None 
		self.__weaponInBack = None
		self.__itemLocation = None
		self.__secondaryItemLocation = None
		self.__weaponType = None
		self.__heat = None
		self.__harm = None
		self.__shotsPerTurn = None
		self.__minimumDistance = None
		self.__shortDistance = None
		self.__mediumDistance = None
		self.__longDistance = None
		self.__operativeTeam = None
		self.__weaponCode = None #if ammunition
		self.__amount = None 
		# in leeme.txt is supposed to be a bool, however some vals are cluster?
		self.__specialAmmunition = None
		self.__triggerSwitch = None
	
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
	
	def getType (self):
		return self.__type
	
	def setType (self, type):
		if isinstance(type, str):
			self.__type = type
		else:
			print "Error, incorrect type!"
	type = property(getType, setType)
	
	def getWeaponInBack (self):
		return self.__weaponInBack
	
	def setWeaponInBack (self, weaponInBack):
		if isinstance(weaponInBack, bool):
			self.__weaponInBack = weaponInBack
		else:
			print "Error, incorrect weaponInBack!"
	weaponInBack = property(getWeaponInBack, setWeaponInBack)
	
	def getItemLocation (self):
		return self.__itemLocation
	
	def setItemLocation (self, itemLocation):
		if isinstance(itemLocation, int):
			self.__itemLocation = itemLocation
		else:
			print "Error, incorrect itemLocation!"
	itemLocation = property(getItemLocation, setItemLocation)
	
	def getSecondaryItemLocation (self):
		return self.__secondaryItemLocation
	
	def setSecondaryItemLocation (self, secondaryItemLocation):
		if isinstance(secondaryItemLocation, int):
			self.__secondaryItemLocation = secondaryItemLocation
		else:
			print "Error, incorrect secondaryItemLocation!"
	secondaryItemLocation = property(getSecondaryItemLocation, setSecondaryItemLocation)
	
	def getWeaponType (self):
		return self.__weaponType
	
	def setWeaponType (self, weaponType):
		if isinstance(weaponType, str):
			self.__weaponType = weaponType
		else:
			print "Error, incorrect weaponType!"
	weaponType = property(getWeaponType, setWeaponType)
	
	def getHeat (self):
		return self.__heat
	
	def setHeat (self, heat):
		if isinstance(heat, int):
			self.__heat = heat
		else:
			print "Error, incorrect heat!"
	heat = property(getHeat, setHeat)
	
	def getHarm (self):
		return self.__harm
	
	def setHarm (self, harm):
		if isinstance(harm, int):
			self.__harm = harm
		else:
			print "Error, incorrect harm!"
	harm = property(getHarm, setHarm)
	
	def getShotsPerTurn (self):
		return self.__shotsPerTurn
	
	def setShotsPerTurn (self, shotsPerTurn):
		if isinstance(shotsPerTurn, int):
			self.__shotsPerTurn = shotsPerTurn
		else:
			print "Error, incorrect shotsPerTurn!"
	shotsPerTurn = property(getShotsPerTurn, setShotsPerTurn)
	
	def getMinimumDistance (self):
		return self.__minimumDistance
	
	def setMinimumDistance (self, minimumDistance):
		if isinstance(minimumDistance, int):
			self.__minimumDistance = minimumDistance
		else:
			print "Error, incorrect minimumDistance!"
	minimumDistance = property(getMinimumDistance, setMinimumDistance)
	
	def getShortDistance (self):
		return self.__shortDistance
	
	def setShortDistance (self, shortDistance):
		if isinstance(shortDistance, int):
			self.__shortDistance = shortDistance
		else:
			print "Error, incorrect shortDistance!"
	shortDistance = property(getShortDistance, setShortDistance)
	
	def getMediumDistance (self):
		return self.__mediumDistance
	
	def setMediumDistance (self, mediumDistance):
		if isinstance(mediumDistance, int):
			self.__mediumDistance = mediumDistance
		else:
			print "Error, incorrect mediumDistance!"
	mediumDistance = property(getMediumDistance, setMediumDistance)
	
	def getLongDistance (self):
		return self.__longDistance
	
	def setLongDistance (self, longDistance):
		if isinstance(longDistance, int):
			self.__longDistance = longDistance
		else:
			print "Error, incorrect longDistance!"
	longDistance = property(getLongDistance, setLongDistance)
	
	def getOperativeTeam (self):
		return self.__operativeTeam
	
	def setOperativeTeam (self, operativeTeam):
		if isinstance(operativeTeam, bool):
			self.__operativeTeam = operativeTeam
		else:
			print "Error, incorrect operativeTeam!"
	operativeTeam = property(getOperativeTeam, setOperativeTeam)
	
	def getWeaponCode (self):
		return self.__weaponCode
	
	def setWeaponCode (self, weaponCode):
		if isinstance(weaponCode, int):
			self.__weaponCode = weaponCode
		else:
			print "Error, incorrect weaponCode!"
	weaponCode = property(getWeaponCode, setWeaponCode)
	
	
	def getAmount (self):
		return self.__amount
	
	def setAmount (self, amount):
		if isinstance(amount, int):
			self.__amount = amount
		else:
			print "Error, incorrect amount!"
	amount = property(getAmount, setAmount)
	
	def getSpecialAmmunition (self):
		return self.__specialAmmunition
	
	def setSpecialAmmunition (self, specialAmmunition):
		if isinstance(specialAmmunition, str):
			self.__specialAmmunition = specialAmmunition
		else:
			print "Error, incorrect specialAmmunition!"
	specialAmmunition = property(getSpecialAmmunition, setSpecialAmmunition)
	
	def getTriggerSwitch (self):
		return self.__triggerSwitch
	
	def setTriggerSwitch (self, triggerSwitch):
		if isinstance(triggerSwitch, int):
			self.__triggerSwitch = triggerSwitch
		else:
			print "Error, incorrect triggerSwitch!"
	triggerSwitch = property(getTriggerSwitch, setTriggerSwitch)
	

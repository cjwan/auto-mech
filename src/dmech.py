#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       dmech.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

from partes import Location

class Dmech(object):
	
	def __init__(self):
		self.__name = None #string
		self.__model = None #string
		self.__ton = None #int
		self.__power = None #int
		self.__internalRadiators = None #int
		self.__radiators = None
		self.__masc = None #bool
		self.__dacmtd = None
		self.__dacmti = None
		self.__dacmtc = None
		self.__heat = None #int 
		self.__arms = None #bool
		self.__lShoulder = None
		self.__lArm = None
		self.__lForearm = None
		self.__lHand = None
		self.__rShoulder = None
		self.__rArm = None
		self.__rForearm = None
		self.__rHand = None
		self.__lArmArmor = None #int
		self.__lTorsoArmor = None
		self.__lLegArmor = None
		self.__rLegArmor = None
		self.__rTorsoArmor = None
		self.__rArmArmor = None
		self.__cTorsoArmor = None
		self.__headArmor = None
		self.__lBackTorsoArmor = None
		self.__rBackTorsoArmor = None
		self.__cBackTorsoArmor = None
		self.__lInternalArmPoints = None
		self.__lInternalTorsoPoints = None
		self.__lInternalLegPoints = None
		self.__rInternalLegPoints = None
		self.__rInternalTorsoPoints = None
		self.__rInternalArmPoints = None
		self.__cInternalTorsoPoints = None
		self.__internalHeadPoints = None
		self.__equippedComponentsNumber = None
		self.component = []
	
	
		self.__weaponsNumber = None
		self.__actuatorsNumber = None
		self.actuator = []
	
		self.location = []
		for i in range(8):
			self.location.append(Location())
	
		self.__walkPoints = None
		self.__runPoints = None
		self.__jumpPoints = None
		self.__radiatorsType = None # 0-simple or 1-double
		
	def getName (self):
		return self.__name
	
	def setName (self, name):
		if isinstance(name, str):
			self.__name = name
		else:
			print "Error, incorrect name!"
	name = property(getName, setName)
	
	def getModel (self):
		return self.__model
	
	def setModel (self, model):
		if isinstance(model, str):
			self.__model = model
		else:
			print "Error, incorrect model!"
	model = property(getModel, setModel)
	
	def getTon (self):
		return self.__ton
	
	def setTon (self, ton):
		if isinstance(ton, int):
			self.__ton = ton
		else:
			print "Error, incorrect ton!"
	ton = property(getTon, setTon)
	
	def getPower (self):
		return self.__power
	
	def setPower (self, power):
		if isinstance(power, int):
			self.__power = power
		else:
			print "Error, incorrect power!"
	power = property(getPower, setPower)
	
	def getInternalRadiators (self):
		return self.__internalRadiators
	
	def setInternalRadiators (self, internalRadiators):
		if isinstance(internalRadiators, int):
			self.__internalRadiators = internalRadiators
		else:
			print "Error, incorrect internalRadiators!"
	internalRadiators = property(getInternalRadiators, setInternalRadiators)
	
	def getRadiators (self):
		return self.__radiators
	
	def setRadiators (self, radiators):
		if isinstance(radiators, int):
			self.__radiators = radiators
		else:
			print "Error, incorrect radiators!"
	radiators = property(getRadiators, setRadiators)
	
	def getMasc (self):
		return self.__masc
	
	def setMasc (self, masc):
		if isinstance(masc, bool):
			self.__masc = masc
		else:
			print "Error, incorrect masc!"
	masc = property(getMasc, setMasc)
	
	def getDacmtd (self):
		return self.__dacmtd
	
	def setDacmtd (self, dacmtd):
		if isinstance(dacmtd, bool):
			self.__dacmtd = dacmtd
		else:
			print "Error, incorrect dacmtd!"
	dacmtd = property(getDacmtd, setDacmtd)
	
	def getDacmti (self):
		return self.__dacmti
	
	def setDacmti (self, dacmti):
		if isinstance(dacmti, bool):
			self.__dacmti = dacmti
		else:
			print "Error, incorrect dacmti!"
	dacmti = property(getDacmti, setDacmti)
	
	def getDacmtc (self):
		return self.__dacmtc
	
	def setDacmtc (self, dacmtc):
		if isinstance(dacmtc, bool):
			self.__dacmtc = dacmtc
		else:
			print "Error, incorrect dacmtc!"
	dacmtc = property(getDacmtc, setDacmtc)
	
	def getHeat (self):
		return self.__heat
	
	def setHeat (self, heat):
		if isinstance(heat, int):
			self.__heat = heat
		else:
			print "Error, incorrect heat!"
	heat = property(getHeat, setHeat)
	
	def getArms (self):
		return self.__arms
	
	def setArms (self, arms):
		if isinstance(arms, bool):
			self.__arms = arms
		else:
			print "Error, incorrect arms!"
	arms = property(getArms, setArms)
	
	def getLShoulder (self):
		return self.__lShoulder
	
	def setLShoulder (self, lShoulder):
		if isinstance(lShoulder, bool):
			self.__lShoulder = lShoulder
		else:
			print "Error, incorrect lShoulder!"
	lShoulder = property(getLShoulder, setLShoulder)
	
	def getLArm (self):
		return self.__lArm
	
	def setLArm (self, lArm):
		if isinstance(lArm, bool):
			self.__lArm = lArm
		else:
			print "Error, incorrect lArm!"
	lArm = property(getLArm, setLArm)
	
	def getLForearm (self):
		return self.__lForearm
	
	def setLForearm (self, lForearm):
		if isinstance(lForearm, bool):
			self.__lForearm = lForearm
		else:
			print "Error, incorrect lForearm!"
	lForearm = property(getLForearm, setLForearm)
	
	def getLHand (self):
		return self.__lHand
	
	def setLHand (self, lHand):
		if isinstance(lHand, bool):
			self.__lHand = lHand
		else:
			print "Error, incorrect lHand!"
	lHand = property(getLHand, setLHand)
	
	def getRShoulder (self):
		return self.__rShoulder
	
	def setRShoulder (self, rShoulder):
		if isinstance(rShoulder, bool):
			self.__rShoulder = rShoulder
		else:
			print "Error, incorrect rShoulder!"
	rShoulder = property(getRShoulder, setRShoulder)
	
	def getRArm (self):
		return self.__rArm
	
	def setRArm (self, rArm):
		if isinstance(rArm, bool):
			self.__rArm = rArm
		else:
			print "Error, incorrect rArm!"
	rArm = property(getRArm, setRArm)
	
	def getRForearm (self):
		return self.__rForearm
	
	def setRForearm (self, rForearm):
		if isinstance(rForearm, bool):
			self.__rForearm = rForearm
		else:
			print "Error, incorrect rForearm!"
	rForearm = property(getRForearm, setRForearm)
	
	def getRHand (self):
		return self.__rHand
	
	def setRHand (self, rHand):
		if isinstance(rHand, bool):
			self.__rHand = rHand
		else:
			print "Error, incorrect rHand!"
	rHand = property(getRHand, setRHand)
	
	def getLArmArmor (self):
		return self.__lArmArmor
	
	def setLArmArmor (self, lArmArmor):
		if isinstance(lArmArmor, int):
			self.__lArmArmor = lArmArmor
		else:
			print "Error, incorrect lArmArmor!"
	lArmArmor = property(getLArmArmor, setLArmArmor)
	
	def getLTorsoArmor (self):
		return self.__lTorsoArmor
	
	def setLTorsoArmor (self, lTorsoArmor):
		if isinstance(lTorsoArmor, int):
			self.__lTorsoArmor = lTorsoArmor
		else:
			print "Error, incorrect lTorsoArmor!"
	lTorsoArmor = property(getLTorsoArmor, setLTorsoArmor)
	
	def getLLegArmor (self):
		return self.__lLegArmor
	
	def setLLegArmor (self, lLegArmor):
		if isinstance(lLegArmor, int):
			self.__lLegArmor = lLegArmor
		else:
			print "Error, incorrect lLegArmor!"
	lLegArmor = property(getLLegArmor, setLLegArmor)
	
	def getRLegArmor (self):
		return self.__rLegArmor
	
	def setRLegArmor (self, rLegArmor):
		if isinstance(rLegArmor, int):
			self.__rLegArmor = rLegArmor
		else:
			print "Error, incorrect rLegArmor!"
	rLegArmor = property(getRLegArmor, setRLegArmor)
	
	def getRTorsoArmor (self):
		return self.__rTorsoArmor
	
	def setRTorsoArmor (self, rTorsoArmor):
		if isinstance(rTorsoArmor, int):
			self.__rTorsoArmor = rTorsoArmor
		else:
			print "Error, incorrect rTorsoArmor!"
	rTorsoArmor = property(getRTorsoArmor, setRTorsoArmor)
	
	def getRArmArmor (self):
		return self.__rArmArmor
	
	def setRArmArmor (self, rArmArmor):
		if isinstance(rArmArmor, int):
			self.__rArmArmor = rArmArmor
		else:
			print "Error, incorrect rArmArmor!"
	rArmArmor = property(getRArmArmor, setRArmArmor)
	
	def getCTorsoArmor (self):
		return self.__cTorsoArmor
	
	def setCTorsoArmor (self, cTorsoArmor):
		if isinstance(cTorsoArmor, int):
			self.__cTorsoArmor = cTorsoArmor
		else:
			print "Error, incorrect cTorsoArmor!"
	cTorsoArmor = property(getCTorsoArmor, setCTorsoArmor)
	
	def getHeadArmor (self):
		return self.__headArmor
	
	def setHeadArmor (self, headArmor):
		if isinstance(headArmor, int):
			self.__headArmor = headArmor
		else:
			print "Error, incorrect headArmor!"
	headArmor = property(getHeadArmor, setHeadArmor)
	
	def getLBackTorsoArmor (self):
		return self.__lBackTorsoArmor
	
	def setLBackTorsoArmor (self, lBackTorsoArmor):
		if isinstance(lBackTorsoArmor, int):
			self.__lBackTorsoArmor = lBackTorsoArmor
		else:
			print "Error, incorrect lBackTorsoArmor!"
	lBackTorsoArmor = property(getLBackTorsoArmor, setLBackTorsoArmor)
	
	def getRBackTorsoArmor (self):
		return self.__rBackTorsoArmor
	
	def setRBackTorsoArmor (self, rBackTorsoArmor):
		if isinstance(rBackTorsoArmor, int):
			self.__rBackTorsoArmor = rBackTorsoArmor
		else:
			print "Error, incorrect rBackTorsoArmor!"
	rBackTorsoArmor = property(getRBackTorsoArmor, setRBackTorsoArmor)
	
	def getCBackTorsoArmor (self):
		return self.__cBackTorsoArmor
	
	def setCBackTorsoArmor (self, cBackTorsoArmor):
		if isinstance(cBackTorsoArmor, int):
			self.__cBackTorsoArmor = cBackTorsoArmor
		else:
			print "Error, incorrect cBackTorsoArmor!"
	cBackTorsoArmor = property(getCBackTorsoArmor, setCBackTorsoArmor)
	
	def getLInternalArmPoints (self):
		return self.__lInternalArmPoints
	
	def setLInternalArmPoints (self, lInternalArmPoints):
		if isinstance(lInternalArmPoints, int):
			self.__lInternalArmPoints = lInternalArmPoints
		else:
			print "Error, incorrect lInternalArmPoints!"
	lInternalArmPoints = property(getLInternalArmPoints, setLInternalArmPoints)
	
	def getLInternalTorsoPoints (self):
		return self.__lInternalTorsoPoints
	
	def setLInternalTorsoPoints (self, lInternalTorsoPoints):
		if isinstance(lInternalTorsoPoints, int):
			self.__lInternalTorsoPoints = lInternalTorsoPoints
		else:
			print "Error, incorrect lInternalTorsoPoints!"
	lInternalTorsoPoints = property(getLInternalTorsoPoints, setLInternalTorsoPoints)
	
	def getLInternalLegPoints (self):
		return self.__lInternalLegPoints
	
	def setLInternalLegPoints (self, lInternalLegPoints):
		if isinstance(lInternalLegPoints, int):
			self.__lInternalLegPoints = lInternalLegPoints
		else:
			print "Error, incorrect lInternalLegPoints!"
	lInternalLegPoints = property(getLInternalLegPoints, setLInternalLegPoints)
	
	def getRInternalLegPoints (self):
		return self.__rInternalLegPoints
	
	def setRInternalLegPoints (self, rInternalLegPoints):
		if isinstance(rInternalLegPoints, int):
			self.__rInternalLegPoints = rInternalLegPoints
		else:
			print "Error, incorrect rInternalLegPoints!"
	rInternalLegPoints = property(getRInternalLegPoints, setRInternalLegPoints)
	
	def getRInternalTorsoPoints (self):
		return self.__rInternalTorsoPoints
	
	def setRInternalTorsoPoints (self, rInternalTorsoPoints):
		if isinstance(rInternalTorsoPoints, int):
			self.__rInternalTorsoPoints = rInternalTorsoPoints
		else:
			print "Error, incorrect rInternalTorsoPoints!"
	rInternalTorsoPoints = property(getRInternalTorsoPoints, setRInternalTorsoPoints)
	
	def getRInternalArmPoints (self):
		return self.__rInternalArmPoints
	
	def setRInternalArmPoints (self, rInternalArmPoints):
		if isinstance(rInternalArmPoints, int):
			self.__rInternalArmPoints = rInternalArmPoints
		else:
			print "Error, incorrect rInternalArmPoints!"
	rInternalArmPoints = property(getRInternalArmPoints, setRInternalArmPoints)
	
	def getCInternalTorsoPoints (self):
		return self.__cInternalTorsoPoints
	
	def setCInternalTorsoPoints (self, cInternalTorsoPoints):
		if isinstance(cInternalTorsoPoints, int):
			self.__cInternalTorsoPoints = cInternalTorsoPoints
		else:
			print "Error, incorrect cInternalTorsoPoints!"
	cInternalTorsoPoints = property(getCInternalTorsoPoints, setCInternalTorsoPoints)
	
	def getInternalHeadPoints (self):
		return self.__internalHeadPoints
	
	def setInternalHeadPoints (self, internalHeadPoints):
		if isinstance(internalHeadPoints, int):
			self.__internalHeadPoints = internalHeadPoints
		else:
			print "Error, incorrect internalHeadPoints!"
	internalHeadPoints = property(getInternalHeadPoints, setInternalHeadPoints)
	
	def getEquippedComponentsNumber (self):
		return self.__equippedComponentsNumber
	
	def setEquippedComponentsNumber (self, equippedComponentsNumber):
		if isinstance(equippedComponentsNumber, int):
			self.__equippedComponentsNumber = equippedComponentsNumber
		else:
			print "Error, incorrect equippedComponentsNumber!"
	equippedComponentsNumber = property(getEquippedComponentsNumber, setEquippedComponentsNumber)
	
	def getWeaponsNumber (self):
		return self.__weaponsNumber
	
	def setWeaponsNumber (self, weaponsNumber):
		if isinstance(weaponsNumber, int):
			self.__weaponsNumber = weaponsNumber
		else:
			print "Error, incorrect weaponsNumber!"
	weaponsNumber = property(getWeaponsNumber, setWeaponsNumber)
	
	def getActuatorsNumber (self):
		return self.__actuatorsNumber
	
	def setActuatorsNumber (self, actuatorsNumber):
		if isinstance(actuatorsNumber, int):
			self.__actuatorsNumber = actuatorsNumber
		else:
			print "Error, incorrect actuatorsNumber!"
	actuatorsNumber = property(getActuatorsNumber, setActuatorsNumber)
	
	def getWalkPoints (self):
		return self.__walkPoints
	
	def setWalkPoints (self, walkPoints):
		if isinstance(walkPoints, int):
			self.__walkPoints = walkPoints
		else:
			print "Error, incorrect walkPoints!"
	walkPoints = property(getWalkPoints, setWalkPoints)
	
	def getRunPoints (self):
		return self.__runPoints
	
	def setRunPoints (self, runPoints):
		if isinstance(runPoints, int):
			self.__runPoints = runPoints
		else:
			print "Error, incorrect runPoints!"
	runPoints = property(getRunPoints, setRunPoints)
	
	def getJumpPoints (self):
		return self.__jumpPoints
	
	def setJumpPoints (self, jumpPoints):
		if isinstance(jumpPoints, int):
			self.__jumpPoints = jumpPoints
		else:
			print "Error, incorrect jumpPoints!"
	jumpPoints = property(getJumpPoints, setJumpPoints)
	
	def getRadiatorsType (self):
		return self.__radiatorsType
	
	def setRadiatorsType (self, radiatorsType):
		if isinstance(radiatorsType, int) and ( radiatorsType == 0 or radiatorsType == 1):
			self.__radiatorsType = radiatorsType
		else:
			print "Error, incorrect radiatorsType!"
	radiatorsType = property(getRadiatorsType, setRadiatorsType)
	
	

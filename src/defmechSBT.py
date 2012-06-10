#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       defmechSBT.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

import dmech
from partes import *
from utils import *

class DefMech:
	def __init__ (self):
		self.mech = dmech.Dmech()
		
	def readDefMech (self, fileName):
		""" 
		Read mechs from a specified file 
		
		Arguments:
			* fileName -- Path to the file containing the mechs description
		
		"""
		try:
			file = open(fileName, "r")
		except IOError:
			print "The file "+ fileName+ " does not exist"
			return -1
	
		m = dmech.Dmech()
		
		file.readline() # Read Magic Number : defmechSBT
	
		m.name = str ( file.readline() ).strip('\n').strip('\r')
		m.model = str ( file.readline() ).strip('\n').strip('\r')
		m.ton = int ( file.readline() )
		m.power = int ( file.readline() )
		m.internalRadiators = int ( file.readline() )
		m.radiators = int ( file.readline() )
		m.masc = str2bool ( file.readline() )
		m.dacmtd = str2bool ( file.readline() )
		m.dacmti = str2bool ( file.readline() )
		m.dacmtc = str2bool ( file.readline() )
		m.heat = int ( file.readline() )
		m.arms = str2bool ( file.readline() )
		m.lShoulder = str2bool ( file.readline() )
		m.lArm = str2bool ( file.readline() )
		m.lForearm = str2bool ( file.readline() )
		m.lHand = str2bool ( file.readline() )
		m.rShoulder = str2bool ( file.readline() )
		m.rArm = str2bool ( file.readline() )
		m.rForearm = str2bool ( file.readline() )
		m.rHand = str2bool ( file.readline() )
		m.lArmArmor = int ( file.readline() )
		m.lTorsoArmor = int ( file.readline() )
		m.lLegArmor = int ( file.readline() )
		m.rLegArmor = int ( file.readline() )
		m.rTorsoArmor = int ( file.readline() )
		m.rArmArmor = int ( file.readline() )
		m.cTorsoArmor = int ( file.readline() )
		m.headArmor = int ( file.readline() )
		m.lBackTorsoArmor = int ( file.readline() )
		m.rBackTorsoArmor =  int ( file.readline() )
		m.cBackTorsoArmor = int ( file.readline() )
		m.lInternalArmPoints = int ( file.readline() )
		m.lInternalTorsoPoints = int ( file.readline() )
		m.lInternalLegPoints = int ( file.readline() )
		m.rInternalLegPoints = int ( file.readline() )
		m.rInternalTorsoPoints = int ( file.readline() )
		m.rInternalArmPoints = int ( file.readline() )
		m.cInternalTorsoPoints = int ( file.readline() )
		m.internalHeadPoints = int ( file.readline() )
		m.equippedComponentsNumber = int ( file.readline() )
		for x in range (m.equippedComponentsNumber):
			m.component.append(Component() )
			m.component[x].code = int ( file.readline() )
			m.component[x].name = str ( file.readline() ).strip('\n').strip('\r')
			m.component[x].type = str ( file.readline() ).strip('\n').strip('\r')
			m.component[x].weaponInBack = str2bool ( file.readline() )
			m.component[x].itemLocation = int ( file.readline() )
			m.component[x].secondaryItemLocation = int ( file.readline() )
			m.component[x].weaponType = str ( file.readline() ).strip('\n').strip('\r')
			m.component[x].heat = int ( file.readline() )
			m.component[x].harm = int ( file.readline() )
			m.component[x].shotsPerTurn = int ( file.readline() )
			m.component[x].minimumDistance = int ( file.readline() )
			m.component[x].shortDistance = int ( file.readline() )
			m.component[x].mediumDistance = int ( file.readline() )
			m.component[x].longDistance = int ( file.readline() )
			m.component[x].operativeTeam = str2bool ( file.readline() )
			m.component[x].weaponCode = int ( file.readline() )
			m.component[x].amount = int ( file.readline() )
			m.component[x].specialAmmunition = str ( file.readline() ).strip('\n').strip('\r')
			m.component[x].triggerSwitch = int ( file.readline() )
	
		m.weaponsNumber =  int ( file.readline() )
		m.actuatorsNumber = int ( file.readline() )
		for p in range(m.actuatorsNumber):
			m.actuator.append(Actuator())
			m.actuator[p].code = int ( file.readline() )
			m.actuator[p].name = str ( file.readline() ).strip('\n').strip('\r')
			m.actuator[p].itemLocation = int ( file.readline() )
			m.actuator[p].operative = str2bool ( file.readline() )
			m.actuator[p].impactsNumber = int ( file.readline() )
		for v in range(8):
			m.location[v].slotNumber = int ( file.readline() )
			for w in range(m.location[v].slotNumber):
				m.location[v].slot.append(Slot())
				m.location[v].slot[w].type = str ( file.readline() ).strip('\n').strip('\r')
				m.location[v].slot[w].amount = int ( file.readline() )
				m.location[v].slot[w].code = int ( file.readline() )
				m.location[v].slot[w].name =  str ( file.readline() ).strip('\n').strip('\r')
				m.location[v].slot[w].componentIndex = int ( file.readline() )
				m.location[v].slot[w].actuatorIndex = int ( file.readline() )
				m.location[v].slot[w].ammunitionDamage = int ( file.readline() )
				
		m.walkPoints = int ( file.readline() )
		m.runPoints = int ( file.readline() )
		m.jumpPoints = int ( file.readline() )
		m.radiatorsType = int ( file.readline() )
	
		self.mech = m
	

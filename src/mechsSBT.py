#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       mechsSBT.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       


"""
	FALTA:
		- Reunir información para la fase de Ataque con Armas
		- Reunir información para la fase de Ataque Físico
		- Confirmar que todo está bien.
"""


import string
from utils import error,str2bool

class Mech:
	"""Clase que alberga la información de un Mech dada por un fichero .sbt"""
	def __init__(self,num=0):
		self.nombre = int(num)
		
	def leeMech(self,n_mechs,fichero,fase,indice):
		# Recopilamos la información que siempre utilizaremos
		# Suponemos el indice en la linea con el nº de mech
		sub_indice = 1
		sub_indice += indice
		# Si está operativo
		if string.find(fichero[sub_indice],"True") != -1:
			self.operativo = True
		elif string.find(fichero[sub_indice],"False") != -1:
			self.operativo = False
			
		sub_indice+=1
		# Si está desconectado
		if string.find(fichero[sub_indice],"True") != -1:
			self.desconectado = True
		elif string.find(fichero[sub_indice],"False") != -1:
			self.desconectado = False
		
		sub_indice+=1
		# Si está atascado
		if string.find(fichero[sub_indice],"True") != -1:
			self.atascado = True
		elif string.find(fichero[sub_indice],"False") != -1:
			self.atascado = False
		
		sub_indice+=1
		# Si está en el suelo
		if string.find(fichero[sub_indice],"True") != -1:
			self.suelo = True
		elif string.find(fichero[sub_indice],"False") != -1:
			self.suelo = False
		
		sub_indice+=1
		# El hexágono en el que se encuentra
		self.hexagono = fichero[sub_indice]
		
		#~ log.write('Se ha leido un mech: '+str(self.nombre)+'\n')
		
		# Para cada fase, obtenemos información pertinente al mech
		# MOVIMIENTO
		if int(fase) == 0:
			sub_indice+=1
			# Lado hacia el que está orientado el Mech
			self.lado = int(fichero[sub_indice])
			
			# Saltamos la linea del torso y comprobamos la temperatura
			sub_indice+=2
			self.temperatura = int(fichero[sub_indice])
			
			sub_indice+=1
			# Si está ardiendo
			if string.find(fichero[sub_indice],"True") != -1:
				self.ardiendo = True
			elif string.find(fichero[sub_indice],"False") != -1:
				self.ardiendo = False
			
		# REACCIÓN
		elif int(fase) == 1:
			sub_indice+=2
			# Lado al que está orientado el torso
			self.torso = int(fichero[sub_indice])
			
			# Saltamos 4 lineas: temp, ardiendo, garrote, tipo_garrote
			sub_indice+=4
			
			# Leemos el estado del blindaje
			"""
			Orden de las localizaciones (11):
			self.blindaje =
				[brazo izquierdo, torso izquierdo, pierna izquierda,
				pierna derecha, torso derecho, brazo derecho,
				torso central, cabeza, parte de atrás del torso izquierdo,
				parte de atrás del torso derecho,
				parte de atrás del torso central]
			"""
			self.blindaje = []
			for i in range(11):
				sub_indice+=1
				self.blindaje.append(int(fichero[sub_indice]))
			
			# Leemos el estado de la estructura
			"""
			Orden de las localizaciones (8):
			self.estructura =
				[brazo izquierdo, torso izquierdo, pierna izquierda,
				pierna derecha, torso derecho, brazo derecho,
				torso central, cabeza]
			"""
			self.estructura = []
			for i in range(8):
				sub_indice+=1
				self.estructura.append(int(fichero[sub_indice]))
		# ATAQUE ARMAS
		elif int(fase) == 2:
			pass
		# ATAQUE FÍSICO
		elif int(fase) == 3:
			pass
		# FINAL TURNO
		elif int(fase) == 4:
			# Saltamos las lineas del lado y del torso y comprobamos la temperatura
			sub_indice+=3
			self.temperatura = int(fichero[sub_indice])
			
			sub_indice+=1
			# Si está ardiendo
			if string.find(fichero[sub_indice],"True") != -1:
				self.ardiendo = True
			elif string.find(fichero[sub_indice],"False") != -1:
				self.ardiendo = False
		else:
			error("No existe esa fase.")
		
class MechJugador(Mech):
	"""
		Clase contenedora de la información relevante en la 
		fase de movimiento del mech jugador.
	"""
	def __init__(self,num=0):
		self.nombre = int(num)
	
	def leeJugador(self,n_mechs,fichero,fase,indice):
		# Obtenemos la información común del Mech
		self.leeMech(n_mechs,fichero,fase,indice)
		# Comprobamos la posición en el fichero
		if int(self.nombre) == int(fichero[indice]):
			# Obtenemos la información necesaria para el jugador
			
			#~ log.write('El mech jugador se ha leido: '+str(self.nombre)+'\n')
			
			#Para cada fase, obtenemos información pertinente al mech
			# MOVIMIENTO
			if int(fase) == 0:
				# ANDAR
				sub_indice = indice + 31
				self.andar = int(fichero[sub_indice])
				# CORRER
				sub_indice+=1
				self.correr = int(fichero[sub_indice])
				# SALTAR
				sub_indice+=1
				self.saltar = int(fichero[sub_indice])
				
				# RADIADORES
				sub_indice+=1
				self.rad_encendidos = int(fichero[sub_indice])
				sub_indice+=1
				self.rad_apagados = int(fichero[sub_indice])
				
				# Heridas del MechWarrior
				sub_indice+=1
				self.heridas = int(fichero[sub_indice])
				
				# Consciencia del MechWarrior
				sub_indice+=1
				if string.find(fichero[sub_indice],"True") != -1:
					self.consciente = True
				elif string.find(fichero[sub_indice],"False") != -1:
					self.consciente = False
			# REACCIÓN
			elif int(fase) == 1:
				sub_indice = indice + 30
				self.slots = []
				# Leemos los slots impactados
				"""
				Orden de las localizaciones (8):
				self.slots =
					[slots brazo izquierdo, slots torso izquierdo,
					slots pierna izquierda, slots pierna derecha,
					slots torso derecho, slots brazo derecho,
					slots torso central, slots cabeza]
				"""
				localizacion = []
				for i in range(11):
					sub_indice+=1
					if string.find(fichero[sub_indice],"True") != -1:
						localizacion.append(True)
					elif string.find(fichero[sub_indice],"False") != -1: 
						localizacion.append(False)
				self.slots.append(list(localizacion))
				localizacion = []
				for i in range(11):
					sub_indice+=1
					if string.find(fichero[sub_indice],"True") != -1:
						localizacion.append(True)
					elif string.find(fichero[sub_indice],"False") != -1: 
						localizacion.append(False)
				self.slots.append(list(localizacion))
				localizacion = []
				for i in range(5):
					sub_indice+=1
					if string.find(fichero[sub_indice],"True") != -1:
						localizacion.append(True)
					elif string.find(fichero[sub_indice],"False") != -1: 
						localizacion.append(False)
				self.slots.append(list(localizacion))
				localizacion = []
				for i in range(5):
					sub_indice+=1
					if string.find(fichero[sub_indice],"True") != -1:
						localizacion.append(True)
					elif string.find(fichero[sub_indice],"False") != -1: 
						localizacion.append(False)
				self.slots.append(list(localizacion))
				localizacion = []
				for i in range(11):
					sub_indice+=1
					if string.find(fichero[sub_indice],"True") != -1:
						localizacion.append(True)
					elif string.find(fichero[sub_indice],"False") != -1: 
						localizacion.append(False)
				self.slots.append(list(localizacion))
				localizacion = []
				for i in range(11):
					sub_indice+=1
					if string.find(fichero[sub_indice],"True") != -1:
						localizacion.append(True)
					elif string.find(fichero[sub_indice],"False") != -1: 
						localizacion.append(False)
				self.slots.append(list(localizacion))
				localizacion = []
				for i in range(11):
					sub_indice+=1
					if string.find(fichero[sub_indice],"True") != -1:
						localizacion.append(True)
					elif string.find(fichero[sub_indice],"False") != -1: 
						localizacion.append(False)
				self.slots.append(list(localizacion))
				localizacion = []
				for i in range(5):
					sub_indice+=1
					if string.find(fichero[sub_indice],"True") != -1:
						localizacion.append(True)
					elif string.find(fichero[sub_indice],"False") != -1: 
						localizacion.append(False)
				self.slots.append(list(localizacion))
			# ATAQUE ARMAS
			elif int(fase) == 2:
				pass
			# ATAQUE FÍSICO
			elif int(fase) == 3:
				pass
			# FINAL TURNO
			elif int(fase) == 4:
				sub_indice = indice + 34
				# RADIADORES
				self.rad_encendidos = int(fichero[sub_indice])
				sub_indice+=1
				self.rad_apagados = int(fichero[sub_indice])
				
				# Saltamos las localizaciones desde las que se ha disparado,
				# los slots impactados y el estado del MechWarrior
				sub_indice+=89
				# MUNICIÓN para Soltar
				self.soltar_municion = int(fichero[sub_indice])
				#~ print "Municion para soltar = ",self.soltar_municion
				self.municiones = []
				for i in range(self.soltar_municion):
					mun_loc = (str(fichero[sub_indice+1]),int(fichero[sub_indice+2]))
					#~ print mun_loc
					self.municiones.append(mun_loc)
					indice+=2
			else:
				error("No existe esa fase.")
			
			
		
		
class MechsSBT:
	"""
		Clase manejadora del fichero mechsJX.sbt
		Cada Mech ocupa 33+n_mechs*2 líneas.
		El Mech jugador ocupa 33+n_mechs*2+93 líneas.
	"""
	def __init__(self,num=0):
		self.nombre = 'mechsSBT'
		self.num = int(num)
		self.jugador = MechJugador(self.num)
		self.mechs = []
		try:
			self.fichero = open('mechsJ'+str(self.num)+'.sbt','r')
		except:
			error("No se ha podido abrir el fichero mechsJ"+str(self.num)+".sbt .")
			
	def leeFichero(self, fase):
		# Leemos el fichero entero.
		lineas = self.fichero.readlines()
		# Comprobamos la cabecera para asegurar que es correcto.
		cabecera = lineas[0]
		#~ print cabecera
		if string.find(cabecera,self.nombre) == -1:
			error("No es un fichero mechsSBT . ")
		else:
			# Obtenemos el nº de mechs.
			self.n_mechs = int(lineas[1])
			
			indice = 2
			# Para todas las fases, llamamos a los lectores de Mechs
			if fase >= 0 and fase < 5:
				cont_mech = 0
				flag = False
				while not flag:
					# Comprobamos si vamos a leer la información del
					# mech jugador o un mech ajeno
					
					#~ log.write("INDICE = "+str(indice))
					#~ log.write("Numero jug = "+str(self.num)+" Numero comp = "+str(lineas[indice]))
					
					if int(self.num) == int(lineas[indice]):
						self.jugador.leeJugador(self.n_mechs,lineas,fase,indice)
						indice += 31+self.n_mechs*2+94
					else:
						rob = Mech(int(lineas[indice]))
						rob.leeMech(self.n_mechs,lineas,fase,indice)
						self.mechs.append(rob)
						indice += 31+self.n_mechs*2
						
					cont_mech += 1
					if cont_mech == self.n_mechs:
						flag = True
			
			self.cierraFichero()
			
	def cierraFichero(self):
		self.fichero.close()



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
		
	def leeMech(self,n_mechs,fichero,indice):
		# Suponemos el indice en la linea con el nº de mech
		sub_indice = indice
		
		# Leemos la información común para todos los mechs
		
		# Si está operativo
		sub_indice+=1
		self.operativo = str2bool(fichero[sub_indice])
		
		sub_indice+=1
		# Si está desconectado
		self.desconectado = str2bool(fichero[sub_indice])
		
		sub_indice+=1
		# Si está atascado
		self.atascado = str2bool(fichero[sub_indice])
		
		sub_indice+=1
		# Si está en el suelo
		self.suelo = str2bool(fichero[sub_indice])
		
		sub_indice+=1
		# El hexágono en el que se encuentra
		self.hexagono = fichero[sub_indice]
		
		sub_indice+=1
		# Lado hacia el que está orientado el Mech
		self.lado = int(fichero[sub_indice])
		
		sub_indice+=1
		# Lado hacia el que está orientado el torso.
		self.lado_torso = int(fichero[sub_indice])
		
		# Temperatura
		sub_indice+=1
		self.temperatura = int(fichero[sub_indice])
		
		sub_indice+=1
		# Si está ardiendo
		self.ardiendo = str2bool(fichero[sub_indice])
		
		sub_indice+=1
		# Si tiene un garrote
		self.garrote = str2bool(fichero[sub_indice])
		
		sub_indice+=1
		# Tipo del garrote
		self.tipo_garrote = int(fichero[sub_indice])
		
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

class MechJugador(Mech):
	"""
		Clase contenedora de la información relevante en la 
		fase de movimiento del mech jugador.
	"""
	def __init__(self,num=0):
		self.nombre = int(num)
	
	def leeJugador(self,n_mechs,fichero,indice):
		# Comprobamos la posición en el fichero
		if int(self.nombre) == int(fichero[indice]):
			# Obtenemos la información común del Mech
			self.leeMech(n_mechs,fichero,indice)
			
			sub_indice = indice + 30
			
			# ANDAR
			sub_indice+=1
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
			self.consciente = str2bool(fichero[sub_indice])
			
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
			sub_indice+=1
			localizacion = []
			for i in range(11):
				localizacion.append(str2bool(fichero[sub_indice+i]))
			self.slots.append(list(localizacion))
			sub_indice+=12
			localizacion = []
			for i in range(5):
				localizacion.append(str2bool(fichero[sub_indice+i]))
			self.slots.append(list(localizacion))
			sub_indice+=6
			localizacion = []
			for i in range(11):
				localizacion.append(str2bool(fichero[sub_indice+i]))
			self.slots.append(list(localizacion))
			sub_indice+=12
			localizacion = []
			for i in range(11):
				localizacion.append(str2bool(fichero[sub_indice+i]))
			self.slots.append(list(localizacion))
			sub_indice+=12
			localizacion = []
			for i in range(5):
				localizacion.append(str2bool(fichero[sub_indice+i]))
			self.slots.append(list(localizacion))
			sub_indice+=6
			localizacion = []
			for i in range(11):
				localizacion.append(str2bool(fichero[sub_indice+i]))
			self.slots.append(list(localizacion))
			sub_indice+=12
			localizacion = []
			for i in range(11):
				localizacion.append(str2bool(fichero[sub_indice+i]))
			self.slots.append(list(localizacion))
			sub_indice+=12
			localizacion = []
			for i in range(5):
				localizacion.append(str2bool(fichero[sub_indice+i]))
			self.slots.append(list(localizacion))
			sub_indice+=6
			
			# Localizaciones desde las que se ha disparado un arma.
			self.localizaciones = []
			for i in range(8):
				self.localizaciones.append(str2bool(fichero[sub_indice+i]))
			sub_indice+=8
			
			# MUNICIÓN para Soltar
			self.soltar_municion = int(fichero[sub_indice])
			#~ print "Municion para soltar = ",self.soltar_municion
			self.municiones = []
			for i in range(self.soltar_municion):
				mun_loc = (str(fichero[sub_indice+1]),int(fichero[sub_indice+2]))
				self.municiones.append(mun_loc)
				indice+=2


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
			
	def leeFichero(self):
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
			#~ if fase >= 0 and fase < 5:
			cont_mech = 0
			flag = False
			while not flag:
				# Comprobamos si vamos a leer la información del
				# mech jugador o un mech ajeno
				
				#~ log.write("INDICE = "+str(indice))
				#~ log.write("Numero jug = "+str(self.num)+" Numero comp = "+str(lineas[indice]))
				
				if int(self.num) == int(lineas[indice]):
					self.jugador.leeJugador(self.n_mechs,lineas,indice)
					indice += 31+self.n_mechs*2+94
				else:
					rob = Mech(int(lineas[indice]))
					rob.leeMech(self.n_mechs,lineas,indice)
					self.mechs.append(rob)
					indice += 31+self.n_mechs*2
					
				cont_mech += 1
				if cont_mech == self.n_mechs:
					flag = True
			
			self.cierraFichero()
			
	def cierraFichero(self):
		self.fichero.close()



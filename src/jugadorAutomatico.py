#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       jugadorAutomatico.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

import sys
import string
from mechsSBT import *
from mapaSBT import *
from configSBT import *
from movimiento import *
from reaccion import *
from finalturno import *
from utils import *
from armas import *

try:
	log = open('log.txt','w')
except:
	raise SystemExit

class JugadorAutomatico:
	def __init__(self, num = 0):
		"""Constructor de la clase JugadorAutomatico"""
		self.jugador = int(num)
		try:
			self.salida_accion = open("accionJ"+str(self.jugador)+".sbt",'w')
		except:
			error("No se ha podido crear el fichero de salida.")
			raise SystemExit
			
	def cierraSalida(self):
		self.salida_accion.close()
		
def _0():
	global log
	log.write("fase movimiento")
	mov = Movimiento(int(sys.argv[1]))
	mov.nextMove()


def _1():
	global log
	log.write("fase reaccion")
	rea = Reaccion(int(sys.argv[1]))
	rea.reacciona()

def _2():
	global log
	acc = Armas(int(sys.argv[1]))
	acc.weaponsAttack()
	print "fin armas"
	log.write("fase At. Armas")
	

def _3():
	global log
	print "AtaqueARmas"
	acc = Armas(int(sys.argv[1]))
	acc.physicalAttack()
	log.write("fase At.fisico")
	

def _4():
	global log
	
	ft = EndTurn(int(sys.argv[1]))
	ft.printAction()
	log.write("fase Final")
	

FASE = { "Movimiento" : _0, "Reaccion" : _1, "AtaqueArmas" : _2,
		"AtaqueFisico" : _3, "FinalTurno" : _4}

def main():
	global player, salida_accion, log
	print "Comienzo Programa"
	# Argumentos
	if len(sys.argv) == 3:
		# Jugador
		if(int(sys.argv[1])>=0):
			num = sys.argv[1]
			# Fase
			if (sys.argv[2] == "Movimiento" or sys.argv[2] == "Reaccion" or sys.argv[2] == "AtaqueArmas" or sys.argv[2] == "AtaqueFisico" or sys.argv[2] == "FinalTurno" ):
				f = sys.argv[2]
			else:
				error("No es una fase de turno válida. (Movimiento, Reaccion, AtaqueArmas, AtaqueFisico, FinalTurno)")
		else:
			error("El numero de jugador debe ser mayor o igual que 0.")
	else:
		print "Numero incorrecto de argumentos:\n"+str(sys.argv[0])+" <jugador> <Fase>"
		error("Numero incorrecto de argumentos:\n"+str(sys.argv[0])+" <jugador> <Fase>")

	# Creamos el jugador
	player = JugadorAutomatico(num)
	# Realizamos las acciones pertinentes para la fase actual
	FASE[f]()
	print "Fin Correcto"
	log.write("Fin correcto")
	# Cerramos los ficheros.
	log.close()
	player.cierraSalida()
	return 0

if __name__ == '__main__':
	main()


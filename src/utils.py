#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       utils.py
#       
#       Copyright 2012 Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

import string

def error(mensaje):
	try:
		log = open('logMap.txt','w')
	except:
		raise SystemExit
	else:
		log.write("ERROR! "+mensaje)
		log.close()
		raise SystemExit

""" Obtiene el valor bool de un string.
	@param s String a procesar.
	@return True/False
"""
def str2bool(s):
	if string.find(s,"True") != -1:
		return True
	elif string.find(s,"False") != -1:
		return False
	else:
		error("Not boolean")

""" Calcula la distancia exacta entre 2 celdas.

	@param c1 Celda 1
	@param c2 Celda 2
	@return distancia
"""
def dist2(c1,c2):
	Vx = abs(c2[0]-c1[0])
	Vy = abs(c2[1]-c1[1])
	if Vy%2 != 0:
		factor = 0
	elif c1[1] < c2[1]: 
		factor = (c1[0]-1)%2
	else:
		factor = (c2[0]-1)%2
	
	return Vx + max(0, Vy- (Vx/2) - factor)

""" Obtiene la orientación relativa entre 2 celdas
	
	@param c1 Celda 1
	@param c2 Celda 2
	@return Cara para orientarse desde c1 a c2
"""
def relative_position(c1, c2):
	valor = -1
	# Fila Norte
	if c1[0] > c2[0]:
		if c1[1] == c2[1]:
			valor = 0
		if c1[1] > c2[1]:
			valor = 5
		if c1[1] < c2[1]:
			valor = 1
	# Fila Sur
	elif c1[0] < c2[0]:
		if c1[1] == c2[1]:
			valor = 3
		if c1[1] > c2[1]:
			valor = 4
		if c1[1] < c2[1]:
			valor = 2
	else:
		if c1[1]+1%2 == 0:
			if c1[1] > c2[1]:
				valor = 5
			else:
				valor = 1
		else:
			if c1[1] > c2[1]:
				valor = 4
			else:
				valor = 2
	return valor

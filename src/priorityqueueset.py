#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       priorityqueset.py
#       
#       Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

import heapq

class PriorityQueueSet(object):
	"""
		Estructura de datos conjunto combinada con cola de prioridad. Se
		comporta como una cola con prioridad garantizando que sus items
		son únicos.
		
		La comprobación de existencia de un item es de orden O(1).
		El borrado del item de menor valor es de orden O(log(n)). Añadir
		un item resulta más costoso y complejo: si no existe, se añade
		con orden O(log(n)); si existe, se compara la prioridad del nuevo
		item en un tiempo de orden O(1), y si el nuevo item es de menor
		prioridad, obtenemos un orden O(n).
	"""
	def __init__(self):
		self.set = {}
		self.heap = []
	
	def __len__(self):
		return len(self.heap)
	
	""" Comprueba si item existe en la ED.
		@param item Objeto a buscar.
		@return True si lo encuentra, False en caso contrario
	"""
	def has_item(self, item):
		return item in self.set

	""" Borra y devuelve el item de menor valor de la ED.
		@return Item de menor valor de la cola.
	"""
	def pop_smallest(self):
		smallest = heapq.heappop(self.heap)
		del self.set[smallest]
		return smallest

	""" Añade item a la cola.
		@param item Item a añadir.
		@return True si el item fue añadido/actualizado
	"""
	def add(self, item):
		if not item in self.set:
			self.set[item] = item
			heapq.heappush(self.heap, item)
			return True
		elif item < self.set[item]:
			for idx, old_item in enumerate(self.heap):
				if old_item == item:
					del self.heap[idx]
					self.heap.append(item)
					heapq.heapify(self.heap)
					self.set[item] = item
					return True
		return False
		

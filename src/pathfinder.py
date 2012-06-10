#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       priorityqueset.py
#       
#       Juan Manuel Rodríguez Trillo <trillop@correo.ugr.es>
#       

from priorityqueueset import PriorityQueueSet

class PathFinder(object):
	""" Calcula un camino en un grafo utilizando el algoritmo A*.
	
		Inicializa el objeto y calcula el camino repetidamente hasta
		encontrar el mejor camino entre un punto de partida (start)
		y uno de llegada (end).
	"""
	def __init__(self, successors, move_cost, heuristic_to_goal):
		""" Constructor del PathFinder.
			successors:
				Función que recibe un punto como argumento y devuelve
				una lista de puntos sucesores pertenecientes al grafo y
				accesibles desde el punto dado.
			 
			move_cost:
				Función que recibe dos puntos como argumentos y devuelve
				el valor del coste del desplazamiento del primero al
				segundo.
				 
			heuristic_to_goal: 
				Función que recibe un punto y un punto objetivo y
				devuelve la estimación heurística del coste de alcanzar
				el objetivo desde el punto.
		"""
		self.successors = successors
		self.move_cost = move_cost
		self.heuristic_to_goal = heuristic_to_goal
	
	""" Calcula el camino entre el punto 'start' y el punto 'goal'.
			
		@param start Punto de partida.
		@param goal Punto objetivo.
		@param movType Tipo de movimiento.
		@param PM Coste máximo.
		
		@return Iterador a los puntos componentes del camino. Si no
				encuentra un camino, devuelve []
	"""
	def compute_path_until_PM(self, start, goal, movType = 0, PM = 7):
		# ======= Algoritmo A* =======
		closed_set = {}
		
		# Nodo inicial
		start_node = self._Node(start.pos, start.face)
		start_node.g_cost = 0
		start_node.f_cost = self._compute_f_cost(start_node, goal)
		
		open_set = PriorityQueueSet()
		open_set.add(start_node)
		
		while len(open_set) > 0:
			# Extrae el nodo con mínimo f_score de open_set
			curr_node = open_set.pop_smallest()
			#~ print curr_node
			# Comprobamos si hemos alcanzado goal y orientamos el valor de face
			#~ print " Comp ",curr_node.coord," Con ",goal.pos
			if curr_node.coord == goal.pos:
				#~ print "Hemos alcanzado GOAL"
				if curr_node.face != goal.face:
					# Corregimos el valor de curr_node.face
					new = self._Node(curr_node.coord, goal.face, curr_node.g_cost+abs(curr_node.face - goal.face) , 0, curr_node)
					# PATH ENCONTRADO
					return self._reconstruct_path_until_PM(new, PM)
				else:
					# PATH ENCONTRADO
					return self._reconstruct_path_until_PM(curr_node, PM)
			
			# Si no es goal, obtenemos los sucesores del nodo.
			closed_set[curr_node] = curr_node
			for succ_coord in self.successors(curr_node.coord,movType, PM):
				succ_node = self._Node(succ_coord)
				# A cada nodo sucesor le calculamos el g_cost y el f_cost
				(succ_node.g_cost, succ_node.face) = self._compute_g_cost(curr_node, succ_node, movType)
				succ_node.f_cost = self._compute_f_cost(succ_node, goal)
				
				if succ_node in closed_set:
					#~ if succ_node.g_cost <= 10:
					#~ print "Sucesor: ",succ_coord,"\nCoste G = ",succ_node.g_cost,"\nCoste F = ",succ_node.f_cost
					continue
				# Añadimos el nodo sucesor a open_set
				if open_set.add(succ_node):
					# Establecemos su predecesor
					#~ if succ_node.g_cost <= 10:
					#~ print "Sucesor: ",succ_coord,"\nCoste G = ",succ_node.g_cost,"\nCoste F = ",succ_node.f_cost
					succ_node.pred = curr_node
		# PATH NO ENCONTRADO
		#~ print "Cjto: ",closed_set.keys()
		#~ print "Path no encontrado"
		#~ return ([], False, 0)
		return self._reconstruct_path_until_PM(curr_node, 1)
	
	def _compute_g_cost(self, from_node, to_node, movType = 0):
		f = Pos(from_node.coord, from_node.face)
		t = Pos(to_node.coord, to_node.face)
		m_c = self.move_cost(f, t, movType)
		return (from_node.g_cost + m_c[0], m_c[1])
	
	def _compute_f_cost(self, node, goal):
		x = Pos(node.coord, node.face)
		return node.g_cost + self._cost_to_goal(x, goal)
	
	def _cost_to_goal(self, node, goal):
		return self.heuristic_to_goal(node, goal)
	
	def _reconstruct_path_until_PM(self, node, PM):
		can = True
		cost = 0
		temp = Pos(node.coord, node.face)
		#~ print "G COST = ",node.g_cost
		if node.g_cost <= PM:
			cost = node.g_cost
			pth = [temp]
		else:
			can = False
			pth =[]
		n = node
		while n.pred:
			n = n.pred
			if n.g_cost <= PM:
				pth.append(Pos(n.coord, n.face))
				if n.g_cost > cost:
					cost = n.g_cost
					can = True
		#~ print (list(reversed(pth)), can, cost)
		return (list(reversed(pth)), can, cost)
	
	""" Abstracción de un nodo para la búsqueda A* en un grafo.
		
		Cada nodo tiene:
			- coord Coordenadas del punto que representa.
			- g_cost Coste acumulado de alcanzar el nodo desde el origen.
			- f_cost Coste estimado de alcanzar el objetivo desde el
					origen pasando por este nodo.
			- pred Nodo predecesor (Excepto el nodo inicial)
			- face Orientación en el nodo (Inicialmente Norte)
		
		Nota:
		Esta clase está diseñada para ser utilizada junto con la clase
		PriorityQueueSet, por lo que implementa las funciones necesarias
		que operan según nuestro objetivo.
	"""
	class _Node(object):
		def __init__(self, coord, face = 0, g_cost=None, f_cost=None, pred=None):
			self.coord = coord
			self.g_cost = g_cost
			self.f_cost = f_cost
			self.pred = pred
			self.face = face
		
		def __eq__(self, other):
			return self.coord == other.coord
		
		def __cmp__(self, other):
			return cmp(self.f_cost, other.f_cost)
		
		def __hash__(self):
			return hash(self.coord)
		
		def __str__(self):
			return 'N(%s) -> g: %s, f: %s' % (self.coord, self.g_cost, self.f_cost)
		
		def __repr__(self):
			return self.__str__()

""" Abstracción de una posición orientada.
"""
class Pos(object):
	def __init__(self, pos, face=0):
		self.pos = pos
		self.face = face 
	
	def printPos (self):
		if (self.pos[1]+1 <= 9): x = "0"+str(self.pos[1]+1)
		else: x = str(self.pos[1]+1)
		if (self.pos[0]+1 <= 9): y = "0"+str(self.pos[0]+1)
		else: y = str(self.pos[0]+1)
		return x+y
	
	def printFace (self):
		return self.face+1
	
	def __eq__(self, other):
		return (self.pos == other.pos) and (self.face == other.face)
	
	def __cmp__(self, other):
		return cmp(self.face, other.face)
	
	def __hash__(self): 
		return hash(self.pos)
	
	def __str__(self):
		return 'N(%s, %s) -> face: %s' % (self.pos[1]+1, self.pos[0]+1, self.face+1)
	
	def __repr__(self):
		return self.__str__()


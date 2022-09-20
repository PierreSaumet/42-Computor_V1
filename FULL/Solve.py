#! /usr/bin/env python3
# -*- coding: UTF-8 -*-


#####################################
# Programme Python 3 Type           #
# Autor: Pierre Saumet, Paris, 2022 #
# Licence: GPL                      #
#####################################

#####################################
# Informations:
"""
	This is a program created with Python3.
	It respects the rules of PEP 8.
	Everythings is in English.
	Python rocks.
"""

import math

class Solve:
	" Solve class: manage parsing data from the given argument "
	def __init__(self, X, Y):
		self.X = X
		self.Y = Y
	
	def reducedForm(self):
		print("test 4x +2 = -1")
		print("result = {}".format(self.solveEquationOneDegree(4, 2, -1)))

		print("test x^2 + 2x + 1 = 0")
		print("result = {}".format(self.solveEquationTwoDegree(1, 2, 1)))


	"""
		Solution for Equation with 1 degree
		Form: mx + p = c
		With m != 0:
			( c - p ) / m
		2x + 1 = 0
			(0 - 1 ) / 2
			-1 / 2
	"""
	def solveEquationOneDegree(self, m, p, c):
		return (c - p) / m
	

	"""
		Solution for Equation with 2 degrees
			if delta < 0 == no solution
			if delta = 0 == one solution
			if delta > 0 == 2 solutions
	"""
	def solveEquationTwoDegree(self, a, b, c):
		delta = self.calculateDelta(a, b, c)
		if delta > 0:
			squareDelta = math.sqrt(delta)
			ret = [(-b - squareDelta) / (2 * a), (-b + squareDelta) / (2 * a)]
		elif delta < 0:
			ret = []
		else:
			ret = [-b / (2 * a)]
		return ret


	"""
		Calculate Delta = b^2 - 4ac
		example:
			x^2 + 2x + 1 = 0
			delta 	= b^2 - 4ac
					= 2 * 2  - 4 * 1 * 1
					= 0
			
	"""
	def calculateDelta(self, a, b, c):
		return b * b - 4 * a *c
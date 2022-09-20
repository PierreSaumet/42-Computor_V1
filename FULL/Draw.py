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

import matplotlib.pyplot as plt
import numpy as np

class Draw:
	" Draw class: drawing data "
	def __init__(self):
		self.X = "test"

	def drawing_result(self):
		print("Test 1 degree")

		x = np.linspace(-10, 10, 20)
		# y = np.linspace(-10, 10, 100)
		y = x**2 + 4

		Y = "x^2 + 2"
		fig = plt.figure("Result of : {}".format(Y))
		# ax = fig.add_subplot(1, 1, 1)
		# ax.spines['left'].set_position('center')
		# ax.spines['bottom'].set_position('zero')
		# ax.spines['right'].set_color('none')
		# ax.spines['top'].set_color('none')
		# ax.xaxis.set_ticks_position('bottom')
		# ax.yaxis.set_ticks_position('left')

		plt.plot(x, y, 'r')

		# show the plot
		plt.show()



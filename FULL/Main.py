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

import sys
import Error
import Parsing
import Solve
import Draw

class Main:
	" Main program "
	def __init__(self, given_argv):
		# Access to the class nameed Error()
		self.error = Error.Error()
		# Access to the class nameed Parsing()
		self.parsing = Parsing.Parsing()
		# Access to the class nameed Solve()
		self.solve = Solve.Solve(4, 3)
		# Access to the class nameed ()
		self.draw = Draw.Draw()
		# The given argument
		self.argument = given_argv


	def ft_no_arg(self):
		equation = input("Enter your equation: ")
		print(equation)

	def main(self):
		if len(self.argument) == 1:
			self.ft_no_arg()
		elif len(self.argument) > 2:
			self.error.display_error("Too many arguments.")
		else:
			self.parsing.start_parsing(self.argument[1]) # a faire
			# self.solve.reducedForm()
			# self.draw.drawing_result()
			


if __name__ == "__main__":
	pgm = Main(sys.argv)
	pgm.main()
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

class Error:
	" Error class: manage errors "
	def __init__(self):
		self.err_nbr = 0
		self.err_msg = ""
	
	def display_error(self, err_msg = ""):
		print("\033[91m{0}\033[00m {1}".format("ERROR: ", err_msg))
		exit()

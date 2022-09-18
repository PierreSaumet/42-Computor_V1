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

from ast import arg
from operator import length_hint
from symbol import argument
import Error


class Parsing:
	" Parsing class: manage parsing data from the given argument "
	def __init__(self):
		self.authorized_char = "0123456789 .*-+=^xX"
		self.error = Error.Error()
		self.A_part = ""
		self.B_part = ""
		
	
	def start_parsing(self, argument):
		print("Debut du parsing ... :\n")
		print(argument)
		for i in range(len(argument)):
			for y in range(len(self.authorized_char)):
				if argument[i] not in self.authorized_char:
					self.error.display_error(" Non authorized character: " + argument[i])
		
		self.count_symbol(argument)
		self.separate_data(argument)
		# print("A = {}".format(self.A_part))
		# print("B = {}".format(self.B_part))
		self.clean_data(self.A_part)
		
	def count_symbol(self, argument):
		count_equal = 0
		for i in range(len(argument)):
			if argument[i] == '=':
				count_equal += 1
				if count_equal > 1:
					self.error.display_error(" Too many equal signe: '='")
		if count_equal == 0:
			self.error.display_error(" You need an equation with '='")
	
	def separate_data(self, argument):
		self.A_part = argument.split("=", 1)
		self.B_part = self.A_part[1]
		self.A_part = self.A_part[0]

	def clean_data(self, argument):
		# Check if second degree
		second_data = ""
		first_data = ""
		constante = ""
		for i in range(len(argument)):
			if argument[i] == '^':
				if argument[i + 1] == '2':
					print("on a un x carre = argument = " + argument + " et i = {}".format(i))
					self.get_second_x(argument, i)
					# {}".format(self.get_second_x(argument, i)))

	
	def get_second_x(self, argument, i):
		length = len(argument)
		print("lenght = {}".format(length))
		print("arg = " + argument)
		if argument[i - 1] not in "xX":
			self.error.display_error(" a '^' character is always after 'x' or 'X': " + argument[i - 1])
		if argument[i + 1] not in "012":
			self.error.display_error(" Non authorized character after '^', only 0/1/2: " + argument[i + 1])
		if argument[i + 2] not in " +-=":
			self.error.display_error(" Non authorized character after '^', only -/+/ /=: " + argument[i + 2])
		y = i - 2
		while argument[y] != ' ':
			y -= 1
		z = i + 2
		tmp = argument[y:i + 2]
		self.clean_second_x(tmp)
		# return argument[y:i + 2]

	def clean_second_x(self, argument):
		new_str = argument.replace('x', 'X')
		print("transfor m= " + new_str)
		x = new_str.find("X")
		if new_str[x - 1] not in  ' *':
			new_str = new_str[:x] + ' ' + new_str[x:]
		print("transfor m= " + new_str)
		
		
		// later
		# x = new_str.find('*')
		# if x != -1:
		# 	if argument[x + 1] != ' ':
		# 		new_str = new_str[:x] + ' ' + new_str[x:]
		# 	# if argument[x - 1] != ' ':
		# 	# 	new_str = new_str[:x] + ' ' + new_str[x:]
		print("transfor m= " + new_str)

		


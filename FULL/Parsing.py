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
		
		self.check_equal(argument)
		self.clean_data(self.A_part)

	# Check if there is one '=' sign and split the data into two groups.	
	def check_equal(self, argument):
		if argument.count('=') > 1 or argument.count('=') == 0: # need to be change
			self.error.display_error(" Too many or not enough equal sign: '='")
		self.A_part = argument.split("=", 1)
		self.B_part = self.A_part[1]
		self.A_part = self.A_part[0]

	# Execute basic check, start with ... end with ...
	def basic_check(self, data):
		data = data.replace('x', 'X')
		data = data.replace(' ', '')
		if data[0] in '+^*':
			self.error.display_error(" Cannot start with: " + data[0])
		if data[len(data) - 1] in "+-*^":
			self.error.display_error(" Cannot end with: " + data[len(data) - 1])
		print("len de data = {}".format(len(data)))
		for i in range(len(data)):
			# print("i = {}".format(i))
			if data[i] in "-+*.^" and i + 1 < len(data) and data[i + 1] in "-+*^.":
				self.error.display_error(" After a '+/-/*/./^', cannot have: " + data[i + 1])
			if data[i] == '^' and i + 1 < len(data) and  data[i + 1] not in "012":
				self.error.display_error(" After a '^', cannot have: " + data[i + 1])
			if data[i] == '*' and i + 1 < len(data) and data[i + 1] != 'X':
				self.error.display_error(" After a '*' can only have 'x/X, not a: " + data[i + 1])
			if data[i] == "X" and i + 1 < len(data)  and data[i + 1] not in "^+-":
				self.error.display_error(" After a 'X' can only have '^' or '+/-', not a: " + data[i + 1])
			if data[i] == '.' and i + 1 >= len(data):
				self.error.display_error(" After a '.' it should have number.")
		return data

	def empty_number(self ,data):
		# print("Dans empty number = " + data)

		lst_data = data.split()
		# print("lst_data = {}".format(lst_data))
		for i in range(len(lst_data)):
			# print("lst_data i = {}".format(lst_data[i]))
			for y in range(len(lst_data[i])):
				if y == 0 and lst_data[i][y] not in "+-":
					if i > 0:
						if lst_data[i-1][len(lst_data[i -1])- 1] not in "+-":
							print("ERROR ?avec {0} car avant {1}".format(lst_data[i], lst_data[i-1]))
							self.error.display_error(" Number should start with '+ or -'")


		

	def clean_data(self, data):
		print("\nDans clean data: ...")
		
		# trouver si chiffes seuls ex 3 3 + 4x  == erreur
		self.empty_number(data)

		
		print("Data = " + data)
		new_str = self.basic_check(data)

		print("new string 1 =-" + new_str + "-")

		tmp = ""
		equations = list()
		for i in range(len(new_str)):
			if new_str[i] in "+-":
				print("TMP = " + tmp)
				if len(tmp) > 0:
					equations.append(tmp)
				tmp = ''
			tmp = tmp + new_str[i]
		print(" fin TMP = " + tmp)
		equations.append(tmp)
		print("test equations = {}".format(equations))
		exit()
				

	def check_second_degree(self, data, i):
		print("Dans check Second Degree...")
		print(data, i)
		lengh_data = len(data)
		print("alors longueur de data = {0} et i = {1}".format(lengh_data, i))
		print("-{}-  data[i] = {}".format(data, data[i]))
		if i + 2 > lengh_data:
			self.error.display_error("Error with the second degree: " + data)
		if i + 2 < lengh_data:
			if data[i + 2] not in " +-=":
				self.error.display_error(" Non authorized character after '^2', only -/+/ /=: " + data[i + 2])

		print("\t GOOD")

# 4x2 +3x +2x^2
	
	def get_second_x(self, argument, i):
		length = len(argument)
		print("lenght = {}".format(length))
		print("arg = " + argument)
		if argument[i - 1] not in "xX":
			self.error.display_error(" a '^' character is always after 'x' or 'X': " + argument[i - 1])
		if argument[i + 1] not in "012": # useless
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

		print("transfor m= " + new_str)
		print("transfor m= " + new_str)

		


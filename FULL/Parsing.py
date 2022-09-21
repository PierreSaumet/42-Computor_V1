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
		
		self.check_equal_symbole(argument)
		
		two_degree = list()
		one_degree = list()
		no_deg = list()
		equations = self.clean_data(self.A_part)
		# trier si second premier ou rien degree
		for item in equations:
			# print(item)s
			if item.find("X^2") > 0:
				# print("SECOND DEGREE = " + item)
				two_degree.append(item)
			elif item.find("X^1") > 0:
				# print("X ^ 1")
				one_degree.append(item)
			elif item.find("X^0") > 0:
				# print("X^ 0 donc 0")
				# if item.find("*X") >0 :
				# 	data = item.replace("X^0", "1")
				# else:
				# 	data = item.replace("X^0", "*1")
				no_deg.append(item)
			elif item.find("X") > 0:
				# print("X")
				one_degree.append(item)
			else:
				# print("autre ? = "+ item)
				no_deg.append(item)
		print("\n\n TOTAL LEN = {}".format(len(equations)))
		print("second list = {0} et len = {1}".format(two_degree, len(two_degree)))
		print("one_degree list = {0} et len = {1}".format(one_degree, len(one_degree)))
		print("no_deg list = {0} et len = {1}".format(no_deg, len(no_deg)))

		self.calculate_no_degree(no_deg)
		self.calculate_one_degree(one_degree)
	

	def calculate_one_degree(self, data):
		print("\n\ndata = {}".format(data))
		new_data = list()
		is_float = 0
		for i in range(len(data)):
			if data[i].find(".") > 0:
				is_float += 1
			if data[i].find("*") > 0:
				new_data.append(data[i][:data[i].find("*")])
			elif data[i].find("X") > 0:
				new_data.append(data[i][:data[i].find("X")])
			else:
				new_data.append(data[i])
		print("nwe data = {}".format(new_data))

		# check if float
		# print("float ? ", is_float)
		if is_float > 0:
			result = 0.0
			for i in range(len(new_data)):
				result += float(new_data[i])
		else:
			result = 0
			for i in range(len(new_data)):
				result += int(new_data[i])
		print("RESULT = ", result)
		new_str = str(result)
		if result > 0:
			new_str = "+ " + new_str + " * X"
		print("FINAL = " + new_str)


	def calculate_no_degree(self, data):
		print("data = {}".format(data))
		new_data = list()
		is_float = 0
		for i in range(len(data)):
			if data[i].find(".") > 0:
				is_float += 1
			if data[i].find("X^0") > 0:
				new_data.append(data[i][:data[i].find("X^0")])
			else:
				new_data.append(data[i])
			# print("new data = {}".format(new_data))
		
		# check if float
		print("float ? ", is_float)
		if is_float > 0:
			result = 0.0
			for i in range(len(new_data)):
				result += float(new_data[i])
		else:
			result = 0
			for i in range(len(new_data)):
				result += int(new_data[i])
		print("RESULT = ", result)
		new_str = str(result)
			


	"""
		This function checks the number of '='.
			If there is more than 1:
				It display an error message.
			Otherwise, it separate the equation in two part
	"""
	def check_equal_symbole(self, argument):
		if argument.count('=') > 1:
			self.error.display_error(" Too many or not enough equal sign: '='")
		if argument.count('=') == 1:
			self.A_part = argument.split("=", 1)
			self.B_part = self.A_part[1]
			self.A_part = self.A_part[0]
		else:
			self.A_part = argument
			self.B_part = "0"


	"""
		This function checks several points:
			-	It replaces all 'x' item by 'X'.
			-	It replaces all spaces by nothing
			-	Checks the beginning and the end if there is no wrong symbol
			-	Checks all symbols and their corresponding values
				Ex:
					2..3 / 2. / 2X^^3  ==> wrong
					Display an error.
		Return the "data" if everything is Okay.
	"""
	def basic_check(self, data):
		data = data.replace('x', 'X')
		data = data.replace(' ', '')
		if data[0] in '^*':
			self.error.display_error(" Cannot start with: " + data[0])
		if data[len(data) - 1] in "+-*^":
			self.error.display_error(" Cannot end with: " + data[len(data) - 1])
		for i in range(len(data)):
			if data[i] in "-+*.^" and i + 1 < len(data) and data[i + 1] in "-+*^.":
				self.error.display_error(" After a '+/-/*/./^', cannot have: " + data[i + 1])
			if data[i] == '^' and i + 1 < len(data) and  data[i + 1] not in "0123456789":
				self.error.display_error(" After a '^', cannot have: " + data[i + 1])
			if data[i] == '*' and i + 1 < len(data) and data[i + 1] != 'X':
				self.error.display_error(" After a '*' can only have 'x/X, not a: " + data[i + 1])
			if data[i] == "X" and i + 1 < len(data)  and data[i + 1] not in "^+-":
				self.error.display_error(" After a 'X' can only have '^' or '+/-', not a: " + data[i + 1])
			if data[i] == '.' and i + 1 >= len(data):
				self.error.display_error(" After a '.' it should have number.")
		return data

	"""
		This function splts "data" with spaces. Then, it checks that there
		is no single number without a sign symbol like "+ or -".
			Ex: 4x + 3  2 = 0  ==> Error, 2 is alone
		It displays an error if there is a problem.
		Othrewise return nothing
	"""
	def empty_number(self ,data):
		lst_data = data.split()
		for i in range(len(lst_data)):
			for y in range(len(lst_data[i])):
				if y == 0 and lst_data[i][y] not in "+-":
					if i > 0:
						if lst_data[i-1][len(lst_data[i -1])- 1] not in "+-":
							print("ERROR ?avec {0} car avant {1}".format(lst_data[i], lst_data[i-1]))
							self.error.display_error(" Number should start with '+ or -'")

	def clean_data(self, data):
		print("\nDans clean data: ...")
		
		self.empty_number(data)
		new_str = self.basic_check(data)
		print("new string 1 =-" + new_str + "-")
		exit()
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
		return equations
		
				

	def check_two_degreeree(self, data, i):
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

		


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

def     ft_error(err_nbr):
    if err_nbr == 0:
        print("Error: too many arguments\n")
        exit()
    elif err_nbr == 1:
        print("Error: you need 2 arguments, for example: \t python3 program.py '4x^2 + 2x + 1 = 0'\n")
        exit()
    elif err_nbr == 2:
        print("Error: symbole not authorize\n")
        exit()
    elif err_nbr == 3:
        print("Error: too many '='\n")
        exit()

def     ft_program(argv_brut):
    print("Argument given = {}".format(argv_brut))
    ft_check_argv(argv_brut)


def ft_get_first_second_part(argv_brut):
    print(argv_brut)

def ft_check_symbol(argv_brut):
    count_equal = 0
    for i in range(len(argv_brut)):
        if argv_brut[i] == '=':
            count_equal += 1
            if count_equal > 1:
                ft_error(3)
            else:
                ft_get_first_second_part(argv_brut)

# Main function to check the given argument
def     ft_check_argv(argv_brut):
    
    for i in range(len(argv_brut)):
        if argv_brut[i].isspace():
            continue
        elif argv_brut[i].isnumeric():
            continue
        elif argv_brut[i] == '+' or argv_brut[i] == '-' or argv_brut[i] == '=' or argv_brut[i] == '^':
            ft_check_symbol(argv_brut)
            continue
        else:
            if argv_brut[i] != 'x' and argv_brut[i] != 'X' and argv_brut[i] != '.':
                ft_error(2)
    print("Parsing OK!\n")       


def ft_display_solution(truc):
    print("Reduced form: {}".format(truc))
    print("Polynomial degree: {}".format(truc))
    print("The solution is: {}".format(truc))
    print(truc)
    

if __name__ == "__main__":
    # print(sys.argv)
    # print(len(sys.argv))

    if len(sys.argv) > 2:
        ft_error(0)
    elif len(sys.argv) == 1:
        ft_error(1)
    else:
        ft_program(sys.argv[1])
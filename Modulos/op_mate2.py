#!/usr/bin/python311

"""
El modulo hace operaciones matematicas algo avanzadas
"""

__author__ = "Alvaro"
__copyright__ = "Copy 2023"
__credits__ = "GDSC"

__license__ = "GPL"
__version__ = "1,0"
__mantainer__ = "Alvaor Peña"
__email__ = "alvaro@gmail.com"
__status__ = "Develop"


def division(num1, num2):
    """Regresa la divsion de dos numeros"""
    return num1/num2

def exponente(num1, num2):
    """Regresa el exponente de un numero"""
    return num1 ** num2

x = 12
y = 20

__all__ = ["division", "exponente", "x", "y"]
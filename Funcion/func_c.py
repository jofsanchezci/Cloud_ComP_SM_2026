#func_c.py
import math


def suma(x,y):
	return x+y

def resta(x,y):
	return x-y

def mul(x,y):
	return x*y 

def div(x,y):
	if y==0:
		return 'ERROR Div/0'
	else:
		return x/y 

def seno(x):
	return math.sin(x)
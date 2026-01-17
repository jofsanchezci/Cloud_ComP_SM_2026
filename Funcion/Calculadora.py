#Calculadora.py
from func_c import suma,resta, mul, div, seno
x,y=input('Ingrese los numeros a calcular: ' ).split()
x=float(x)
y=float(y)

print(suma(x,y))
print(resta(x,y))
print(mul(x,y))
print(div(x,y))
print(seno(x))
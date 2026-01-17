#Funcion.py
#Como graficar una función lineal
import matplotlib.pyplot as plt
import math

def linea(x):
	return x

def cuadrado(x):
	return x**2

def seno(x):
	return math.sin(x)

#for i in range(-5,6):
#	print(linea(i))

#for i in range(-5,6):
#	print(cuadrado(i))

#x es el dominio (Listas)
#y el rango

x=[]
y=[]

# for i in range(-5,6):
# 	x.append(i)
# 	y.append(cuadrado(i))

# plt.plot(x,y)
# plt.grid()
# plt.title('Grafica de una función')
# plt.show()

#Grafica de Sin(x)
cont=-6
while cont <=6:
	x.append(cont)
	y.append(seno(cont))
	cont+=0.1

print(len(x))
plt.plot(x,y)
plt.grid()
plt.title('Grafica de una función')
plt.show()


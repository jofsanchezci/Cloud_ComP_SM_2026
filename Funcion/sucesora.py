#sucesora.py
def s(x):
	return x+1

#print(s(3))

def suma(a, b):
    resultado = a
    for _ in range(b):
        resultado = s(resultado)
    return resultado

print('La suma es: ', suma(10,3))
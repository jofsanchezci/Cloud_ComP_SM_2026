#primo.py
n=int(input('Ingrese el numero: '))
if n<0:
	print('ERROR, el numero debe ser mayor a Cero')
else:
	cont=0
	for i in range(1,n+1):
		if n%i==0:
			cont+=1

	if cont==2:
		print('El numero', n, 'es primo')
	else:
		print('El numero', n, 'NO es primo')


n=int(input('Ingrese un numero: '))
cont=1
if n < 0:
	print('ERROR')
elif n==0 or n==1:
	print(1)
else:
		for i in range(1,n+1):
			cont*=i
		print('El facorial de', n, 'es: ', cont)
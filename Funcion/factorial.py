#factorial.py
#n!
#Ejemplo 3!=1*2*3
#4!= 4*3!
#5!=5*4*3*2*1
#Factorial Iterativo
def facto(n):
	if n<0:
		return 'ERROR'
	elif n==0 or n==1:
		return 1
	else:
		return n*facto(n-1)






n=int(input('Ingrese un numero: '))
# cont=1
# if n < 0:
# 	print('ERROR')
# elif n==0 or n==1:
# 	print(1)
# else:
# 		for i in range(1,n+1):
# 			cont*=i
# 		print('El facorial de', n, 'es: ', cont)  

print('El factorial de ', n, 'es: ',   facto(n))



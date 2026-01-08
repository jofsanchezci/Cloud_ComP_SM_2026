#funcioP.py
def primo(n):
	if n<0:
		return'ERROR'
	else:
		cont=0
		for i in range(1,n+1):
			if n%i==0:
				cont+=1

		if cont==2:
			return 1
			 
		else:
			return 0

#n=int(input('Ingrese el numero: '))
for i in range(1,101):
	if primo(i)==1:
		print(i)

n = int(input('Enter an integer: '))
print ('The divisors of the numbers  are: ')
for i in range (1, n+1):
	if( n % i == 0):
		print(i)
num = int(input('Enter any two numbers to star '))
a = int(input())
b = int(input('Fibonnaci number to generated:'))
list = [num,a]
for x in range(0,b,1):
	list.append(list[x]+list[x+1])
print(list)
a = [1,5,7,8,10,12,23,25,60,89]
b = int(input("enter number: "))
c = []
for i in a:
	if i < b:
		c.append(i)
print(c)
import sys
number = int(input("Please enter a number" + "\n" ))
prime = False 
if number > 0:
    for x in range (2, number - 1): 
        if number % x != 0: 
            continue 
        elif number % x == 0: 
            sys.exit("The number is not prime.")
    sys.exit("The number is prime.") 
    sys.exit("The number is not prime.") 
else:
    sys.exit("The number is not prime.")
import random
num = random.randint(1,9)
count = 0
guess = input('Enter your number between 1 to 9:')
guess = int(guess)
while guess!= num and guess!='exit':
	guess = int(guess)
	count+=1
	if guess > num:
		guess = input('Number is less than you have guessed')
	elif guess < num:
		guess = input('Number is bigger than you have guessed')
if guess == num:
	print('voilla! Number you have guessed is ' +str(count))
else :
	print('Try again ')
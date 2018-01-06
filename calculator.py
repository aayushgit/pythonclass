def calculate():
	operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
	while True:
		try:
			number_1 = int( input('Enter your first number:'))
			number_2 = int(input('Enter your second number:'))
			break
		except ValueError:
			print("Not a Vlid Integer Sire!")
	if operation == '+':
		#addition
		print('{} + {} =  '.format(number_1, number_2))
		print(number_1 + number_2)
	elif operation == '-':
		#subtraction
		print('{} - {} =  '.format(number_1, number_2))
		print(number_1 - number_2)
	elif operation == '*':
		#multiplication
		print('{} * {} =  '.format(number_1, number_2))
		print(number_1 * number_2)
	elif operation == '/':
		#division
		print('{} / {} =  '.format(number_1, number_2)) 
		print(number_1 / number_2)
	else:
		print("Please Enter a Valid Operation. +, -, * or /")

#A function to calculate again
def again():
	calc_again = input('''
	Do you want to calculate again?
	Type Y for YES and N for NO.
	''')
	#If user types Y, run again
	if calc_again.upper() == 'Y':
		calculate()
	elif calc_again.upper() == 'N':
		print('Its like your loss man')
	else:
		again()
#The Welcome Function
def welcome():
	print('''
	Welcome to the Calculator Man!
	Its like I do calculations kind of thing.
	''')

#Call the Welcome
welcome()
#Call the function to calculate
calculate()

#Call the again function
again()

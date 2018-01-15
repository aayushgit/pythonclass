#interpreter:python3
string= input ("Please Enter a Word:\t")
if string in open('pos.txt').read():
	print('Positive')

elif string in open('neg.txt').read():
	print('Negative')

else:
	print('Ins\'t positive or negative')

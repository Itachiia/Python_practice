from random import uniform as U 
Y = float( round( U(1,5), 1 ) )

print("Fangfang, Please input your number :")

for i in range(7) :
	x = float (input())
	if x > Y :
		print("It's bigger than your number, please input again :")
	elif x < Y :
		print("It's smaller than your number, please input again :")
	else :
		print("You are right")
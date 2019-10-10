import turtle

q = turtle.pen()
turtle.bgcolor('white')
sides = 7
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
for x in range (360) :
	turtle.pencolor(colors[x%sides])
	turtle.forward(x * 3 / sides + x)
	turtle.left(360 / sides + 1)
	turtle.width(x * sides / 200 )
	turtle.speed (x + 1)
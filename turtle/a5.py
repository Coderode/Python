import turtle
d=turtle.Turtle()
d.speed(0)
d.getscreen().bgcolor("#994444")

#simple star
# def star(turtle):
# 	for i in range(5):
# 		turtle.forward(50)
# 		turtle.left(216)  #angle =216 for 5 tip star
d.penup()
d.goto(-160,40)
d.pendown()

def star(turtle,size):
	if size <= 10:
		return
	else:
		for i in range(5):
			turtle.forward(size)
			star(turtle,size/3)  #recursive function
			turtle.left(216)


star(d,300)
d.hideturtle()
turtle.done()
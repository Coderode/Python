import turtle
import math
c=turtle.Turtle()
c.speed(0)
c.color("red","yellow")
c.begin_fill()
c.setposition(0,0)


for i in range(2000):
	# c.forward(math.sqrt(i))
	# c.left(i%180)
	
	c.forward(10)
	c.left(math.sin(i/10)*25)
	c.left(20)




c.end_fill()
c.hideturtle()
turtle.done()  #to stop turtle window
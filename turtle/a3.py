import turtle
c=turtle.Turtle()
c.speed(0)
c.color("red","yellow")
c.begin_fill()
c.setposition(-150,0)
for i in range(200):
	c.forward(400)
	c.left(168.5)
c.end_fill()
c.hideturtle()
turtle.done()  #to stop turtle window
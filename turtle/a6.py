import turtle
t=turtle.Turtle()
list1=["purple","red","orange","blue","green"]
t.speed(0)
for i in range(250):
	t.color(list1[i%5])
	t.pensize(i/10+1)
	t.forward(i)
	t.left(59)
turtle.done()
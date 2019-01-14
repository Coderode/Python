import turtle
b=turtle.Turtle()
#square
b.speed(0)  #to increase or decrease the speed of cursor 0-fastest  10-fast
b.color("red","cyan")  #(outline color,interior color)
b.begin_fill()
b.pensize(10)  #width of cursor
def square():
	for i in range(4):
		b.forward(100)
		b.left(90)
square()
b.end_fill()
b.color("#1C9C0E","#E0FD22")  #hex color code from net
b.begin_fill()
b.right(90)
b.penup()  #not to wright on the screen
b.forward(50)
b.pendown() #to wright on the screen
square()
b.end_fill()
b.hideturtle()
turtle.done()

#to know more functions of turtle goto python documentation tutle module
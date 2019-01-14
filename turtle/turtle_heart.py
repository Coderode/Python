import turtle
t=turtle.Turtle()
turtle.title("Heart shape")  
screen=turtle.Screen()
screen.bgcolor("black")
t.color("red")
t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(140)
t.circle(-70,200)  #-ve for anticlockwise(radius=70 bits) circle upto 200 degree
#t.left(120)
t.setheading(60) #above and this line do the same thing
t.circle(-70,200)  #forward=2*circle(radius)
t.forward(140)
t.end_fill()
t.hideturtle()
#heart shape in 4 parts
#set heading -set the angle of the turtle at that degree from > side
#according to main point of that turtle

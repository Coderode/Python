import turtle
t=turtle.Turtle()
list1=["yellow","red","blue","green"]
t.up()  #penup
t.goto(200,0)
#4 circles
# for i in range(4):
# 	t.down() #pendown
# 	t.begin_fill()
# 	t.fillcolor(list1[i])
# 	t.circle(50)
# 	t.end_fill()
# 	t.up()
# 	t.bk(100)  #move backward


for i in range(4):
	t.down()
	t.color(list1[i])
	t.pensize(20)
	t.circle(100)
	t.up()
	t.bk(100)
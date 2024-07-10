import turtle
#square1
drawing_board=turtle.Screen()
drawing_board.bgcolor("#C133FF")
drawing_board.title("Python Turtle")
turtle_instance=turtle.Turtle()

turtle_instance.forward(100)
turtle_instance2=turtle.Turtle()
turtle_instance2.left(90)
turtle_instance2.forward(100)
turtle_instance2.right(90)
turtle_instance2.forward(100)
turtle_instance2.right(90)
turtle_instance2.forward(100)
turtle.done()

'''
#square2
turtle_instance=turtle.Turtle()

for i in range (4):
    turtle_instance.forward(200)
    turtle_instance.left(90)

turtle.done()
'''
'''
#star
turtle_instance=turtle.Turtle()
turtle_instance.left(45)
turtle_instance.forward(200)
turtle_instance.right(90)
turtle_instance.forward(200)
turtle_instance.right(160)
turtle_instance.forward(300)
turtle_instance.right(160)
turtle_instance.forward(300)
turtle_instance.right(160)
turtle_instance.forward(300)
'''
'''
#star2
turtle_instance=turtle.Turtle()
for i in range (5):
 turtle_instance.left(144)
 turtle_instance.forward(200)
turtle.done()
'''
'''
#polygon
turtle_instance=turtle.Turtle()
num_sides=6
angle=360.0/num_sides
side_length=100

for i in range (num_sides):
 turtle_instance.left(angle)
 turtle_instance.forward(side_length)
turtle.done()
'''



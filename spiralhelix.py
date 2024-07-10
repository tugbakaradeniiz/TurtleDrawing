import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Python Turtle")

turtle_instance=turtle.Turtle()
turtle_instance.color("purple")
turtle.speed(0)  #Çizim hızını ayarlar.
turtle_colors=["red","purple","blue","green","orange","yellow"]

for i in range(6):
 turtle_instance.color(turtle_colors[i])
 turtle_instance.circle(10*i)
 turtle_instance.circle(-10*i)
 turtle_instance.left(i)

turtle.mainloop()
#turtle.done()
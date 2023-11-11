from turtle import *

# we want to paint a house a1

speed(10)

width(8)
color("blue")
begin_fill()
forward(150)
left(90)

forward(150)
left(90)

forward(150)
left(90)

forward(150)
left(90)

end_fill()

#drawing a door

forward(55)
color("brown")
begin_fill()
left(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
end_fill()
 
penup()
goto(150,150)
pendown()

#drawing a roof

color("red")
begin_fill()
right(150)
forward(150)
left(120)
forward(150)
end_fill()

penup()
goto(15,85)
pendown()

#drawing windows

color("cyan")
begin_fill()
right(150)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(135,85)
pendown()

color("cyan")
begin_fill()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

exitonclick()
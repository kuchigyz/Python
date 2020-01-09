import turtle
turtle.speed(0) 
turtle.hideturtle()

#Sin kvadrat
turtle.color('blue')
turtle.right(45)
turtle.begin_fill()
turtle.circle(54, 360, 4)
turtle.end_fill()

#Prazen Shestoygylnik
turtle.penup()
turtle.goto(-20, -100)
turtle.pendown()
turtle.right(45)
turtle.color('black')
turtle.circle(60, 360, 6)


''' Kakvo az bih napisal:

import turtle
turtle.speed(0) 
turtle.hideturtle()

def DrawSquare(color):
  turtle.penup()
  turtle.goto(-38, 21)
  turtle.pendown()
  turtle.color(color)
  turtle.right(45)
  turtle.begin_fill()
  turtle.circle(54, 360, 4)
  turtle.end_fill()
  turtle.left(45)
def DrawHexagon(color):
  turtle.penup()
  turtle.goto(0, 0)
  turtle.pendown()
  turtle.color(color)
  turtle.begin_fill()
  turtle.circle(60, 360, 6)
  turtle.end_fill()

while True:
  DrawHexagon("black")  
  DrawSquare("blue")
  DrawHexagon("blue")  
  DrawSquare("black")

  '''
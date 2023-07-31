# Turtle Party Project
# by Julio D. Chavez

import turtle

def draw_circle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtl.goto(x,y)
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end.fill()
  turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yello", 50, -25, 0)

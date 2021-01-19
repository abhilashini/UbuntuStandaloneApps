#!/home/atulrpai/CodePython/SELF/self_venv/bin/python3.6
import turtle as t
import random


def rgb():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return (r, g, b)

tt = t.Turtle()
t.colormode(255)

def draw_spirograph(gap):
	for i in range(360//gap):
		tt.speed("fastest")
		tt.color(rgb())
		tt.circle(100)
		tt.setheading(tt.heading() + gap)

draw_spirograph(12)

s = t.Screen()
s.exitonclick()

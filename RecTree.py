#!/usr/bin/env python3

import turtle
import time

def rec(n,t,r):
	if n == 0:
		return
	if n > 6:
		t.width(4)
		t.color('#511919')
	if n < 7 and n > 4:
		t.width(3)
		t.color('dark green')
	if n < 5 and n > 2:
		t.width(2)
		t.color('#FFB7C5')
	if n < 3:
		t.color('#FF6A87')
	t.pendown()
	t.forward(r)
	# print(x,y)
	t.left(45)
	rec(n-1,t,r*0.65)
	t.right(90)
	rec(n-1,t,r*0.65)
	t.left(45)
	t.penup()
	t.backward(r)


w = turtle.Screen()
w.bgcolor("#edd6ad")
w.title("Cherry Blossom Recersion Tree")

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.width(4)
t.speed("fastest")
t.goto(0,-180)
t.color('#511919')
t.showturtle()
t.pendown()
n = 10
# t = 0
t.left(90)
rec(n,t,150)
time.sleep(30)

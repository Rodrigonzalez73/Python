from turtle import *
import turtle as t 

Screen = t.Screen()
Screen.setworldcoordinates(-350,-350,350,350)
speed(0)
bgcolor('white')
color('red')
hideturtle()

n=1
p=True
while True:
    circle(n)
    if p:
        n=n-1
    else:
        n=n+1
    if n==0 or n==60:
        p= not p 
    left(1)
    forward(0.5)
done()                

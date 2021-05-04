import turtle
import time

clock = turtle.Turtle()
second = turtle.Turtle()
minute = turtle.Turtle()
hour = turtle.Turtle()
screen = turtle.Screen()

'Initial timing'

ts = time.gmtime()
seconds = int(time.strftime("%S", ts))
minutes = int(time.strftime("%M", ts))
hours = int(time.strftime("%I", ts))

clock.pensize(3)
screen.bgcolor('black')
clock.speed(0)
clock.color("purple")
clock.penup()
clock.goto(0,-150)
clock.pendown()
clock.circle(150)
clock.penup()
clock.goto(0,0)
minute.color('white')
hour.color('white')
second.color('white')
minute.pensize(2)
second.speed(0)
minute.speed(0)
hour.speed(0)

for i in range(12):
    clock.forward(120)
    clock.pendown()
    clock.forward(30)
    clock.penup()
    clock.goto(0,0)
    clock.rt(30)
    
clock.hideturtle()

minute.goto(0,0)
hour.goto(0,0)
second.hideturtle()
minute.hideturtle()
hour.hideturtle()
minute.setheading(90-6*minutes)
hour.setheading(90-30*hours)
second.setheading(90-6*seconds)
minute.forward(100)
hour.forward(50)

while True:
    second.pendown()
    second.forward(115)
    time.sleep(1)
    second.undo()
    second.rt(6)
    s = minute.heading()
    
    if second.heading()==90 :
        minute.undo()
        minute.rt(6)
        minute.pendown()
        minute.forward(100)
        
        
    if minute.heading()==90 and s!=90 :
        hour.undo()
        hour.rt(6)
        hour.pendown()
        hour.forward(50)
        
turtle.done()


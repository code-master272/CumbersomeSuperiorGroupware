#Snake
#
#

import turtle
import time
import random

delay = 0.1

#Set up screen
wn = turtle.Screen()
wn.title("Snake by Austin C.")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#0066ff")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("gray")
food.penup()
food.goto(0,100)

segments = []

#Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard binding
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#Main game loop
while True:
    wn.update()

    #Check for border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        #time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #Hide segments
        #for segment in segments:
        #    segment.goto(1000, 1000)

        #Clear the segments list
        #segments.clear()


    #Check for food collision
    if head.distance(food) < 20:
        #Move the food
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#6600ff")
        new_segment.penup()
        segments.append(new_segment)

    #move end segment
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move segment 0
    if len(segments) > 0:
       x = head.xcor()
       y = head.ycor()
       segments[0].goto(x, y)

    move()

    time.sleep(delay)

wn.mainloop()
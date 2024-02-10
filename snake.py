import turtle
import time
import random

delay = 0.1

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Right"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Functions
def go_up():
    if head.direction != "Down":
        head.direction = "Up"

def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"

def go_right():
    if head.direction != "Left":
        head.direction = "Right"

def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Right"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random location
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with the body segments
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Right"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

    time.sleep(delay)
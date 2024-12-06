import turtle
import time
import random

# Delay for game speed
delay = 0.1

# Scores
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("yellow")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")  # Use "circle" for a clear distinction from the head
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Scoreboard
sc = turtle.Turtle()
sc.speed(0)
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("Score: 0  High Score: 0", align="center", font=("ds-digital", 24, "normal"))

# Functions for direction
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
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

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# Main game loop
while True:
    wn.update()

    # Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments of the body
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset the score
        score = 0
        sc.clear()
        sc.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

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

    # Check for collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments of the body
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset the score
            score = 0
            sc.clear()
            sc.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    time.sleep(delay)

wn.mainloop()

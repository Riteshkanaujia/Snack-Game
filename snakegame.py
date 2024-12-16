import turtle
import random
import time

# Game settings
delay = 0.1
score = 0
highest_score = 0
bodies = []

# Screen setup
s = turtle.Screen()
s.title("SNAKE GAME")
s.bgcolor("grey")
s.setup(width=600, height=600)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("green")
food.penup()

# Set initial food position in the allowed area
food.goto(random.randint(-290, 290), random.randint(-240, 240))

# Scoreboard
sb = turtle.Turtle()
sb.speed(0)
sb.shape("circle")
sb.color("black")
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write(f"Score: {score} | Highest Score: {highest_score}", align="center", font=("Courier", 24, "bold"))

# Movement functions
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

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

# Key mappings
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# Main game loop
while True:
    s.update()

    # Border collision check
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide snake bodies
        for body in bodies:
            body.goto(1000, 1000)  # Move out of sight
        bodies.clear()

        # Reset score and delay
        score = 0
        delay = 0.1
        sb.clear()
       

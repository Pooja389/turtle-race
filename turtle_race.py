from turtle import *
import random
screen = Screen()
screen.setup(height = 500,width = 600)

text_turtle = Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.goto(0, 0)  # Center of the screen

all_turtle = []
colors = ["red","blue","green","yellow","pink","black","orange","brown"]
for i in range(8):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-270,-210 + i*60)
    all_turtle.append(turtle)

ask_winner = screen.textinput(title = f"bet",prompt="who will win the race name the color of turtle").lower()   

i = 0
while True:
    
    all_turtle[i].forward(random.randint(10,50))

    if all_turtle[i].xcor() > 285 :
        winner_turtle = all_turtle[i].color()[1]
        break

    i = i + 1 
    if i > 7:
        i = 0 

if ask_winner == winner_turtle:
    text_turtle.write(f"you won!, bcoz {winner_turtle} turtle won the race", align="center", font=("Arial", 20, "bold"))
    
else:
    text_turtle.write(f"you lose!, bcoz {winner_turtle} turtle won the race", align="center", font=("Arial", 20, "bold"))

screen.exitonclick()

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time



screen = Screen()

#set up the main screen
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

#set up the paddle:
r_paddle = Paddle((350, 0)) 
l_paddle = Paddle((-350, 0)) 

#set up the ball:
ball = Ball()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce()
    
 



# set up the movements of the paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.exitonclick()
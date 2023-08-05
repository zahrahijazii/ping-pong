from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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


# set up the movements of the paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#set up the ball:
ball = Ball()

#set up the scoreboard:
score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    
    #Detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    #Detect when paddle misses:
    if ball.xcor() > 380:
        ball.restart()
        score.l_point()
    
    if ball.xcor() < -380:
        ball.restart()
        score.r_point()


    
 




screen.exitonclick()
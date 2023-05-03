import time
from turtle import Screen, Turtle

from src import Ball, Paddle, Scoreboard


def screen_builder():
    s = Screen()
    s.setup(width=800, height=600)
    s.bgcolor("#000000")
    s.title("Pong")
    s.tracer(0)
    return s


def main():
    # Instantiate game objects
    screen = screen_builder()
    scoreboard = Scoreboard()
    r_paddle = Paddle(start_pos=(350, 0))
    l_paddle = Paddle(start_pos=(-350, 0))
    ball = Ball()

    # Build screen listeners
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    # Game main loop
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        ball.move()
        # Detect collision with wall (vertical collision)
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()

        # Detect collision with paddles (horizontal collision)
        r_paddle_collision = ball.distance(r_paddle) < 50 and ball.xcor() > 320
        l_paddle_collision = ball.distance(l_paddle) < 50 and ball.xcor() < -320
        if r_paddle_collision or l_paddle_collision:
            ball.x_bounce()

        # Detects when paddle misses a ball (horizontal collision)
        if ball.xcor() > 390:
            ball.reset_position()
            scoreboard.l_point()
            scoreboard.update_scoreboard()
        if ball.xcor() < -390:
            ball.reset_position()
            scoreboard.r_point()
            scoreboard.update_scoreboard()

    # Close the game when screen detects a mouse click
    # TODO: set up a proper close options
    screen.exitonclick()


if __name__ == "__main__":
    main()

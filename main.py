from turtle import Screen, Turtle
import time

from src import Ball, Paddle


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
        ball.move()
        screen.update()

    # Close the game when screen detects a mouse click
    # TODO: set up a proper close options
    screen.exitonclick()


if __name__ == "__main__":
    main()

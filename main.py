from turtle import Screen


def screen_builder():
    s = Screen()
    s.setup(width=800, height=600)
    s.bgcolor("#000000")
    s.title("Pong")
    return s


def main():
    screen = screen_builder()
    screen.exitonclick()


if __name__ == "__main__":
    main()

import turtle
import time

def draw_moving_heart():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    t.width(2)

    def draw_heart():
        t.begin_fill()
        t.left(50)
        t.forward(133)
        t.circle(50, 200)
        t.right(140)
        t.circle(50, 200)
        t.forward(133)
        t.end_fill()

    for _ in range(10):
        t.penup()
        t.goto(0, 0)
        t.clear()
        t.goto(0, -10 * _)
        t.pendown()
        draw_heart()
        time.sleep(0.2)

    screen.mainloop()

draw_moving_heart()

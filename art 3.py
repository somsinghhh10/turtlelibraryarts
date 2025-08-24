import turtle
import colorsys

def draw_attractive_art():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.hideturtle()

    num_colors = 100
    colors = [colorsys.hsv_to_rgb(i/num_colors, 1.0, 1.0) for i in range(num_colors)]

    for i in range(360):
        color = colors[i % num_colors]
        t.pencolor(color[0], color[1], color[2])
        t.forward(i * 2)
        t.right(61)
        t.forward(i * 2)
        t.right(61)

    screen.mainloop()

draw_attractive_art()

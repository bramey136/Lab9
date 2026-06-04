import turtle
import math

"""
Name: Bria Ramey
Project 3: Turtle Graphics Scene Refactoring

Description:
I refactored my beach sunset scene by breaking draw_scene into smaller helper
functions like draw_sun, draw_cloud, draw_palm_tree, draw_boat, and draw_wave.
Each function has a single purpose and uses parameters so it can be reused.

To make the scene more populated, I reused these functions to add more clouds,
waves, palm trees, and an extra boat. This made it easy to expand the scene
without rewriting code.

Improvements:
- Broke large function into smaller reusable ones
- Removed repeated code using parameters
- Organized code into logical sections
- Made scene more complex using reusable functions
"""

# ---------------- SETUP ----------------

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)

    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")

    # FIXED SCREEN SIZE
    screen.setup(width=800, height=600)
    screen.setworldcoordinates(-400, -300, 400, 300)

    turtle.tracer(0, 0)
    t.hideturtle()

    return t, screen


# ---------------- BASIC SHAPES ----------------

def draw_rectangle(t, width, height, fill_color=None):
    t.setheading(0)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    t.setheading(t.heading())  # keeps intentional angles
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    t.setheading(0)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_curve(t, length, curve_factor, segments=10):
    segment_length = length / segments
    original_heading = t.heading()

    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)

    t.setheading(original_heading)


def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# ---------------- HELPER OBJECTS ----------------

def draw_sun(t, x, y):
    jump_to(t, x, y)
    draw_circle(t, 85, "gold")

    jump_to(t, x + 12, y + 8)
    draw_circle(t, 72, "orange")


def draw_cloud(t, x, y, scale=1):
    t.pencolor("white")

    positions = [(0, 0), (35, -10), (80, 0)]
    sizes = [35, 45, 35]

    for (dx, dy), size in zip(positions, sizes):
        jump_to(t, x + dx * scale, y + dy * scale)
        t.setheading(0)
        draw_circle(t, size * scale, "white")

    t.pencolor("black")


def draw_palm_tree(t, x, y):
    jump_to(t, x, y)
    t.setheading(0)
    draw_rectangle(t, 20, -140, "saddlebrown")

    jump_to(t, x - 25, y + 145)
    t.setheading(0)
    draw_triangle(t, 80, "forestgreen")

    jump_to(t, x - 10, y + 150)
    t.setheading(60)
    draw_triangle(t, 80, "darkgreen")

    jump_to(t, x + 5, y + 155)
    t.setheading(120)
    draw_triangle(t, 75, "green")


def draw_boat(t, x, y):
    jump_to(t, x, y)
    t.setheading(0)
    draw_rectangle(t, 110, 28, "peru")

    jump_to(t, x + 20, y)
    t.setheading(0)
    draw_triangle(t, 90, "white")

    jump_to(t, x + 110, y)
    t.setheading(120)
    draw_triangle(t, 55, "lightyellow")


def draw_wave(t, x, y, length, curve):
    jump_to(t, x, y)
    t.setheading(0)
    draw_curve(t, length, curve, 12)


# ---------------- MAIN SCENE ----------------

def draw_scene(t):
    screen = t.getscreen()
    screen.bgcolor("lightyellow")

    # Background
    jump_to(t, -400, -200)
    draw_rectangle(t, 800, 180, "steelblue")

    jump_to(t, -400, -130)
    draw_rectangle(t, 800, 70, "sandybrown")

    # ORIGINAL SCENE
    draw_sun(t, 100, -130)

    draw_cloud(t, -280, 150)
    draw_cloud(t, 210, 170)

    draw_palm_tree(t, -315, -130)
    draw_palm_tree(t, 308, -130)

    draw_boat(t, 155, -170)

    t.pencolor("lightblue")
    t.pensize(2)

    draw_wave(t, -370, -160, 130, 8)
    draw_wave(t, -120, -175, 110, -8)
    draw_wave(t, 300, -162, 90, 8)

    # -------- ENHANCED SCENE --------
    draw_cloud(t, -50, 180, 0.8)
    draw_cloud(t, 100, 200, 0.7)

    draw_palm_tree(t, -100, -130)

    t.pencolor("lightblue")
    t.pensize(2)

    draw_wave(t, 50, -170, 120, 6)
    draw_wave(t, 200, -175, 100, -6)

    draw_boat(t, -200, -170)

    turtle.update()


# ---------------- MAIN ----------------

def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


if __name__ == "__main__":
    main()

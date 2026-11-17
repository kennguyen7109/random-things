import turtle
import math
import random
# Set random seed for deterministic positioning
random.seed(7)
# Initialize screen environment
screen = turtle.Screen()
screen.setup(1.0, 1.0)
screen.bgcolor("#12001c")
root = screen.getcanvas().winfo_toplevel()
root.attributes("-fullscreen", True)
screen.listen()
screen.onkey(turtle.bye, "Escape") # Esc out
root.update()
screen.update()
# Size take from screen
W = root.winfo_screenwidth()
H = root.winfo_screenheight()
hw, hh = W / 2, H / 2
unit = H / 480
horizon = H * 0.05
# Initialize turtle graphics object
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
# Draw background white stars randomly across the canvas
def stars():
    t.penup()
    screen_x = screen.window_width() // 2
    screen_y = screen.window_height() // 2
    for _ in range(150):
        x = random.randint(-screen_x, screen_x)
        y = random.randint(-screen_y, screen_y)
        t.goto(x, y)
        t.dot(random.randint(2, 4), "white")
# Draw the curved green flower stem
def stem(bx, by, hx, hy, s):
    cx, cy = bx, (by + hy)/ 2
    steps = 50
    leaf_at = {int(steps * 0.3) : 160, int(steps * 0.6) : 20}
    t.color("#2e9e5b")
    t.pensize(7)
    left_leaf_opened = False
    right_leaf_opened = False
    t.penup()
    t.goto(bx, by)
    t.pendown()
    points = []
    for step in range(steps + 1):
        prog = step / steps
        x = (1 - prog) ** 2 * bx + 2 * (1 - prog) * prog * cx + prog ** 2 * hx
        y = (1 - prog) ** 2 * by + 2 * (1 - prog) * prog * cy + prog ** 2 * hy
        t.goto(x, y)
        if step in leaf_at:
            leaf(x, y, leaf_at[step], s * 0.8)
            t.penup()
            t.goto(x, y)
            t.color("#2e9e5b")
            t.pensize(max(3, 7 * s))
            t.pendown()
    t.penup()
# Draw a leaf with detailed main stem and branching side veins
def leaf(x, y, angle, s):
    # Outer leaf body outline and fill
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.color("#7fe0a3", "#1f8a4c")
    t.pensize(2)
    t.pendown()
    t.begin_fill()
    t.circle(95 * s, 60)
    t.left(120)
    t.circle(95 * s, 60)
    t.end_fill()
    # Main center vein line
    t.penup()
    t.goto(x, y)
    t.setheading(angle + 30)
    t.color("#a3f3c3")
    t.pensize(1)
    t.pendown()
    t.forward(80 * s)
# Draw an individual petal
def petal(size, edge, fill):
    # Main filled petal body
    t.color(edge, fill)
    t.pensize(2)
    t.begin_fill()
    t.circle(size, 80)
    t.left(100)
    t.circle(size, 80)
    t.left(100)
    t.end_fill()
# Draw layered concentric petals radiating outward from the flower center
def bloom(cx, cy, s):
    rings = [
        (8, 120, "#ff6fa8", "#7d0a45"),
        (8, 102, "#ff7fb4", "#a8125c"),
        (7, 84, "#ff9cc6" ,"#d81b78"),
        (6, 66, "#ffb3d3", "#f2559a"),
        (5, 50, "#ffb0e4", "#ff8cc0"),
        (4, 34, "#fff0f6", "#ffc2dc"),
    ]
    for count, size, edge, fill in rings:
        shift = random.randint(0, 40)
        for i in range(count):
            t.penup()
            t.goto(cx, cy)
            a = shift + i * 360 / count
            t.setheading(shift + i * 360/ count + random.uniform(-4, 4))
            t.pendown()
            ss = size * s * random.uniform(0.94, 1.04)
            petal(ss, edge, fill)
# Draw a clean, simple central stamen without extra connecting lines
def center(cx, cy, s):
    # Central core dot
    t.penup()
    t.goto(cx, cy)
    t.dot(24 * s, "#ffd54a")
def flower(x, y, s, base_x):
    stem(base_x, -230, x, y, s)
    bloom(x, y, s)
    center(x, y, s)
flowers = [(-270, 100, 0.55, -300), (280, 120, 0.60, 300), (0, 60, 1.00, 0)]
# Execution
stars()
for x, y, s, base_x in flowers:
    flower(x, y, s, base_x)
t.hideturtle()
turtle.done()
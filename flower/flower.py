import turtle
import math
import random
# Set random seed for deterministic positioning
random.seed(7)
# Initialize screen environment
screen = turtle.Screen()
screen.bgcolor("#12001c")
root = screen.getcanvas().winfo_toplevel()
screen.setup(1.0, 1.0)
root.attributes("-fullscreen", True)
screen.listen()
screen.onkey(turtle.bye, "Escape")
# Initialize turtle graphics object
t= turtle.Turtle()
t.speed(0)
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
def stem():
    cx, cy, r = -399.4, -68.4, 420.0
    start_angle_deg = 18.0
    end_angle_deg = -16.0
    steps = 50
    points = []
    for step in range(steps + 1):
        prog = step / steps
        deg = end_angle_deg + (start_angle_deg - end_angle_deg) * prog
        rad = math.radians(deg)
        px = cx + r * math.cos(rad)
        py = cy + r * math.sin(rad)
        points.append((px, py, prog))
    t.color("#2e9e5b")
    t.pensize(7)
    left_leaf_opened = False
    right_leaf_opened = False
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    
    for px, py, prog in points:
        t.goto(px, py)
        # Open left leaf when stem draw to y = -150
        if py >= -150 and not left_leaf_opened:
            t.penup()
            leaf(12, -150, 160)
            left_leaf_opened = True
            t.penup()
            t.goto(px, py)
            t.color("#2e9e5b")
            t.pensize(6)
            t.pendown()
        #Open right leaf when stem draw to y = -95
        if py >= -95 and not right_leaf_opened:
            t.penup()
            leaf(19, -95, 20)
            right_leaf_opened = True
            t.penup()
            t.goto(px, py)
            t.color("#2e9e5b")
            t.pensize(6)
            t.pendown()    
    t.penup()
# Draw a leaf with detailed main stem and branching side veins
def leaf(x, y, angle):
    # Outer leaf body outline and fill
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.color("#7fe0a3", "#1f8a4c")
    t.pensize(2)
    t.pendown()
    t.begin_fill()
    t.circle(95, 60)
    t.left(120)
    t.circle(95, 60)
    t.end_fill()
    # Main center vein line
    t.penup()
    t.goto(x, y)
    t.setheading(angle + 30)
    t.color("#a3f3c3")
    t.pensize(1)
    t.pendown()
    t.forward(80)
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
def bloom():
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
            t.goto(0, 60)
            a = shift + i * 360 / count
            t.setheading(a + random.uniform(-4, 4))
            t.pendown()
            s = size * random.uniform(0.94, 1.04)
            petal(s, edge, fill)
# Draw a clean, simple central stamen without extra connecting lines
def center():
    # Central core dot
    t.penup()
    t.goto(0, 60)
    t.dot(24, "#ffd54a")
# Execution 
stars()
stem()
bloom()
center()
t.hideturtle()
turtle.done()
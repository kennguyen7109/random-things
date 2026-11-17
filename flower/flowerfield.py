import turtle
import math
import random

random.seed(7)

screen = turtle.Screen()
screen.setup(1.0, 1.0)
screen.bgcolor("#9fd8ff")
root = screen.getcanvas().winfo_toplevel()
root.attributes("-fullscreen", True)
screen.listen()
screen.onkey(turtle.bye, "Escape")
root.update()
screen.update()

W = root.winfo_screenwidth()
H = root.winfo_screenheight()
hw, hh = W / 2, H / 2
unit = H / 480
horizon = H * 0.05

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
# Utility fuction
def hex_to_gcb(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))
def mix(c1, c2, f):
    f = max(0.0, min(1.0, f))
    a, b = hex_to_gcb(c1), hex_to_gcb(2)
    return "#%02x%02x%02x" % tuple(int(a[i] + (b[i] - a[i]) * f) for i in range(3))
def rect(x1, x2, y1, y2, color):
    t.penup()
    t.goto(x1, y1)
    t.color(color, color)
    t.pensize(1)
    t.pendown()
    t.begin_fill()
    for x, y in ((x1, y1), (x2, y2), (x1, y2), (x2, y1)):
        t.goto(x, y)
    t.end_fill()
    t.penup()
# Sky, Sun, Cloud, Hill
def sky_color(y):
    f = (y - horizon) / (hh - horizon)
    return mix("#c9ecff", "#2b7fd4", max(0.0, min(1.0, f)) ** 0.8)
def draw_sky():
    bands = 48
    top, bot = hh * 1.05, horizon
    step = (top - bot) / bands
    for i in range(bands):
        y1 = bot + i * step
        rect(-hw * 1.05, hw * 1.05, y1 - 1, y1 + step + 1, sky_color(y1 + step /2))
def draw_sun(sx, sy, r):
    base = sky_color(sy)
    for k in range(8, 0, -1):
        t.goto(sx, sy)
        t.dot(2 * r * (1 + 0.28 * k), mix(base, "#fff6c0", 0.08 + 0.5 * (1 - k / 8)))
    t.color("#fff2a8")
    t.pensize(int(max(2, 3 * unit)))
    for i in range(16):
        a = math.radians(i * 22.5)
        t.penup()
        t.goto(sx + math.cos(a) * r * 1.25, sy + math.sin(a) * r * 1.25)
        t.pendown()
        t.goto(sx + math.cos(a) * r * 2.0, sy + math.sin(a) * r * 2.0)
    t.penup()
    for c, d in ((2.0, "#ffcf40"), (1.55, "#ffe566"), (1.0, "#fff4b0")):
        t.goto(sx, sy)
        t.dot(r * c, d)
P = [(-70, -6, 56), (-32, 14, 78), (14, 22, 88), (58, 6, 70), (92, -8, 50), (0, -10, 90)]
def draw_cloud(cx, cy, sc):
        for dx, dy, d in P:
            t.goto(cx + dx * sc, cy + (dy - 7) * sc)
            t.dot(d * sc, "#d3e6f6")
        for dx, dy, d in P:
            t.goto(cx + dx * sc, cy + dy * sc)
            t.dot(d * sc, "#ffffff")
def draw_hills():
    for color, hmin, hmax, n in (("#a5dcb0", 0.07, 0.12, 4), ("#82d08a", 0.04, 0.08, 5)):
        for _ in range(n):
            x = random.uniform(-hw, hw)
            height = H * random.uniform(hmin, hmax)
            r = H * random.uniform(0.45, 0.8)
            t.goto(x, horizon + height - r)
            t.dot(int(2 * r), color)
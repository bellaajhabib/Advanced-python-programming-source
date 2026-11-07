"""
Dice & Lottery Generator — visual version with Turtle graphics.
Click the screen to re-roll everything!
"""

from turtle import Turtle, Screen
import random

# --- Screen setup ---
screen = Screen()
screen.setup(750, 850)
screen.title("🎲 Dice & Lottery Generator — Click to re-roll!")
screen.bgcolor("#1a1a2e")
screen.tracer(0)


def make_t():
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    return t


# --- Draw a rounded rectangle ---
def draw_box(t, x, y, w, h, color="#16213e", border="#e94560"):
    t.goto(x, y)
    t.fillcolor(color)
    t.pencolor(border)
    t.pensize(2)
    t.pendown()
    t.begin_fill()
    for side in [w, h, w, h]:
        t.forward(side)
        t.left(90)
    t.end_fill()
    t.penup()


# --- Draw a die face ---
def draw_die(t, cx, cy, num):
    size = 80
    x = cx - size // 2
    y = cy - size // 2
    dot_size = 12

    # white die body
    draw_box(t, x, y, size, size, color="white", border="#333333")

    # dot positions relative to center
    positions = {
        1: [(0, 0)],
        2: [(-20, 20), (20, -20)],
        3: [(-20, 20), (0, 0), (20, -20)],
        4: [(-20, 20), (20, 20), (-20, -20), (20, -20)],
        5: [(-20, 20), (20, 20), (0, 0), (-20, -20), (20, -20)],
        6: [(-20, 20), (20, 20), (-20, 0), (20, 0), (-20, -20), (20, -20)],
    }

    for dx, dy in positions[num]:
        t.goto(cx + dx, cy + dy)
        t.dot(dot_size, "#1a1a2e")


# --- Draw lottery balls ---
def draw_ball(t, x, y, num, color, text_color="white"):
    t.goto(x, y)
    t.dot(44, color)
    t.dot(38, color)
    t.goto(x, y - 8)
    t.color(text_color)
    t.write(str(num), align="center", font=("Arial", 13, "bold"))


# --- Draw a section title ---
def draw_title(t, x, y, text):
    t.goto(x, y)
    t.color("#e94560")
    t.write(text, align="center", font=("Arial", 16, "bold"))


# --- Draw everything ---
artist = make_t()


def draw_all():
    artist.clear()

    # ==============================
    # DICE (top section)
    # ==============================
    draw_title(artist, 0, 370, "🎲  DICE ROLL  🎲")
    dice_num = random.randint(1, 6)
    draw_die(artist, 0, 310, dice_num)

    # ==============================
    # LOTTERY 1: EuroMillions style (5 from 1-50 + 2 lucky 1-12)
    # ==============================
    y = 220
    draw_title(artist, 0, y, "🎰  EUROMILLIONS  (50/5 + 12/2)")

    nums = sorted(random.sample(range(1, 51), 5))
    lucky = sorted(random.sample(range(1, 13), 2))

    start_x = -140
    for i, n in enumerate(nums):
        draw_ball(artist, start_x + i * 55, y - 45, n, "#0f3460")
    for i, n in enumerate(lucky):
        draw_ball(artist, start_x + (5 + i) * 55 + 15, y - 45, n, "#e94560")

    # ==============================
    # LOTTERY 2: 6 from 1-40 + 1 lucky 1-5
    # ==============================
    y = 100
    draw_title(artist, 0, y, "🎰  LOTO  (40/6 + 5/1)")

    nums2 = sorted(random.sample(range(1, 41), 6))
    lucky2 = random.randint(1, 5)

    start_x = -165
    for i, n in enumerate(nums2):
        draw_ball(artist, start_x + i * 55, y - 45, n, "#0f3460")
    draw_ball(artist, start_x + 6 * 55 + 15, y - 45, lucky2, "#e94560")

    # ==============================
    # LOTTERY 3: 10 from 1-25
    # ==============================
    y = -20
    draw_title(artist, 0, y, "🎰  KENO  (25/10)")

    nums3 = sorted(random.sample(range(1, 26), 10))

    start_x = -250
    for i, n in enumerate(nums3):
        draw_ball(artist, start_x + i * 55, y - 45, n, "#533483")

    # ==============================
    # LOTTERY 4: 5 from 1-49 + 1 lucky 1-10
    # ==============================
    y = -140
    draw_title(artist, 0, y, "🎰  LOTO CLASSIQUE  (49/5 + 10/1)")

    nums4 = sorted(random.sample(range(1, 50), 5))
    lucky4 = random.randint(1, 10)

    start_x = -140
    for i, n in enumerate(nums4):
        draw_ball(artist, start_x + i * 55, y - 45, n, "#0f3460")
    draw_ball(artist, start_x + 5 * 55 + 15, y - 45, lucky4, "#e94560")

    # ==============================
    # Footer
    # ==============================
    artist.goto(0, -280)
    artist.color("#555555")
    artist.write("Click anywhere to re-roll!", align="center",
                 font=("Arial", 13, "italic"))

    screen.update()


# --- Click to re-roll ---
def on_click(x, y):
    draw_all()

draw_all()
screen.onclick(on_click)
screen.mainloop()

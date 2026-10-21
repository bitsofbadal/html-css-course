import tkinter as tk
import random
import math

root = tk.Tk()
root.title("For You ❤️")
root.configure(bg="black")
root.attributes("-fullscreen", True)

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

W = root.winfo_screenwidth()
H = root.winfo_screenheight()

# Big YOU text
text_id = canvas.create_text(
    W // 2, H // 2,
    text="YOU",
    fill="#ff1744",
    font=("Arial", int(H * 0.32), "bold")
)

# Romantic subtitle
canvas.create_text(
    W // 2, H // 2 + H * 0.20,
    text="❤️Only U ❤️",
    fill="#ff80ab",
    font=("Arial", max(16, int(H * 0.035)), "bold")
)

# Floating particles
particles = []

colors = [
    "#ff1744", "#ff4081", "#ff80ab",
    "#ffffff", "#ba68c8", "#f50057"
]

for _ in range(100):
    x = random.randint(0, W)
    y = random.randint(0, H)
    r = random.randint(2, 5)

    particle = canvas.create_oval(
        x-r, y-r, x+r, y+r,
        fill=random.choice(colors),
        outline=""
    )

    particles.append({
        "id": particle,
        "x": x,
        "y": y,
        "r": r,
        "speed": random.uniform(0.5, 2.5)
    })

phase = 0

def animate():
    global phase
    phase += 0.06

    # Glowing colour animation
    glow_colors = [
        "#ff1744", "#ff4081",
        "#f50057", "#e040fb",
        "#ff80ab"
    ]

    canvas.itemconfig(
        text_id,
        fill=glow_colors[int(phase) % len(glow_colors)]
    )

    # Floating particle animation
    for p in particles:
        p["y"] -= p["speed"]
        p["x"] += math.sin(phase + p["y"] * 0.01) * 1.5

        if p["y"] < 0:
            p["y"] = H
            p["x"] = random.randint(0, W)

        r = p["r"]
        canvas.coords(
            p["id"],
            p["x"]-r, p["y"]-r,
            p["x"]+r, p["y"]+r
        )

    root.after(30, animate)

# Press ESC to exit fullscreen
root.bind("<Escape>", lambda event: root.destroy())

animate()
root.mainloop()
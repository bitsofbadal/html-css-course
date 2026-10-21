
import time
import sys
import os
import random

DEEP_RED = '\033[38;5;88m'
PASSION_PURPLE = '\033[38;5;54m'
GOLDEN_WARM = '\033[38;5;136m'
MIST_WHITE = '\033[38;5;251m'
BOLD = '\033[1m'
RESET = '\033[0m'

def sensual_typing(text, color):
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.078)
    print()
    time.sleep(0.8)

lyrics = [
    ("Tere ehsaason mein... ☁️", DEEP_RED),
    ("Bheege lamhaato mein... ☁️", PASSION_PURPLE),
    ("Mujhko dooba tishnagi si hai... 🥀", GOLDEN_WARM),
    ("Teri adao se dilkash khataon se ❤️", MIST_WHITE),
    ("Meri zindagi hai tu... 💖", DEEP_RED),
]

os.system("cls" if os.name == "nt" else "clear")

time.sleep(1)

for text, color in lyrics:
    sensual_typing(text, color)
    time.sleep(1.2)

print(f"\n{BOLD}{PASSION_PURPLE}❤️  Made with Python  ❤️{RESET}")
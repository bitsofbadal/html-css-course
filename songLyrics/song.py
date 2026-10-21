
  
import time

lyrics = [
    "🎶 Sunn Le Yeh Sadaa....",
    "💖 Kaisi Dillagi Hai Tu....",
    "🤗 Kaisi Bebasi Hai Tu....",
    "🥰 Meri Zindagi Hai Tu....",
    "💖 Meri Zindagi Hai Tu....",
    "💖 ☆*:.. o(≧▽≦)o ..:*☆ 💖"
]

delays = [0.9, 4.2, 4.2, 4.6, 0.8, 4.0]

def type_line(line):
    for char in line:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()

time.sleep(2)

for i in range(len(lyrics)):
    type_line(lyrics[i])
    time.sleep(delays[i])

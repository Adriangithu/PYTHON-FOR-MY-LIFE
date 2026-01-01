import curses
import random
import time
import math

Text = "Selamat Tahun Baru 2026"
warna = [1,2,3,4,5,6,7]

def texttampil(stdscr, y, text):
  h , w = stdscr.getmaxyx()
  x = w//2 - len(text)//2
  stdscr.addstr(y,x,text)

def kembangapi(stdscr):
  h,w = stdscr.getmaxyx()
  y = h - 2
  peak = random.randint(h//4, h//2)
  color = random.choice(warna)
  x = random.randint(0, w - 1) # Define x here, randomly for a firework launch point

  while y > peak:
    stdscr.clear()
    stdscr.attron(curses.color_pair(color))
    stdscr.addstr(y,x,"|")
    stdscr.attroff(curses.color_pair(color))
    stdscr.refresh()
    y -= 1
    time.sleep(0.02)

  for r in range(1,8):
    stdscr.clear()
    for angle in range(0,360,20):
      rad = math.radians(angle)
      ex = int(x+r*math.cos(rad))
      ey = int(y+r*math.sin(rad))
      if 0 < ey < h and 0 <ex <w:
        stdscr.attron(curses.color_pair(random.choice(warna)))
        stdscr.addstr(ey, ex, "*")
        stdscr.attroff(curses.color_pair(random.choice(warna)))
    texttampil(stdscr, h//2, Text)
    stdscr.refresh()
    time.sleep(0.05)

def main(stdscr):
  curses.curs_set(0)
  curses.start_color()
  curses.use_default_colors()

  for i in range(1,8):
    curses.init_pair(i,i,-1)

  while True:
    kembangapi(stdscr)
curses.wrapper(main)
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import screeninfo
import random
import sys
import os
import argparse


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='store_true')
parser.add_argument('-n', '--number', type=int, required=False,
                    default=1, help='Number of elephants')
parser.add_argument('-d', '--delay', type=float, required=False,
                    default=2, help='Delay of changing position in seconds')
# parser.add_argument('-dm', '--dont-move', action='store_true')
args = parser.parse_args()

help_message = \
    '''Options:
-h, --help
\tShow this help message and exit
-n NUMBER, --number NUMBER
\tNumber of elephants
-d DELAY, --delay DELAY
\tDelay of changing position in seconds'''

if args.help:
    messagebox.showinfo("Help", help_message)
    sys.exit(0)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class ElephantWindow:
    def __init__(self):
        self.m = screeninfo.get_monitors()[0]

        self.window = tk.Tk()

        self.window.overrideredirect(True)
        self.window.config(bg='white')
        self.window.wm_attributes('-transparentcolor', 'white')
        self.window.attributes('-topmost', True)

        self.img = Image.open(resource_path('elephant.png')).resize((300, 200))
        self.img_tk = ImageTk.PhotoImage(self.img)

        self.label = tk.Label(self.window, image=self.img_tk, bg='white')
        self.label.pack()

    def change_window_position(self):
        x, y = random.randint(0, self.m.width - 300), \
            random.randint(0, self.m.height - 200)
        self.window.geometry(f'+{x}+{y}')
        self.window.after(int(args.delay * 1000), self.change_window_position)

    def start(self):
        self.change_window_position()
        self.window.mainloop()


class ElephantWindowToplevel:
    def __init__(self):
        self.m = screeninfo.get_monitors()[0]

        self.window = tk.Toplevel()

        self.window.overrideredirect(True)
        self.window.config(bg='white')
        self.window.wm_attributes('-transparentcolor', 'white')
        self.window.attributes('-topmost', True)

        self.img = Image.open(resource_path('elephant.png')).resize((300, 200))
        self.img_tk = ImageTk.PhotoImage(self.img)

        self.label = tk.Label(self.window, image=self.img_tk, bg='white')
        self.label.pack()

    def change_window_position(self):
        x, y = random.randint(0, self.m.width - 300), \
            random.randint(0, self.m.height - 200)
        self.window.geometry(f'+{x}+{y}')
        self.window.after(int(args.delay * 1000), self.change_window_position)

    def start(self):
        self.change_window_position()


e = ElephantWindow()
for _ in range(args.number - 1):
    ElephantWindowToplevel().start()
e.start()

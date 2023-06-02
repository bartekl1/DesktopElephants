import tkinter as tk
from PIL import Image, ImageTk
import screeninfo
import random
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def change_window_position():
    x, y = random.randint(0, m.width - 300), random.randint(0, m.height - 200)
    window.geometry(f'+{x}+{y}')
    window.after(2000, change_window_position)


m = screeninfo.get_monitors()[0]

window = tk.Tk()

window.overrideredirect(True)
window.config(bg='white')
window.wm_attributes('-transparentcolor', 'white')
window.attributes('-topmost', True)

img = Image.open(resource_path('elephant.png')).resize((300, 200))
img_tk = ImageTk.PhotoImage(img)

label = tk.Label(window, image=img_tk, bg='white')
label.pack()

change_window_position()

window.mainloop()

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes
import locale
import sys
import os

import DesktopElephants

polish_text = [
    'Ilość słoni:',
    'Opóźnienie zmiany pozycji:',
    'Zakończ po czasie:',
    'Nie zmieniaj pozycji',
    'Nie kończ',
    'Argumenty:',
    'Kopiuj',
    'Skopiowano'
]

english_text = [
    'Number of elephants:',
    'Delay of changing position:',
    'End after time:',
    'Don\'t change position',
    'Don\'t end',
    'Arguments',
    'Copy',
    'Copied'
]


class Args:
    def __init__(self, number, delay, end):
        self.number = number
        self.delay = delay
        self.end = end


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_text(text_number):
    if language == 'pl_PL':
        return polish_text[text_number]
    else:
        return english_text[text_number]


def update_arguments():
    arguments = []
    if number_var.get() != '1' and number_var.get() != '':
        arguments.append('-n')
        arguments.append(number_var.get())
    if delay_var.get() != '':
        arguments.append('-d')
        arguments.append(delay_var.get())
    if end_var.get() != '':
        arguments.append('-e')
        arguments.append(end_var.get())
    arguments_var.set(' '.join(arguments))
    arguments_copy_button.config(text=get_text(6))


def copy_arguments():
    window.clipboard_clear()
    window.clipboard_append(arguments_var.get())
    window.update()
    arguments_copy_button.config(text=get_text(7))


def start():
    try:
        number = int(number_var.get())
        delay = float(delay_var.get()) if delay_var.get() != '' else None
        end = float(end_var.get()) if end_var.get() != '' else None
    except Exception:
        messagebox.showerror('Błąd', 'Wprowadzono błędne dane!')
    else:
        window.destroy()
        DesktopElephants.args = Args(number, delay, end)
        e = [DesktopElephants.ElephantWindow()]
        for _ in range(number - 1):
            e.append(DesktopElephants.ElephantWindowToplevel())
            e[-1].start()
        e[0].start()


def main():
    global language, \
        delay_entry, end_entry, \
        number_var, delay_var, end_var, \
        arguments_var, arguments_copy_button, window

    windll = ctypes.windll.kernel32
    language = locale.windows_locale[windll.GetUserDefaultUILanguage()]

    window = tk.Tk()

    window.title('Desktop Elephants')
    window.iconbitmap(resource_path('elephant.ico'))

    title_frame = tk.Frame(window)
    title_frame.pack()

    title = tk.Label(title_frame,
                     text='Desktop Elephants',
                     font=('Calibri', 24),
                     fg='blue')
    title.grid(row=0, column=0)

    image = Image.open(resource_path('elephant.png')).resize((70, 40))
    image_tk = ImageTk.PhotoImage(image)
    image_label = tk.Label(title_frame, image=image_tk)
    image_label.grid(row=0, column=1)

    options_frame = tk.Frame(window)
    options_frame.pack()

    number_var = tk.StringVar(value='1')
    number_var.trace("w", lambda name, index, mode: update_arguments())

    number_label = tk.Label(options_frame,
                            text=get_text(0),
                            font=('Calibri', 12))
    number_label.grid(row=0, column=0, sticky='w')

    number_entry = tk.Entry(options_frame,
                            font=('Calibri', 12),
                            width=8,
                            textvariable=number_var)
    number_entry.grid(row=0, column=1)

    delay_var = tk.StringVar()
    delay_var.trace("w", lambda name, index, mode: update_arguments())

    delay_label = tk.Label(options_frame,
                           text=get_text(1),
                           font=('Calibri', 12))
    delay_label.grid(row=1, column=0, sticky='w')

    delay_entry = tk.Entry(options_frame,
                           font=('Calibri', 12),
                           width=8,
                           textvariable=delay_var)
    delay_entry.grid(row=1, column=1)

    end_var = tk.StringVar()
    end_var.trace("w", lambda name, index, mode: update_arguments())

    end_label = tk.Label(options_frame,
                         text=get_text(2),
                         font=('Calibri', 12))
    end_label.grid(row=2, column=0, sticky='w')

    end_entry = tk.Entry(options_frame,
                         font=('Calibri', 12),
                         width=8,
                         textvariable=end_var)
    end_entry.grid(row=2, column=1)

    arguments_frame = tk.Frame(window)
    arguments_frame.pack(pady=5)

    arguments_label = tk.Label(arguments_frame,
                               text=get_text(5),
                               font=('Calibri', 12))
    arguments_label.grid(row=0, column=0)

    arguments_var = tk.StringVar()

    arguments_entry = tk.Entry(arguments_frame,
                               font=('Calibri', 12),
                               width=15,
                               textvariable=arguments_var)
    arguments_entry.grid(row=0, column=1)

    arguments_copy_button = tk.Button(arguments_frame,
                                      text=get_text(6),
                                      font=('Calibri', 10),
                                      command=copy_arguments)
    arguments_copy_button.grid(row=0, column=2)

    start_button = tk.Button(window,
                             text='START',
                             font=('Calibri', 20),
                             command=start)
    start_button.pack()

    window.mainloop()


if __name__ == '__main__':
    main()

import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
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
    'Skopiowano',
    'Błąd',
    'Wprowadzono błędne dane!'
]

english_text = [
    'Number of elephants:',
    'Delay of changing position:',
    'End after time:',
    'Don\'t change position',
    'Don\'t end',
    'Arguments',
    'Copy',
    'Copied',
    'Error',
    'Entered incorrect data'
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
    arguments_copy_button.configure(text=get_text(6))


def copy_arguments():
    window.clipboard_clear()
    window.clipboard_append(arguments_var.get())
    window.update()
    arguments_copy_button.configure(text=get_text(7))


def start():
    try:
        number = int(number_var.get())
        delay = float(delay_var.get()) if delay_var.get() != '' else None
        end = float(end_var.get()) if end_var.get() != '' else None
    except Exception:
        messagebox.showerror(get_text(8), get_text(9))
    else:
        try:
            window.destroy()
        except Exception:
            pass
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

    ctk.sys.stdout = open(os.devnull, 'w')

    windll = ctypes.windll.kernel32
    language = locale.windows_locale[windll.GetUserDefaultUILanguage()]

    window = ctk.CTk()

    window.title('Desktop Elephants')
    window.iconbitmap(resource_path('elephant.ico'))

    main_frame = ctk.CTkFrame(window, fg_color='transparent')
    main_frame.pack(padx=4, pady=4)

    title_frame = ctk.CTkFrame(main_frame, fg_color='transparent')
    title_frame.pack()

    title = ctk.CTkLabel(title_frame,
                         text='Desktop Elephants',
                         font=('Calibri', 24),
                         fg_color='transparent')
    title.grid(row=0, column=0)

    image = Image.open(resource_path('elephant.png'))
    image_tk = ctk.CTkImage(image, size=(70, 40))
    image_label = ctk.CTkLabel(title_frame, image=image_tk, text='')
    image_label.grid(row=0, column=1)

    options_frame = ctk.CTkFrame(main_frame, fg_color='transparent')
    options_frame.pack()

    number_var = ctk.StringVar(value='1')
    number_var.trace("w", lambda name, index, mode: update_arguments())

    number_label = ctk.CTkLabel(options_frame,
                                text=get_text(0),
                                font=('Calibri', 14))
    number_label.grid(row=0, column=0, sticky='w',
                      padx=2, pady=2)

    number_entry = ctk.CTkEntry(options_frame,
                                font=('Calibri', 14),
                                width=50,
                                textvariable=number_var)
    number_entry.grid(row=0, column=1,
                      padx=2, pady=2)

    delay_var = ctk.StringVar()
    delay_var.trace("w", lambda name, index, mode: update_arguments())

    delay_label = ctk.CTkLabel(options_frame,
                               text=get_text(1),
                               font=('Calibri', 14))
    delay_label.grid(row=1, column=0, sticky='w',
                     padx=2, pady=2)

    delay_entry = ctk.CTkEntry(options_frame,
                               font=('Calibri', 14),
                               width=50,
                               textvariable=delay_var)
    delay_entry.grid(row=1, column=1,
                     padx=2, pady=2)

    end_var = ctk.StringVar()
    end_var.trace("w", lambda name, index, mode: update_arguments())

    end_label = ctk.CTkLabel(options_frame,
                             text=get_text(2),
                             font=('Calibri', 14))
    end_label.grid(row=2, column=0, sticky='w',
                   padx=2, pady=2)

    end_entry = ctk.CTkEntry(options_frame,
                             font=('Calibri', 14),
                             width=50,
                             textvariable=end_var)
    end_entry.grid(row=2, column=1,
                   padx=2, pady=2)

    arguments_frame = ctk.CTkFrame(main_frame, fg_color='transparent')
    arguments_frame.pack(pady=5)

    arguments_label = ctk.CTkLabel(arguments_frame,
                                   text=get_text(5),
                                   font=('Calibri', 14))
    arguments_label.grid(row=0, column=0,
                         padx=2, pady=2)

    arguments_var = ctk.StringVar()

    arguments_entry = ctk.CTkEntry(arguments_frame,
                                   font=('Calibri', 14),
                                   width=120,
                                   textvariable=arguments_var)
    arguments_entry.grid(row=0, column=1,
                         padx=2, pady=2)

    arguments_copy_button = ctk.CTkButton(arguments_frame,
                                          text=get_text(6),
                                          font=('Calibri', 14),
                                          width=56,
                                          command=copy_arguments)
    arguments_copy_button.grid(row=0, column=2,
                               padx=2, pady=2)

    start_button = ctk.CTkButton(main_frame,
                                 text='START',
                                 font=('Calibri', 26),
                                 width=100,
                                 command=start)
    start_button.pack()

    window.mainloop()


if __name__ == '__main__':
    main()

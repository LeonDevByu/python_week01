import math
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry, FloatEntry
import pywhatkit
from tkinter import *


def main():
    # Create the Tk root object.
    root = tk.Tk()
    root.geometry("500x300")
    root.maxsize(500, 600)
    root.config(bg="lightgrey")
    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("ATTENDANCE LIST OF THE QUORUM OF ELDERS")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)
    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def populate_main_window(frm_main):
    lbl_01 = Label(frm_main, text="Please enter your information: ", bg="lightgrey")
    # lbl_01 = Label(frm_main, text="Attendance: 1     Missing: 2")

    lbl_02 = Label(frm_main, text="León  Matías Edwin Leonardo :")
    lbl_03 = Label(frm_main, text="Benites Relaiza Alex Patricio :")
    lbl_04 = Label(frm_main, text="León   Matías   Javier   Luis :")
    lbl_05 = Label(frm_main, text="Rosas Rodriguez, Jean Pool :")
    lbl_06 = Label(frm_main, text="Cabellos Tineo, Eduardo Martin :")
    lbl_07 = Label(frm_main, text="Aranda Capcha, David Julian :")
    lbl_08 = Label(frm_main, text="Aranda Loayza, Jeffrey Robert :")
    lbl_09 = Label(frm_main, text="Ascarate Ortega, Armando :")
    lbl_10 = Label(frm_main, text="Asto Laupa, Julio Cesar :")

    # Create three number entries.
    red_var02 = IntVar()
    red_var03 = IntVar()
    red_var04 = IntVar()
    red_var05 = IntVar()
    red_var06 = IntVar()
    red_var07 = IntVar()
    red_var08 = IntVar()
    red_var09 = IntVar()
    red_var10 = IntVar()
    ent_02 = Checkbutton(frm_main, width=5, variable=red_var02, bg="grey")
    ent_03 = Checkbutton(frm_main, width=5, variable=red_var03, bg="darkgray")
    ent_04 = Checkbutton(frm_main, width=5, variable=red_var04, bg="grey")
    ent_05 = Checkbutton(frm_main, width=5, variable=red_var05, bg="darkgray")
    ent_06 = Checkbutton(frm_main, width=5, variable=red_var06, bg="grey")
    ent_07 = Checkbutton(frm_main, width=5, variable=red_var07, bg="darkgray")
    ent_08 = Checkbutton(frm_main, width=5, variable=red_var08, bg="grey")
    ent_09 = Checkbutton(frm_main, width=5, variable=red_var09, bg="darkgray")
    ent_10 = Checkbutton(frm_main, width=5, variable=red_var10, bg="grey")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")
    btn_submit = Button(frm_main, text="Submit", command=populate_main_window)
    btn_end = Button(frm_main, text="End", command=frm_main.quit)

    # Layout all the labels, number entries, and buttons in a grid.
    lbl_01.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    lbl_02.grid(row=1, column=0, padx=3, pady=2, sticky="e")
    ent_02.grid(row=1, column=1, padx=3, pady=2, sticky="w")

    lbl_03.grid(row=2, column=0, padx=3, pady=2, sticky="e")
    ent_03.grid(row=2, column=1, padx=3, pady=2, sticky="w")

    lbl_04.grid(row=3, column=0, padx=3, pady=2, sticky="e")
    ent_04.grid(row=3, column=1, padx=3, pady=2, sticky="w")

    lbl_05.grid(row=4, column=0, padx=3, pady=2, sticky="e")
    ent_05.grid(row=4, column=1, padx=3, pady=2, sticky="w")

    lbl_06.grid(row=5, column=0, padx=3, pady=2, sticky="e")
    ent_06.grid(row=5, column=1, padx=3, pady=2, sticky="w")

    lbl_07.grid(row=6, column=0, padx=3, pady=2, sticky="e")
    ent_07.grid(row=6, column=1, padx=3, pady=2, sticky="w")

    lbl_08.grid(row=7, column=0, padx=3, pady=2, sticky="e")
    ent_08.grid(row=7, column=1, padx=3, pady=2, sticky="w")

    lbl_09.grid(row=8, column=0, padx=3, pady=2, sticky="e")
    ent_09.grid(row=8, column=1, padx=3, pady=2, sticky="w")

    lbl_10.grid(row=9, column=0, padx=3, pady=2, sticky="e")
    ent_10.grid(row=9, column=1, padx=3, pady=2, sticky="w")

    btn_submit.grid(row=11, column=0, padx=3, pady=2)
    btn_clear.grid(row=11, column=1, padx=3, pady=2)
    btn_end.grid(row=11, column=2, padx=3, pady=2)

    red02 = red_var02.get()
    red03 = red_var03.get()
    red04 = red_var04.get()
    red05 = red_var05.get()
    red06 = red_var06.get()
    red07 = red_var07.get()
    red08 = red_var08.get()
    red09 = red_var09.get()
    red10 = red_var10.get()

    print(
        "red02: {}\nred03:{}\nred04: {}\nred05: {}\nred06: {}\nred07: {}\nred08: {}\nred09: {}\nred10: {}".format(
            red02, red03, red04, red05, red06, red07, red08, red09, red10))
    # This function is called each time the user releases a key.
    frm_main.mainloop()

    # def display_ent(event):

    # try:
    # Get the user input.

    # w2 = ent_02.get()
    # w3 = ent_03.get()
    # w4 = ent_04.get()
    # w5 = ent_05.get()
    # w6 = ent_06.get()
    # w7 = ent_07.get()
    # w8 = ent_08.get()
    # w9 = ent_09.get()
    # w10 = ent_10.get()

    # print(f"{w2}")
    # print(f"{w3}")
    # print(f"{w4}")
    # if w4 == 1:
    #     print("attendance")
    # else:
    #     print("missing")
    # Compute the tire volume in liters.
    # v = (math.pi * w *

    # When the user deletes all the digits in one
    # of the number entries, clear the result.
    #     w.config(text="")

    # This function is called each time
    # the user clicks the "Clear" button.

    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_02.clear()
        ent_03.clear()
        ent_04.clear()
        ent_05.clear()
        ent_06.clear()
        ent_07.clear()
        ent_08.clear()
        ent_09.clear()
        ent_10.clear()

        ent_02.focus()

    # ent_02.bind("<KeyRelease>", display_ent)
    # ent_03.bind("<KeyRelease>", display_ent)
    # ent_04.bind("<KeyRelease>", display_ent)
    # ent_05.bind("<KeyRelease>", display_ent)
    # ent_06.bind("<KeyRelease>", display_ent)
    # ent_07.bind("<KeyRelease>", display_ent)
    # ent_08.bind("<KeyRelease>", display_ent)
    # ent_09.bind("<KeyRelease>", display_ent)
    # ent_10.bind("<KeyRelease>", display_ent)

    btn_clear.config(command=clear)
    ent_02.focus()


# Give the keyboard focus to the width text field.
# ent_02.focus()
def message():
    try:
        pywhatkit.sendwhatmsg("+51940696481", "HOLA NENA", 20, 19)
        print("Abriendo... Escanee codigo QR")
        print("Enviado exitosamente")

    except:
        print("No se pudo encontrar")


# If this file is executed like this:
# > python teach_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()

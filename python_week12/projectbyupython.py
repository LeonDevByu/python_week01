import math
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry, FloatEntry
import pywhatkit


def main():
    # Create the Tk root object.
    root = tk.Tk()
    root.geometry("500x300")
    root.maxsize(500, 300)
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
    lbl_01 = Label(frm_main, text="Please enter your information:   Attendance: 1     Missing: 2 ", bg="lightgrey")
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
    ent_02 = IntEntry(frm_main, width=5, lower_bound=1, upper_bound=2)
    ent_03 = IntEntry(frm_main, width=5, lower_bound=1, upper_bound=2)
    ent_04 = IntEntry(frm_main, width=5, lower_bound=1, upper_bound=2)
    ent_05 = IntEntry(frm_main, width=5, lower_bound=1, upper_bound=2)
    ent_06 = IntEntry(frm_main, width=5, lower_bound=1, upper_bound=2)
    ent_07 = IntEntry(frm_main, width=5, lower_bound=1, upper_bound=2)
    ent_08 = IntEntry(frm_main, width=5, lower_bound=1, upper_bound=2)
    ent_09 = IntEntry(frm_main, width=5, lower_bound=1, upper_bound=2)
    ent_10 = IntEntry(frm_main, width=5, lower_bound=1, upper_bound=2)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")
    btn_send = Button(frm_main, text="Submit")
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

    btn_clear.grid(row=11, column=1, padx=3, pady=2)
    btn_send.grid(row=11, column=0, padx=3, pady=2)

    # This function is called each time the user releases a key.

    def display_ent(event):

        """Compute the approximate volume of a tire in liters."""

    # try:
        # Get the user input.
        w = ent_02.get()
        w = ent_03.get()
        w = ent_04.get()
        w = ent_05.get()
        w = ent_06.get()
        w = ent_07.get()
        w = ent_08.get()
        w = ent_09.get()
        w = ent_10.get()

        if w == 1:
            print("attendance")
        else:
            print("missing")
        # Compute the tire volume in liters.
        # v = (math.pi * w * w * a * (w * a + 2540 * d)) / 10_000_000_000

        # Display the volume rounded to one digit
        # after the decimal for the user to see.
        # w.config(text=f"")

    # except ValueError:

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

    btn_clear.config(command=clear)

    ent_02.bind("<KeyRelease>", display_ent)
    ent_03.bind("<KeyRelease>", display_ent)
    ent_04.bind("<KeyRelease>", display_ent)
    ent_05.bind("<KeyRelease>", display_ent)
    ent_06.bind("<KeyRelease>", display_ent)
    ent_07.bind("<KeyRelease>", display_ent)
    ent_08.bind("<KeyRelease>", display_ent)
    ent_09.bind("<KeyRelease>", display_ent)
    ent_10.bind("<KeyRelease>", display_ent)


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

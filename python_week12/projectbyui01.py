from tkinter import *
import tkinter as tk
import pywhatkit

root = Tk()
root.title("ATTENDANCE LIST OF THE QUORUM OF ELDERS")
root.geometry("450x500")  # set starting size of window
root.maxsize(450, 500)
root.config(bg="lightgrey")


def main():
    root = tk.Tk()
    atendance = 0
    INDEX0_0 = 0
    INDEX1_1 = 1
    INDEX_0 = 0
    INDEX_1 = 1
    INDEX_2 = 2
    INDEX_3 = 3
    INDEX_00_0 = 0
    INDEX_01_1 = 1

    message_01 = message()
    for i in message_01:
        E = i[INDEX_00_0]
        F = i[INDEX_01_1]
    print(f"{E}, {F}")
    list_total = display_checked()
    for i in list_total:
        X = i[INDEX0_0]
        Y = i[INDEX1_1]
        # print(i[1], i[2])
        print(f"{X}, {Y}")
        if Y == 1:
            periodic_table = make_table()
            for i in periodic_table:
                A = i[INDEX_0]
                B = i[INDEX_1]
                C = i[INDEX_2]
                D = i[INDEX_3]
                print(f"{A}, {B}, {C},{D}")

                if "X" == "A":
                    try:
                        pywhatkit.sendwhatmsg("C", "Hi", "D", "E", 20, 19)
                        print("Open... Scan QR code")
                        print("Sent successfully")

                    except:

                        print("Could not find")

        else:
            periodic_table = make_table()
            for i in periodic_table:
                A = i[INDEX_0]
                B = i[INDEX_1]
                C = i[INDEX_2]
                D = i[INDEX_3]
                print(f"{A}, {B}, {C},{D}")
                try:
                    pywhatkit.sendwhatmsg("C", "HOLA", "D", "F", 20, 19)
                    print("Open... Scan QR code")
                    print("Sent successfully")

                except:
                    print("Could not find")


def display_checked():
    '''check if the checkbuttons have been toggled, and display
    a value of '1' if they are checked, '0' if not checked'''
    red02 = red_var02.get()
    red03 = red_var03.get()
    red04 = red_var04.get()
    red05 = red_var05.get()
    red06 = red_var06.get()
    red07 = red_var07.get()
    red08 = red_var08.get()
    red09 = red_var09.get()
    red10 = red_var10.get()

    table_list = [["red02", red02], ["red03", red03], ["red04", red04], ["red05", red05], ["red06", red06],
                  ["red07", red07], ["red08", red08], ["red09", red09], ["red10", red10]]
    table = list(table_list)
    return table

    # print(
    #     "red02: {}\nred03:{}\nred04: {}\nred05: {}\nred06: {}\nred07: {}\nred08: {}\nred09: {}\nred10: {}".format(
    #         red02, red03, red04, red05, red06, red07, red08, red09, red10))

# Create label
lbl_01 = Label(root, text="Please enter your information:", bg="lightgrey")
lbl_01.grid(row=0)

lbl_02 = Label(root, text="León  Matías Edwin Leonardo :")
lbl_03 = Label(root, text="Benites Relaiza Alex Patricio :")
lbl_04 = Label(root, text="León   Matías   Javier   Luis :")
lbl_05 = Label(root, text="Rosas Rodriguez, Jean Pool :")
lbl_06 = Label(root, text="Cabellos Tineo, Eduardo Martin :")
lbl_07 = Label(root, text="Aranda Capcha, David Julian :")
lbl_08 = Label(root, text="Aranda Loayza, Jeffrey Robert :")
lbl_09 = Label(root, text="Ascarate Ortega, Armando :")
lbl_10 = Label(root, text="Asto Laupa, Julio Cesar :")
# Create variables and checkbuttons

red_var02 = IntVar()
red_var03 = IntVar()
red_var04 = IntVar()
red_var05 = IntVar()
red_var06 = IntVar()
red_var07 = IntVar()
red_var08 = IntVar()
red_var09 = IntVar()
red_var10 = IntVar()
ent_02 = Checkbutton(root, width=5, variable=red_var02, bg="grey")
ent_03 = Checkbutton(root, width=5, variable=red_var03, bg="darkgray")
ent_04 = Checkbutton(root, width=5, variable=red_var04, bg="grey")
ent_05 = Checkbutton(root, width=5, variable=red_var05, bg="darkgray")
ent_06 = Checkbutton(root, width=5, variable=red_var06, bg="grey")
ent_07 = Checkbutton(root, width=5, variable=red_var07, bg="darkgray")
ent_08 = Checkbutton(root, width=5, variable=red_var08, bg="grey")
ent_09 = Checkbutton(root, width=5, variable=red_var09, bg="darkgray")
ent_10 = Checkbutton(root, width=5, variable=red_var10, bg="grey")

btn_clear = Button(root, text="Clear")
btn_submit = Button(root, text="Submit", command=display_checked)
btn_end = Button(root, text="End", command=root.quit)
# Button(root, text="Tally", command=display_checked).grid(row=5)
# Button(root, text="End", command=root.quit).grid(row=6)
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

root.mainloop()


def make_table():
    table01_list = [

        ["red02", "León  Matías Edwin Leonardo", "+51940696481", "Edwin"],
        ["red03", "Benites Relaiza Alex Patricio", "+51940696481", "Alex"],
        ["red04", "León   Matías   Javier   Luis", "+51933172697", "Javier"],
        ["red05", "Rosas Rodriguez, Jean Pool", "+51933166559", "Jean"],
        ["red06", "Cabellos Tineo, Eduardo Martin", "+51940696481", "Eduardo"],
        ["red07", "Aranda Capcha, David Julian", "+51940696481", "David"],
        ["red08", "Aranda Loayza, Jeffrey Robert", "+51940696481", "Jeffrey"],
        ["red09", "Ascarate Ortega, Armando", "+51940696481", "Armando"],
        ["red10", "Asto Laupa, Julio Cesar", "+51940696481", "Julio"]
    ]

    table01 = list(table01_list)
    return table01


def message():
    messages = [
        ["Thank you for attending the conference and the quorum classes, we look forward to seeing you next Sunday."
            , "Hope you are well, we missed you in the classes today, hope to see you next Sunday."],
    ]

    menssage01 = list(messages)
    return menssage01

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

    btn_clear.config(command=clear)
    ent_02.focus()


if __name__ == "__main__":
    main()

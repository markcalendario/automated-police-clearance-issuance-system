
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\markc\Desktop\Programming\decode\new imp\build\assets\frame1")


def assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("992x594")
window.configure(bg = "#F5F5F5")


canvas = Canvas(
    window,
    bg = "#F5F5F5",
    height = 594,
    width = 992,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=69.0,
    y=293.0,
    width=258.0,
    height=235.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    992.0,
    76.0,
    fill="#003049",
    outline="")

image_image_1 = PhotoImage(
    file=assets("image_1.png"))
image_1 = canvas.create_image(
    93.0,
    38.0,
    image=image_image_1
)

canvas.create_text(
    128.0,
    29.0,
    anchor="nw",
    text="Police Clearance  Issuance System",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

button_image_2 = PhotoImage(
    file=assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=861.0,
    y=28.0,
    width=62.0,
    height=21.0
)

canvas.create_text(
    761.0,
    125.0,
    anchor="nw",
    text="10:08 PM",
    fill="#000000",
    font=("Inter Bold", 35 * -1)
)

canvas.create_text(
    69.0,
    150.0,
    anchor="nw",
    text="Mark Kenneth!",
    fill="#000000",
    font=("Inter Bold", 35 * -1)
)

canvas.create_text(
    743.0,
    167.0,
    anchor="nw",
    text="Today is Wednesday,\nJanuary 02, 2023",
    fill="#000000",
    font=("Inter Regular", 18 * -1)
)

canvas.create_text(
    69.0,
    125.0,
    anchor="nw",
    text="Welcome to the system,",
    fill="#000000",
    font=("Inter Regular", 18 * -1)
)

button_image_3 = PhotoImage(
    file=assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=665.0,
    y=293.0,
    width=258.0,
    height=235.0
)

button_image_4 = PhotoImage(
    file=assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=367.0,
    y=293.0,
    width=258.0,
    height=235.0
)
window.resizable(False, False)
window.mainloop()

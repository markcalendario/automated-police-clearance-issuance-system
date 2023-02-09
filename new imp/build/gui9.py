
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\markc\Desktop\Programming\decode\new imp\build\assets\frame9")


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
canvas.create_rectangle(
    0.0,
    0.0,
    992.0,
    76.0,
    fill="#003049",
    outline="")

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
    x=861.0,
    y=28.0,
    width=62.0,
    height=21.0
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
    x=759.0,
    y=28.0,
    width=62.0,
    height=21.0
)

canvas.create_text(
    128.0,
    29.0,
    anchor="nw",
    text="Police Clearance  Issuance System",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    69.0,
    106.0,
    anchor="nw",
    text="Manage Wanted List",
    fill="#000000",
    font=("Inter Bold", 30 * -1)
)

canvas.create_text(
    69.0,
    152.0,
    anchor="nw",
    text="Guides on importing face images of a wanted personalities:",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    535.0,
    281.0,
    anchor="nw",
    text="WANTED 10023",
    fill="#000000",
    font=("Inter Bold", 32 * -1)
)

canvas.create_text(
    605.0,
    354.0,
    anchor="nw",
    text="Remove From Wanted List",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
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
    x=535.0,
    y=412.0,
    width=388.0,
    height=53.0
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
    x=535.0,
    y=340.0,
    width=388.0,
    height=53.0
)

button_image_5 = PhotoImage(
    file=assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=535.0,
    y=484.0,
    width=388.0,
    height=53.0
)

image_image_1 = PhotoImage(
    file=assets("image_1.png"))
image_1 = canvas.create_image(
    201.0,
    413.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=assets("image_2.png"))
image_2 = canvas.create_image(
    93.0,
    38.0,
    image=image_image_2
)

canvas.create_text(
    69.0,
    199.0,
    anchor="nw",
    text="2. Dimension must be square.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    69.0,
    218.0,
    anchor="nw",
    text="3. Image must be cropped closely to the face.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    69.0,
    237.0,
    anchor="nw",
    text="4. Image must not be blury.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    69.0,
    178.0,
    anchor="nw",
    text="1. Image must be JPEG or PNG.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)
window.resizable(False, False)
window.mainloop()

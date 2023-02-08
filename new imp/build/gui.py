
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\markc\Desktop\Programming\decode\new imp\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("992x594")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 594,
    width = 992,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    627.0,
    0.0,
    992.0,
    594.0,
    fill="#003049",
    outline="")

canvas.create_text(
    730.0,
    230.0,
    anchor="nw",
    text="Police Clearance \nIssuance System",
    fill="#FFFFFF",
    font=("Inter Bold", 18 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    627.0,
    594.0,
    fill="#F6F6F6",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    454.0,
    297.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    808.5,
    374.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=677.0,
    y=356.0,
    width=263.0,
    height=34.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    808.5,
    449.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=677.0,
    y=431.0,
    width=263.0,
    height=35.0
)

canvas.create_text(
    677.0,
    338.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("Inter Regular", 12 * -1)
)

canvas.create_text(
    677.0,
    414.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Inter Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=676.8257446289062,
    y=490.9165344238281,
    width=262.88726806640625,
    height=37.7628173828125
)
window.resizable(False, False)
window.mainloop()


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\markc\Desktop\Programming\decode\build\assets\frame5")


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
canvas.create_text(
    69.0,
    106.0,
    anchor="nw",
    text="Verify a Clearance",
    fill="#000000",
    font=("Inter Bold", 30 * -1)
)

canvas.create_text(
    69.0,
    154.0,
    anchor="nw",
    text="Click the button below to verify a clearance by scanning the embedded QR Code in the document. Once verified, information will be shown on the form below.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

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
    y=204.0,
    width=357.0,
    height=57.0
)

canvas.create_text(
    634.0,
    223.0,
    anchor="nw",
    text="This certificate is valid until June 24, 2023",
    fill="#000000",
    font=("Inter Bold", 13 * -1)
)

canvas.create_text(
    69.0,
    283.0,
    anchor="nw",
    text="First Name",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    69.0,
    308.0,
    anchor="nw",
    text="First name will be shown here.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    572.0,
    308.0,
    anchor="nw",
    text="Birthday will be shown here.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    572.0,
    377.0,
    anchor="nw",
    text="Address will be shown here.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    572.0,
    446.0,
    anchor="nw",
    text="Place of birth will be shown here.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    572.0,
    515.0,
    anchor="nw",
    text="Purpose will be shown here.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    69.0,
    377.0,
    anchor="nw",
    text="Last name will be shown here.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    69.0,
    446.0,
    anchor="nw",
    text="Middle name will be shown here.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    69.0,
    515.0,
    anchor="nw",
    text="Suffix will be shown here.",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    69.0,
    352.0,
    anchor="nw",
    text="Last Name",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    69.0,
    421.0,
    anchor="nw",
    text="Middle Name",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    69.0,
    490.0,
    anchor="nw",
    text="Suffix",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    572.0,
    283.0,
    anchor="nw",
    text="Birthday (MM/DD/YYYY)",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    572.0,
    352.0,
    anchor="nw",
    text="Complete Address",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    572.0,
    421.0,
    anchor="nw",
    text="Place of Birth",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    572.0,
    490.0,
    anchor="nw",
    text="Purpose",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
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
    343.0,
    134.0,
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
    x=759.0,
    y=28.0,
    width=62.0,
    height=21.0
)
window.resizable(False, False)
window.mainloop()

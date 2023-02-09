from assets import assets
from fonts import fonts
from tkinter import Canvas, Button, PhotoImage, Toplevel

class image_match:
  def __init__(self, parent_frame, wanted_image):
    
    self.parent_frame = parent_frame
    self.window = Toplevel(self.parent_frame)
    self.window.geometry("992x594")
    self.window.configure(bg = "#F5F5F5")
    self.window.resizable(False, False)
    self.window.protocol("WM_DELETE_WINDOW",  self.handle_close)
    
    self.canvas = Canvas(
			self.window,
			bg = "#F5F5F5",
			height = 594,
			width = 992,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge"
		)

    self.canvas.place(x = 0, y = 0)
		
    self.canvas.create_rectangle(
			0.0,
			0.0,
			992.0,
			76.0,
			fill="#003049",
			outline=""
		)

    self.canvas.create_text(
			69.0,
			106.0,
			anchor="nw",
			text="{} Image Match".format(wanted_image.split('.')[0]),
			fill="#8D0000",
			font=(fonts.bold, 30 * -1)
		)

    self.canvas.create_text(
			69.0,
			152.0,
			anchor="nw",
			text="Take necessary action as soon as possible. Try again if this is false positive.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

    self.logo_img = PhotoImage(file=assets("image_match", "logo_img.png"))
    
    self.logo = self.canvas.create_image(
			503.0,
			35.0,
			image=self.logo_img
		)

    self.big_logo_img = PhotoImage(file=assets("image_match", "big_logo_img.png"))

    self.big_logo = self.canvas.create_image(
			503.0,
			356.0,
			image=self.big_logo_img
		)

    self.wanted_face_img = PhotoImage(file="./database/wanted_list/" + wanted_image)
    
    self.wanted_face = self.canvas.create_image(
			230.0,
			356.0,
			image=self.wanted_face_img
		)
    
    self.client_face_img = PhotoImage(file='./client.png')
		
    self.client_face = self.canvas.create_image(
    	774.0,
    	356.0,
    	image=self.client_face_img
		)
    
  def show(self):
    self.window.mainloop()
  
  def handle_close(self):
    self.window.withdraw()


from fonts import fonts
from sign_out import sign_out
import os
from tkinter import Canvas, Button, PhotoImage, Toplevel, filedialog
from tkinter.messagebox import askyesno, showerror, showinfo
from assets import assets
from face_model_processors import get_faces, has_one_face, zoom_to_client_face
from cv2 import imread, imwrite
from shutil import move
from time import time

class ManageWantedList:
	def __init__(self, parent_frame, root):
		self.parent_frame = parent_frame
		self.root = root
		
		self.window = Toplevel(self.parent_frame.window)
		self.window.geometry("992x594")
		self.window.configure(bg = "#F5F5F5")
		self.window.resizable(False, False)
		self.window.protocol("WM_DELETE_WINDOW", self.handle_close)

		self.selected_wanted_image_path = None

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

		self.sign_out_btn_img = PhotoImage(file=assets("manage_wanted_list", "sign_out_btn.png"))

		self.sign_out_btn = Button(
			self.window,
			image=self.sign_out_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=lambda: sign_out(self.root),
			relief="flat"
		)
		
		self.sign_out_btn.place(
			x=861.0,
			y=28.0,
			width=62.0,
			height=21.0
		)

		self.home_btn_image = PhotoImage(file=assets("manage_wanted_list", "home_btn.png"))
		
		self.home_btn = Button(
			self.window,
			image=self.home_btn_image,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_close,
			relief="flat"
		)

		self.home_btn.place(
			x=759.0,
			y=28.0,
			width=62.0,
			height=21.0
		)

		self.canvas.create_text(
			128.0,
			29.0,
			anchor="nw",
			text="Police Clearance Issuance System",
			fill="#FFFFFF",
			font=(fonts.bold, 14 * -1)
		)

		self.canvas.create_text(
			69.0,
			106.0,
			anchor="nw",
			text="Manage Wanted List",
			fill="#000000",
			font=(fonts.bold, 30 * -1)
		)

		self.canvas.create_text(
			69.0,
			152.0,
			anchor="nw",
			text="Guides on importing face images of a wanted personalities:",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.image_filename_preview = self.canvas.create_text(
			535.0,
			281.0,
			anchor="nw",
			text="FILENAME",
			fill="#000000",
			font=(fonts.bold, 20 * -1)
		)

		self.canvas.create_text(
			605.0,
			354.0,
			anchor="nw",
			text="Remove From Wanted List",
			fill="#FFFFFF",
			font=(fonts.bold, 20 * -1)
		)

		self.remove_wanted_image_btn_img = PhotoImage(file=assets("manage_wanted_list", "remove_wanted_image_btn.png"))
		
		self.remove_wanted_image_btn = Button(
			self.window,
			image=self.remove_wanted_image_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_remove_wanted_image,
			relief="flat"
		)

		self.remove_wanted_image_btn.place(
			x=535.0,
			y=340.0,
			width=388.0,
			height=53.0
		)

		self.import_wanted_image_btn_img = PhotoImage(file="./assets/manage_wanted_list/import_wanted_image_btn.png")
		
		self.import_wanted_image_btn = Button(
			self.window,
			image=self.import_wanted_image_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_import_wanted_image,
			relief="flat"
		)

		self.import_wanted_image_btn.place(
			x=535.0,
			y=400.0,
			width=388.0,
			height=53.0
		)

		self.wanted_image = PhotoImage(file=assets("manage_wanted_list", "wanted_image_placeholder.png"))
		
		self.wanted_preview = self.canvas.create_image(
			230.0,
			413.0,
			image=self.wanted_image
		)

		self.logo = PhotoImage(file=assets("manage_wanted_list", "logo.png"))
		
		self.canvas.create_image(
			93.0,
			38.0,
			image=self.logo
		)
		
		self.canvas.create_text(
			69.0,
			178.0,
			anchor="nw",
			text="1. Image must be JPEG or PNG.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.canvas.create_text(
			69.0,
			199.0,
			anchor="nw",
			text="2. Dimension may not be square.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.canvas.create_text(
			69.0,
			218.0,
			anchor="nw",
			text="3. Image must have the face in it and not blurry.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

	def start(self):
		self.parent_frame.hide()
		self.window.mainloop()
	
	def show(self):
		self.window.deiconify()

	def hide(self):
		self.window.withdraw()

	def handle_close(self):
		self.hide()
		self.parent_frame.show()

	def handle_import_wanted_image(self):
		selected_image_path = filedialog.askopenfile(
			initialdir="./database/wanted_list", 
			filetypes=[("Wanted file", "*.jpg;*.jpeg;*.png")])

		if selected_image_path == None:
			return
		
		selected_image_path = selected_image_path.name
		
		if not os.path.exists(selected_image_path):
			showerror("Error", "Image file does not exists.")
			return
		
		image = imread(selected_image_path)
		faces = get_faces(image)
		
		if not len(faces):
			showerror("Error", "No face detected. Please make sure that it is a photo of a person.")
			return
		
		if not has_one_face(faces):
			showerror("Error", "The image contains number of faces less or more than 1.")
			return

		resized, cropped_image = zoom_to_client_face(faces[0], image)
		if not resized:
			showerror("Error", "Can't process the image. Please make sure that the face is in the center.")
			return
		
		imwrite(".temp_preview.png", cropped_image)
	
		self.wanted_image.configure(file=".temp_preview.png")
		self.change_filename_preview(selected_image_path)
		
		self.toggle_button_state()
		response = askyesno("Are you sure?", "Do you really want to import this image as a wanted?")
		self.toggle_button_state()
		self.reset_previews()

		if not response:
			os.remove(".temp_preview.png")
			showinfo("Importation Cancelled", "Importation of the selected wanted image cancelled.")
			return
		
		wanted_image_new_filename = f"WANTED_{str(time()).split('.')[0]}"
		move(".temp_preview.png", f"./database/wanted_list/{wanted_image_new_filename}.png")
		showinfo("Success", f"{wanted_image_new_filename} imported successfully.")

	def toggle_button_state(self):
		is_enabled = self.import_wanted_image_btn["state"] == "normal" or self.remove_wanted_image_btn["state"] == "enabled"

		if is_enabled:
			self.import_wanted_image_btn.config(state="disabled")
			self.remove_wanted_image_btn.config(state="disabled")
			return
		
		self.import_wanted_image_btn.config(state="normal")
		self.remove_wanted_image_btn.config(state="normal")

	def reset_previews(self):
		self.change_filename_preview()
		self.wanted_image.configure(file=assets("manage_wanted_list", "wanted_image_placeholder.png"))

	def change_filename_preview(self, selected_image_path=None):
		filename = "FILENAME"
		
		if selected_image_path != None:
			filename = os.path.basename(selected_image_path).split(".")[0][:30]
			
		self.canvas.itemconfig(self.image_filename_preview, text=filename)
		
	def handle_remove_wanted_image(self):
		selected_image_path = filedialog.askopenfile(
			initialdir="./database/wanted_list", 
			filetypes=[("Wanted file", "*.jpg;*.jpeg;*.png")])
		
		if selected_image_path == None: return

		selected_image_path = selected_image_path.name

		if not os.path.exists(selected_image_path):
			showerror("Error", "File does not exists.")
			return
		
		in_wanted_list_dir = "wanted_list" in selected_image_path
		
		if not in_wanted_list_dir:
			showerror("Error", "You cannot remove files outside from wanted list folder.")
			return 

		self.wanted_image.configure(file=selected_image_path)
		self.change_filename_preview(selected_image_path)

		self.toggle_button_state()
		response = askyesno("Are you sure?", "Do you really want to delete this wanted image?")
		self.toggle_button_state()
		self.reset_previews()
		
		if not response:
			showinfo("Deletion Cancelled", "Wanted image deletion cancelled.")
			return
		
		os.remove(selected_image_path)
		showinfo("Success", "Wanted image deleted successfully.")

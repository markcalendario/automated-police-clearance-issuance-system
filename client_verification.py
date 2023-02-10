from fonts import fonts
import os
from face_recognition import load_image_file, face_encodings, compare_faces
from tkinter import Canvas, Button, PhotoImage, Toplevel, messagebox
from image_match import image_match
from face_model_processors import capture_client_face
from assets import assets
from sign_out import sign_out
from clearance_form import ClearanceForm

class clearance_verification:
	def __init__(self, parent_frame, root):

		self.root = root
		self.parent_frame = parent_frame
		self.window = Toplevel(self.parent_frame.window)
		self.window.geometry("992x594")
		self.window.protocol("WM_DELETE_WINDOW",  self.handle_close)
		self.window.wm_title("Police Clearance Issuance System")
		self.window.configure(bg = "#F5F5F5")
		self.window.resizable(False, False)

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

		# region Result Button

		self.waiting_btn_img = PhotoImage(file=assets("clearance_verification", "waiting_result_img.png"))

		self.failed_btn_img = PhotoImage(file=assets("clearance_verification", "failed_result_img.png"))
		
		self.passed_btn_img = PhotoImage(file=assets("clearance_verification", "passed_result_img.png"))

		self.result_btn = Button(
			self.window,
			image=self.waiting_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_waiting_btn_click,
			relief="flat"
		)

		self.result_btn.place(
				x=520.0,
				y=281.0,
				width=403.0,
				height=277.0
		)

		# endregion Result Button

		# region Start Verification Button

		self.start_verification_btn_img = PhotoImage(file=assets("clearance_verification", "start_verification_btn.png"))
		
		self.start_verification_btn = Button(
			self.window,
			image=self.start_verification_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_start_verification,
			relief="flat"
		)

		self.start_verification_btn.place(
			x=69.0,
			y=281.0,
			width=403.0,
			height=277.0
		)

		# endregion Start Verification Button

		# region Sign Out Button

		self.sign_out_btn_image = PhotoImage(file=assets("clearance_verification", "sign_out_btn.png"))
		
		self.sign_out_btn = Button(
			self.window,
			image=self.sign_out_btn_image,
			borderwidth=0,
			highlightthickness=0,
			command=lambda: sign_out(self.root),
			relief="flat"
		)

		self.sign_out_btn.place(
			x=874.0,
			y=26.0,
			width=62.0,
			height=21.0
		)

		# endregion Sign Out Button

		# region Home Button

		self.home_btn_img = PhotoImage(file=assets("clearance_verification", "home_btn.png"))

		self.home_btn = Button(
				self.window,
				image=self.home_btn_img,
				borderwidth=0,
				highlightthickness=0,
				command=self.handle_close,
				relief="flat"
		)

		self.home_btn.place(
				x=772.0,
				y=26.0,
				width=62.0,
				height=21.0
		)

		# endregion Home Button

		self.canvas.create_rectangle(
			0.0,
			0.0,
			992.0,
			76.0,
			fill="#003049",
			outline=""
		)

		self.canvas.create_text(
			128.0,
			29.0,
			anchor="nw",
			text="Police Clearance  Issuance System",
			fill="#FFFFFF",
			font=(fonts.bold, 14 * -1)
		)

		self.canvas.create_text(
			69.0,
			106.0,
			anchor="nw",
			text="Create a Clearance",
			fill="#000000",
			font=(fonts.bold, 30 * -1)
		)

		self.canvas.create_text(
			104.0,
			156.0,
			anchor="nw",
			text="Wanted Verification",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.canvas.create_text(
			320.0,
			156.0,
			anchor="nw",
			text="Client Information",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.canvas.create_text(
			508.0,
			156.0,
			anchor="nw",
			text="Issuance",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.nav_guide_dots_img = PhotoImage(file=assets("clearance_verification", "guide_dots.png"))
		
		self.nav_guide_dots = self.canvas.create_image(
			283.0,
			96.0,
			image=self.nav_guide_dots_img
		)

		self.canvas.create_text(
				69.0,
				237.0,
				anchor="nw",
				text="2. Once checked and the client is not on the wanted list, get the client information.",
				fill="#000000",
				font=("fonts.regular", 14 * -1)
		)

		self.canvas.create_text(
				69.0,
				256.0,
				anchor="nw",
				text="3. Issue a clearance.",
				fill="#000000",
				font=("fonts.regular", 14 * -1)
		)

		self.canvas.create_text(
				69.0,
				216.0,
				anchor="nw",
				text="1. Verify first the client to check if he/she is on the wanted list.",
				fill="#000000",
				font=("fonts.regular", 14 * -1)
		)

		self.canvas.create_text(
				69.0,
				193.0,
				anchor="nw",
				text="Steps in creating a clearance.",
				fill="#000000",
				font=(fonts.bold, 14 * -1)
		)

	def handle_waiting_btn_click(self):
		messagebox.showinfo("Verification Guide", "Please start getting the face model of the client for verification.")

	def is_face_wanted(self):
		wanted_list_dir = './database/wanted_list'
		wanted_list = os.listdir(wanted_list_dir)

		client_face = load_image_file('./client_temporary_files/client.png')
		client_face_encoding = None

		try:
			client_face_encoding = face_encodings(client_face)[0]
		except IndexError:
			messagebox.showerror("Verification Guide", "Face is unrecognizable. Try again.")

		for wanted in wanted_list:
			if not wanted.endswith(".png"):
				continue

			wanted_face = load_image_file(os.path.join(wanted_list_dir, wanted))
			result = []

			try:
				wanted_face_encoding = face_encodings(wanted_face)[0]
				result = compare_faces([wanted_face_encoding], client_face_encoding, tolerance=0.45)
			except:
				print("Face not found in image [{}]".format(wanted))

			if any(result) and len(result) != 0:
				return wanted

		return False
		
	def change_result_btn(self, type, wanted=None):

		image = None
		command = None
		
		if type == "FAILED":
			image = self.failed_btn_img
			command = lambda: self.handle_failed_btn_click(wanted)
		elif type == "PASSED":
			image = self.passed_btn_img
			command = lambda: self.handle_passed_btn_click()
		elif type == "WAITING":
			image = self.waiting_btn_img
			command = lambda: self.handle_waiting_btn_click()

		self.result_btn.configure(image=image, command=command)

	def handle_start_verification(self):
		is_face_captured = capture_client_face()
		self.change_result_btn("WAITING")
		
		if not is_face_captured:
			return messagebox.showwarning("Face Verification.", "Face verification is not successful. Try again to proceed.")
		
		messagebox.showinfo("Face Verification", "Client image has been successfully saved. Please wait for verification result.")

		wanted = self.is_face_wanted()

		if wanted:
			return self.handle_wanted_match(wanted)
		
		self.change_result_btn("PASSED")

	def handle_passed_btn_click(self):
		ClearanceForm(self, self.root).start()

	def handle_wanted_match(self, wanted):
		self.change_result_btn("FAILED", wanted)
		image_match(self.window, wanted).show()

	def handle_failed_btn_click(self, wanted):
		image_match(self.window, wanted).show()
		
	def start(self):
		self.parent_frame.hide()
		self.window.mainloop()

	def show(self):
		self.reset_face_verification_result()
		self.window.deiconify()

	def hide(self):
		self.window.withdraw()

	def handle_close(self):
		self.parent_frame.show()
		self.hide()

	def reset_face_verification_result(self):
		self.change_result_btn("WAITING")

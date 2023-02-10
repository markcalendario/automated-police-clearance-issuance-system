from tkinter import Canvas, Entry, Button, PhotoImage, Toplevel
from tkinter.messagebox import showerror, askyesno
from assets import assets
from sign_out import sign_out
from fonts import fonts
from datetime import datetime
from time import time, localtime
import qrcode
from admin import admin
from issuance_area import IssuanceArea

class ClearanceForm:
	def __init__(self, parent_frame, root):
		self.parent_frame = parent_frame
		self.root = root

		self.clearance_number = self.generate_clearance_number()
		
		self.window = Toplevel(self.parent_frame.window)
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
		
		self.canvas.create_text(
			69.0,
			106.0,
			anchor="nw",
			text=f"Create a Clearance [{self.clearance_number}]",
			fill="#000000",
			font=(fonts.bold, 30 * -1)
		)
		
		self.canvas.create_text(
			104.0,
			158.0,
			anchor="nw",
			text="Wanted Verification",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.canvas.create_text(
			320.0,
			158.0,
			anchor="nw",
			text="Client Information",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.canvas.create_text(
			508.0,
			158.0,
			anchor="nw",
			text="Issuance",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.canvas.create_text(
			69.0,
			218.0,
			anchor="nw",
			text="First Name",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.firstname_entry = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.firstname_entry.place(
				x=69.0,
				y=239.0,
				width=351.0,
				height=32.0
		)
		
		self.canvas.create_text(
				69.0,
				287.0,
				anchor="nw",
				text="Last Name",
				fill="#000000",
				font=(fonts.bold, 14 * -1)
		)
		
		self.lastname_entry = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.lastname_entry.place(
				x=69.0,
				y=308.0,
				width=351.0,
				height=32.0
		)
		
		self.canvas.create_text(
			69.0,
			356.0,
			anchor="nw",
			text="Middle Name",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.middlename_entry = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.middlename_entry.place(
			x=69.0,
			y=377.0,
			width=351.0,
			height=32.0
		)
		
		self.canvas.create_text(
			69.0,
			425.0,
			anchor="nw",
			text="Suffix",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.suffix_entry = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.suffix_entry.place(
			x=69.0,
			y=446.0,
			width=351.0,
			height=32.0
		)
		
		self.canvas.create_text(
			572.0,
			218.0,
			anchor="nw",
			text="Birthdate (MM/DD/YYYY)",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.birthdate_entry = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.birthdate_entry.place(
			x=572.0,
			y=239.0,
			width=351.0,
			height=32.0
		)
		
		self.canvas.create_text(
			572.0,
			287.0,
			anchor="nw",
			text="Complete Address",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.address_entry = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.address_entry.place(
			x=572.0,
			y=308.0,
			width=351.0,
			height=32.0
		)
		
		self.canvas.create_text(
			572.0,
			356.0,
			anchor="nw",
			text="Place of Birth",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.birth_place_entry = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.birth_place_entry.place(
			x=572.0,
			y=377.0,
			width=351.0,
			height=32.0
		)
		
		self.canvas.create_text(
			572.0,
			425.0,
			anchor="nw",
			text="Purpose",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.purpose_entry = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.purpose_entry.place(
			x=572.0,
			y=446.0,
			width=351.0,
			height=32.0
		)
		
		self.finalize_btn_img = PhotoImage(file=assets("clearance_form", "finalize_btn.png"))
		
		self.finalize_btn = Button(
			self.window,
			image=self.finalize_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_finalize_btn_click,
			relief="flat"
		)
		
		self.finalize_btn.place(
			x=69.0,
			y=512.0,
			width=854.0,
			height=59.0
		)
		
		self.canvas.create_rectangle(
			0.0,
			0.0,
			992.0,
			76.0,
			fill="#003049",
			outline=""
		)
		
		self.guide_dots_img = PhotoImage(file=assets("clearance_form", "guide_dots.png"))
		
		self.guide_dots = self.canvas.create_image(
			283.0,
			97.0,
			image=self.guide_dots_img
		)
		
		self.canvas.create_text(
			128.0,
			29.0,
			anchor="nw",
			text="Police Clearance Issuance System",
			fill="#FFFFFF",
			font=(fonts.bold, 14 * -1)
		)
		
		self.sign_out_btn_img = PhotoImage(file=assets("clearance_form", "sign_out_btn.png"))
		
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
			y=26.0,
			width=62.0,
			height=21.0
		)
		
		self.home_btn_img = PhotoImage(file=assets("clearance_form", "home_btn.png"))
		
		home_btn = Button(
			self.window,
			image=self.home_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_close,
			relief="flat"
		)
		
		home_btn.place(
			x=759.0,
			y=26.0,
			width=62.0,
			height=21.0
		)
		
	def start(self):
		self.parent_frame.hide() 
		self.window.mainloop()
		
	def hide(self):
		self.window.withdraw()

	def show(self): 
		self.window.deiconify()

	def handle_close(self):
		self.hide()
		self.parent_frame.show()

	def validate_entries(self):
		self.first_name = self.firstname_entry.get().strip()
		self.last_name = self.lastname_entry.get().strip()
		self.middle_name = self.middlename_entry.get().strip()
		self.suffix = self.suffix_entry.get().strip()
		self.birthdate = self.birthdate_entry.get().strip()
		self.address = self.address_entry.get().strip()
		self.birth_place = self.birth_place_entry.get().strip()
		self.purpose = self.purpose_entry.get().strip()

		if self.first_name == "":
			return False, "First name is empty."
		
		if self.last_name == "":
			return False, "Last name is empty"
		
		if self.middle_name == "":
			return False, "Middle name is empty."
		
		if self.birthdate == "":
			return False, "Birthdate is empty."
		
		try:
			datetime.strptime(self.birthdate, "%m/%d/%Y")
		except:
			return False, "Date format is not acceptable."
		
		if self.address == "":
			return False, "Address is empty."
		
		if self.birth_place == "":
			return False, "Birth place is empty."

		if self.purpose == "":
			return False, "Purpose is empty."
		
		return True, "Valid"

	def generate_clearance_number(self):
		now = datetime.now()
		clearance_number = now.strftime('%m%d%Y_%H%M%S')
		return f"CLRNC_{clearance_number}"

	def save_clearance_record(self):
		clearance_data_str = f"NAME={self.first_name} {self.middle_name} {self.last_name} {self.middle_name}\nADDRESS={self.address}\nBIRTHDATE={self.birthdate}\nBIRTHPLACE={self.birth_place}\nPURPOSE={self.purpose}\n"

		file = open(f"./database/clearance_list/{self.clearance_number}.txt", "w")
		file.write(clearance_data_str)
		file.close()	

	def generate_printable_clearance(self):
		file = open("./clearance_template/clearance.html", "r")
		content = file.read()
		content = content.replace("%FULLNAME%", f"{self.first_name} {self.middle_name} {self.last_name} {self.suffix}")
		content = content.replace("%ADDRESS%", self.address)
		content = content.replace("%BIRTHDATE%", self.birthdate)
		content = content.replace("%BIRTHPLACE%", self.birth_place)
		content = content.replace("%PURPOSE%", self.purpose)
		content = content.replace("%NUMBER%", self.clearance_number)
		content = content.replace("%VERIFIER NAME%", admin.get_name())
		file.close()

		file = open("./client_temporary_files/clearance.html", "w")
		file.write(content)
		file.close()

	def generate_qr_code(self):
		qr = qrcode.make(self.clearance_number)
		qr.save("./client_temporary_files/qrcode.png")

	def handle_finalize_btn_click(self):
		inputs_valid, message = self.validate_entries()

		if not inputs_valid: 
			showerror("Error", message)
			return
		
		response = askyesno("Are you sure?", f"Do you really want to finalize {self.clearance_number}?")

		if not response:
			return
		
		self.save_clearance_record()
		self.generate_printable_clearance()
		self.generate_qr_code()

		IssuanceArea(self, self.root).start()

		

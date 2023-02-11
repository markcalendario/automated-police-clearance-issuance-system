import os
from tkinter import Toplevel, Canvas, Button, PhotoImage, filedialog
from assets import assets
from fonts import fonts
from sign_out import sign_out
from qrcode_processors import start_qrcode_scan
from tkinter.messagebox import showwarning, showerror, showinfo, askyesno
from enum import Enum
from datetime import datetime, timedelta
class ClearanceStatusEnum(Enum):
	REVOKED = -2
	EXPIRED = -1
	INVALID = 0
	VALID = 1

class ManageClearanceList:
	def __init__(self, parent_frame, root):
		self.root = root
		self.parent_frame = parent_frame

		self.window = Toplevel(parent_frame.window)
		self.window.geometry("992x594")
		self.window.configure(bg = "#F5F5F5")
		self.window.resizable(False, False)
		self.window.protocol("WM_DELETE_WINDOW", self.handle_close)
		self.window.wm_title("Police Clearance Issuance System")

		self.clearance_code = None
		self.clearance_expiry = None
		self.clearance_status = None

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
		
		self.title = self.canvas.create_text(
			69.0,
			106.0,
			anchor="nw",
			text="Manage Clearance",
			fill="#000000",
			font=(fonts.bold, 30 * -1)
		)

		self.canvas.create_text(
			69.0,
			154.0,
			anchor="nw",
			text="Click the button below to verify a clearance by scanning the embedded QR Code in the document. \nOnce verified, status and information will be shown below.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.scan_clearance_btn_img = PhotoImage(file=assets("manage_clearance_list", "scan_clearance_btn.png"))

		self.scan_clearance_btn = Button(
			self.window,
			image=self.scan_clearance_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_scan_clearance_button_click,
			relief="flat"
		)

		self.scan_clearance_btn.place(
			x=69.0,
			y=204.0,
			width=141.32533264160156,
			height=47.66595458984375
		)

		self.select_clearance_btn_img = PhotoImage(file=assets("manage_clearance_list", "select_clearance_btn.png"))

		self.select_clearance_btn = Button(
			self.window,
			image=self.select_clearance_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_select_clearance_button_click,
			relief="flat"
		)

		self.select_clearance_btn.place(
			x=222.0,
			y=204.0,
			width=141.3253173828125,
			height=47.66595458984375
		)

		self.revoke_clearance_btn_img = PhotoImage(file=assets("manage_clearance_list", "revoke_clearance_btn.png"))
		
		self.revoke_clearance_btn = Button(
			self.window,
			image=self.revoke_clearance_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_revoke_button_click,
			relief="flat"
		)

		self.check_img = PhotoImage(file=assets("manage_clearance_list", "check.png"))
		self.error_img = PhotoImage(file=assets("manage_clearance_list", "error.png"))
		
		self.verification_result_icon = self.canvas.create_image(
			595.0,
			228.0,
			image=""
		)

		self.status_description = self.canvas.create_text(
			634.0,
			220.0,
			anchor="nw",
			text="",
			fill="#000000",
			font=(fonts.bold, 13 * -1)
		)

		self.canvas.create_text(
			69.0,
			283.0,
			anchor="nw",
			text="First Name",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.first_name = self.canvas.create_text(
			69.0,
			308.0,
			anchor="nw",
			text="First name will be shown here.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.canvas.create_text(
			69.0,
			352.0,
			anchor="nw",
			text="Last Name",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.last_name = self.canvas.create_text(
			69.0,
			377.0,
			anchor="nw",
			text="Last name will be shown here.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.canvas.create_text(
			69.0,
			421.0,
			anchor="nw",
			text="Middle Name",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.middle_name = self.canvas.create_text(
			69.0,
			446.0,
			anchor="nw",
			text="Middle name will be shown here.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.canvas.create_text(
			69.0,
			490.0,
			anchor="nw",
			text="Suffix",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.suffix = self.canvas.create_text(
			69.0,
			515.0,
			anchor="nw",
			text="Suffix will be shown here.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.canvas.create_text(
			572.0,
			283.0,
			anchor="nw",
			text="Birthday (MM/DD/YYYY)",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.birthdate = self.canvas.create_text(
			572.0,
			308.0,
			anchor="nw",
			text="Birthdate will be shown here.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.canvas.create_text(
			572.0,
			352.0,
			anchor="nw",
			text="Complete Address",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.address = self.canvas.create_text(
			572.0,
			377.0,
			anchor="nw",
			text="Address will be shown here.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.canvas.create_text(
			572.0,
			421.0,
			anchor="nw",
			text="Place of Birth",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.birth_place = self.canvas.create_text(
			572.0,
			446.0,
			anchor="nw",
			text="Place of birth will be shown here.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.canvas.create_text(
			572.0,
			490.0,
			anchor="nw",
			text="Purpose",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)

		self.purpose = self.canvas.create_text(
			572.0,
			515.0,
			anchor="nw",
			text="Purpose will be shown here.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.canvas.create_rectangle(
			0.0,
			0.0,
			992.0,
			76.0,
			fill="#003049",
			outline="")

		self.icon = PhotoImage(file=assets("global", "logo_img.png"))
		
		self.canvas.create_image(
			93.0,
			38.0,
			image=self.icon
		)

		self.canvas.create_text(
			128.0,
			29.0,
			anchor="nw",
			text="Police Clearance Issuance System",
			fill="#FFFFFF",
			font=(fonts.bold, 14 * -1)
		)

		self.sign_out_img = PhotoImage(file=assets("global", "sign_out_btn.png"))
		
		self.sign_out_btn = Button(
			self.window,
			image=self.sign_out_img,
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

		self.home_btn_img = PhotoImage(file=assets("global", "home_btn.png"))
		
		self.home_btn = Button(
			self.window,
			image=self.home_btn_img,
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

	def start(self):
		self.parent_frame.hide()
		self.window.mainloop()

	def hide(self):
		self.window.withdraw()

	def show(self):
		self.window.deiconify()

	def handle_close(self):
		self.parent_frame.show()
		self.hide()

	def is_clearance_exists(self):
		try:
			clearance = open(f"./database/clearance_list/{self.clearance_code}.txt", "r")
			clearance.close()
		except:
			return False
		
		return True
	
	def is_clearance_revoked(self):
		clearance = open(f"./database/clearance_list/{self.clearance_code}.txt", "r")
		clearance_data = clearance.readlines()
		clearance.close()

		is_revoked = None

		for data in clearance_data:
			if "REVOKED" in data:
				is_revoked = int(data.split("=", 1)[1])
				break

		if is_revoked:
			return True
		
		return False
	
	def is_clearance_expired(self):
		now = datetime.now()
		expiration_date = self.get_expiration_date()

		if now > expiration_date:
			return True
		
		return False
	
	def display_clearance_data(self):
		clearance = open(f"./database/clearance_list/{self.clearance_code}.txt", "r")
		clearance_data = clearance.readlines()
		clearance.close()

		firstname = clearance_data[0].split("=", 1)[1]
		middlename = clearance_data[1].split("=", 1)[1]
		lastname = clearance_data[2].split("=", 1)[1]
		suffix = clearance_data[3].split("=", 1)[1]
		address = clearance_data[4].split("=", 1)[1]
		birthdate = clearance_data[5].split("=", 1)[1]
		birthplace = clearance_data[6].split("=", 1)[1]
		purpose = clearance_data[7].split("=", 1)[1]
		
		self.canvas.itemconfigure(self.first_name, text=firstname)
		self.canvas.itemconfigure(self.middle_name, text=middlename)
		self.canvas.itemconfigure(self.last_name, text=lastname)
		self.canvas.itemconfigure(self.suffix, text=suffix)
		self.canvas.itemconfigure(self.birthdate, text=birthdate)
		self.canvas.itemconfigure(self.birth_place, text=birthplace)
		self.canvas.itemconfigure(self.address, text=address)
		self.canvas.itemconfigure(self.purpose, text=purpose)

	def get_clearance_status(self):

		if not self.is_clearance_exists():
			return ClearanceStatusEnum.INVALID.value

		if self.is_clearance_revoked():
			return ClearanceStatusEnum.REVOKED.value

		if self.is_clearance_expired():
			return ClearanceStatusEnum.EXPIRED.value
		
		return ClearanceStatusEnum.VALID.value

	def place_revoke_button(self):
		self.revoke_clearance_btn.place(
			x=374.0,
			y=204.0,
			width=156.0,
			height=47.66595458984375
		)
	
	def unplace_revoke_button(self):
		self.revoke_clearance_btn.place_forget()

	def reset_clearance_verification_state(self):
		self.clearance_expiry = None
		self.clearance_code = None
		self.clearance_status = None

		self.unplace_revoke_button()
		self.canvas.itemconfigure(self.status_description, text="")
		self.canvas.itemconfigure(self.title, text="Manage Clearance")
		self.canvas.itemconfigure(self.verification_result_icon, image="")

		self.canvas.itemconfigure(self.first_name, text="-")
		self.canvas.itemconfigure(self.middle_name, text="-")
		self.canvas.itemconfigure(self.last_name, text="-")
		self.canvas.itemconfigure(self.suffix, text="-")
		self.canvas.itemconfigure(self.birthdate, text="-")
		self.canvas.itemconfigure(self.birth_place, text="-")
		self.canvas.itemconfigure(self.address, text="-")
		self.canvas.itemconfigure(self.purpose, text="-")

	def show_clearance_verification_result(self):
		status = self.clearance_status
		description = ""
		icon = self.error_img

		if status == ClearanceStatusEnum.INVALID.value:
			description = "No records found for this clearance."

		if status == ClearanceStatusEnum.REVOKED.value:
			description = "This clearance was revoked."

		if status == ClearanceStatusEnum.EXPIRED.value:
			description = f"This clearance expired in {self.clearance_expiry}."
		
		if status == ClearanceStatusEnum.VALID.value:
			description = f"This clearance is valid until {self.clearance_expiry}."
			icon = self.check_img
		
		# Show description

		self.canvas.itemconfigure(self.status_description, text=description)
		self.canvas.itemconfigure(self.verification_result_icon, image=icon)

	def get_expiration_date(self):
		clearance_number_date = self.clearance_code.split("_")[1]
		date_in_clearance_number = datetime.strptime(clearance_number_date, "%m%d%Y")
		return date_in_clearance_number + timedelta(days=180)

	def handle_scan_clearance_button_click(self):
		self.reset_clearance_verification_state()
		clearance_number = start_qrcode_scan()

		if not clearance_number:
			showwarning("Warning", "Clearance scanning did not finish.")
			return

		self.verify_clearance_status(clearance_number)

	def handle_revoke_button_click(self):
		response = askyesno("Are you sure?", f"Do you really want to revoke {self.clearance_code}?")

		if not response:
			return
		
		clearance = None
		clearance_data = None
		try:
			clearance = open(f"./database/clearance_list/{self.clearance_code}.txt", "r")
			clearance_data = clearance.read()
			clearance.close()
		except FileNotFoundError:
			showerror("Error", f"Document {self.clearance_code} not found!")
			return
		
		clearance = open(f"./database/clearance_list/{self.clearance_code}.txt", "w")		
		clearance_data = clearance_data.replace("REVOKED=0", "REVOKED=1")
		clearance.write(clearance_data)
		clearance.close()

		showinfo("Success", f"{self.clearance_code} has been revoked successfully.")
		self.reset_clearance_verification_state()

	def handle_select_clearance_button_click(self):
		clearance_file_path = filedialog.askopenfile(
			initialdir="./database/clearance_list", 
			filetypes=[("Clearance file", "*.txt")])
		
		if not clearance_file_path:
			return 
		
		clearance_file_path = clearance_file_path.name
		clearance_file_base_name = os.path.basename(clearance_file_path)

		if not clearance_file_base_name.endswith(".txt"):
			showerror("File error", "File type is not acceptable.")
			return
		
		comes_from_database = "clearance_list" in clearance_file_path
		has_two_underscore = clearance_file_base_name.count("_") == 2
		has_clrnc_identifier = clearance_file_base_name.count("CLRNC_")

		if not comes_from_database:
			showerror("File error", "This file does not come from the clearance database.")
			return

		if not has_clrnc_identifier:
			showerror("File error", "Invalid clearance file naming format. [CLRNC Error]")
			return

		if not has_two_underscore:
			showerror("File error", "Invalid clearance file naming format. [Separator Error]")
			return
		
		if not self.has_valid_file_name_date(clearance_file_base_name):
			showerror("File error", "Invalid clearance file naming format. [Date Error]")
			return

		self.verify_clearance_status(clearance_file_base_name.replace(".txt", ""))

	def has_valid_file_name_date(self, clearance_code:str):
		try:
			datetime.strptime(clearance_code.split("_")[1], "%m%d%Y")
		except:
			return False
		
		return True

	def verify_clearance_status(self, clearance_number):
		self.clearance_code = clearance_number
		self.clearance_status = self.get_clearance_status()

		if self.clearance_status == ClearanceStatusEnum.INVALID.value:
			self.show_clearance_verification_result()
			return

		if self.clearance_status == ClearanceStatusEnum.VALID.value:
			self.place_revoke_button()
		

		self.canvas.itemconfigure(self.title, text=f"Result for {self.clearance_code}") 
		self.clearance_expiry = datetime.strftime(self.get_expiration_date(), "%b. %d, %Y")
		self.display_clearance_data()
		self.show_clearance_verification_result()

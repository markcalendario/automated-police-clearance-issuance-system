from tkinter import Toplevel, Canvas, Button, PhotoImage
from assets import assets
from fonts import fonts
from sign_out import sign_out

class ClearanceStatusEnum:
	REVOKED: -2
	EXPIRED: -1
	INVALID: 0
	VALID: 0

class ManageClearanceList:
	def __init__(self, parent_frame, root):
		self.root = root
		self.window = Toplevel(parent_frame.window)
		
		self.window.geometry("992x594")
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
		
		self.canvas.create_text(
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
			text="Click the button below to verify a clearance by scanning the embedded QR Code in the document. Once verified, information will be shown below.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
		)

		self.verify_clearance_btn_img = PhotoImage(file=assets("manage_clearance_list", "verify_clearance_btn.png"))

		self.verify_clearance_btn = Button(
			self.window,
			image=self.verify_clearance_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=lambda: print("button_1 clicked"),
			relief="flat"
		)

		self.verify_clearance_btn.place(
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
			command=lambda: print("button_2 clicked"),
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
			command=lambda: print("button_3 clicked"),
			relief="flat"
		)

		self.check_img = PhotoImage(file=assets("manage_clearance_list", "check.png"))
		self.error_img = PhotoImage(file=assets("manage_clearance_list", "error.png"))
		
		self.verification_result_icon = self.canvas.create_image(
			595.0,
			228.0,
			image=""
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
			command=lambda: print("button_4 clicked"),
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
			command=lambda: print("button_5 clicked"),
			relief="flat"
		)

		self.home_btn.place(
			x=759.0,
			y=28.0,
			width=62.0,
			height=21.0
		)

	def start(self):
		self.window.mainloop()
		self.parent_frame.hide()

	def place_revoke_button(self):
		self.revoke_clearance_btn.place(
			x=374.0,
			y=204.0,
			width=156.0,
			height=47.66595458984375
		)
	
	def unplace_revoke_button(self):
		self.revoke_clearance_btn.place_forget()

	def show_clearance_verification_result(self, result_type, description):
	
		# Show description
		self.result_description = self.canvas.create_text(
			634.0,
			220.0,
			anchor="nw",
			text=description,
			fill="#000000",
			font=(fonts.bold, 13 * -1)
		)
		
		# Show status icon
		icon = self.check_img
		if result_type in [status.value for status in ClearanceStatusEnum]:
			icon = self.error_img

		self.canvas.itemconfig(self.verification_result_icon, image=icon)



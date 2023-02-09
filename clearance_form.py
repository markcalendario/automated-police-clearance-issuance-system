from tkinter import Canvas, Entry, Button, PhotoImage, Toplevel
from assets import assets
from sign_out import sign_out
from fonts import fonts

class ClearanceForm:
	def __init__(self, parent_frame, root):
		self.parent_frame = parent_frame
		self.root = root
		
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
			text="Create a Clearance",
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
		
		self.surname_entry = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.surname_entry.place(
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
		
		self.entry_2 = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.entry_2.place(
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
		
		self.entry_3 = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.entry_3.place(
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
		
		self.entry_4 = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.entry_4.place(
			x=69.0,
			y=446.0,
			width=351.0,
			height=32.0
		)
		
		self.canvas.create_text(
			572.0,
			218.0,
			anchor="nw",
			text="Birthday (MM/DD/YYYY)",
			fill="#000000",
			font=(fonts.bold, 14 * -1)
		)
		
		self.entry_5 = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.entry_5.place(
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
		
		self.entry_6 = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.entry_6.place(
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
		
		self.entry_7 = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.entry_7.place(
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
		
		self.entry_8 = Entry(
			self.window,
			bd=5,
			bg="#DEDEDE",
			fg="#000000",
			highlightthickness=2,
			relief="flat"
		)
		
		self.entry_8.place(
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
			command=lambda: print("Finalize"),
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


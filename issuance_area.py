from tkinter import Toplevel, Canvas, Button, PhotoImage
from assets import assets
from sign_out import sign_out
import webbrowser
import os
from fonts import fonts

class IssuanceArea:
	def __init__(self, parent_frame, root):
		self.parent_frame = parent_frame
		self.root = root

		self.window = Toplevel(parent_frame.window)
		self.window.geometry("992x594")
		self.window.configure(bg = "#F5F5F5")
		self.window.resizable(False, False)
		self.window.protocol("WM_DELETE_WINDOW",  self.handle_close)
		self.window.iconbitmap("./assets/global/favicon.ico")
		
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
			69.0,
			210.0,
			anchor="nw",
			text="CLRNC_4005_23058 is ready!",
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
			69.0,
			260.0,
			anchor="nw",
			text="Clearance certificate is now ready. You can now print the certificate by clicking the button below. \nThe browser will open then press CTRL + P to print the clearance.",
			fill="#000000",
			font=(fonts.regular, 14 * -1)
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

		self.print_clearance_btn_img = PhotoImage(file=assets("clearance_printing_area", "print_clearance_btn.png"))
		
		self.print_clearance_btn = Button(
			self.window,
			image=self.print_clearance_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_print_btn_click,
			relief="flat"
		)
		
		self.print_clearance_btn.place(
			x=69.0,
			y=308.0,
			width=854.0,
			height=263.0
		)

		self.canvas.create_rectangle(
			0.0,
			0.0,
			992.0,
			76.0,
			fill="#003049",
			outline=""
		)

		self.guide_dots_img = PhotoImage(file=assets("clearance_printing_area", "guide_dots.png"))
		
		self.guide_dots = self.canvas.create_image(
			283.0,
			96.0,
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

		self.sign_out_btn_img = PhotoImage(file=assets("clearance_printing_area", "sign_out_btn.png"))
		
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

		self.home_btn_img = PhotoImage(file=assets("clearance_printing_area", "home_btn.png"))
		
		self.home_btn = Button(
			self.window,
			image=self.home_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_home_click,
			relief="flat"
		)

		self.home_btn.place(
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

	def handle_close(self):
		self.parent_frame.show()
		self.hide()

	def handle_home_click(self):
		self.hide()
		self.parent_frame.handle_close()

	def handle_print_btn_click(self):
		try:
			webbrowser.open(os.path.join(os.path.dirname(__file__), "client_temporary_files/clearance.html"))
		except:
			print("No browser.")

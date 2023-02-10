import time
import threading
from fonts import fonts
from admin import admin
from sign_out import sign_out
from assets import assets
from manage_wanted_list import ManageWantedList
from client_verification import ClientVerification
from manage_clearance_list import ManageClearanceList
from tkinter import Canvas, Button, PhotoImage, Toplevel

class landing_screen:
	def __init__(self, root):

		# Initialization of Frame Properties
		self.root = root
		self.window = Toplevel(self.root.window)
		self.window.geometry("992x594")
		self.window.configure(bg = "#F5F5F5")
		self.window.protocol("WM_DELETE_WINDOW",  lambda: None)
		self.window.wm_title("Police Clearance Issuance System")
		self.window.resizable(False, False)

		# Initialize Application Design and Layout

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
		
		# region Give Clearance Button

		self.give_clearance_btn_img = PhotoImage(file=assets("landing", "give_clearance_btn.png"))
		
		self.give_clearance_btn = Button(
			self.window,
			image=self.give_clearance_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_show_give_clearance,
			relief="flat"
		)

		self.give_clearance_btn.place(
			x=69.0,
			y=293.0,
			width=258.0,
			height=235.0
		)

		# endregion Give Clearance Button

		# region Verify Clearance Button

		self.manage_clearance_btn_img = PhotoImage(file=assets("landing", "manage_clearance_btn.png"))
		
		self.manage_clearance_btn = Button(
			self.window,
			image=self.manage_clearance_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_manage_clearance_list_btn_click,
			relief="flat"
		)

		self.manage_clearance_btn.place(
			x=367.0,
			y=293.0,
			width=258.0,
			height=235.0
		)

		# endregion Verify Clearance Button

		# region Manage Wanted List Button

		self.manage_wanted_list_btn_img = PhotoImage(file=assets("landing", "manage_wanted_list_btn.png"))
		
		self.manage_wanted_list_btn = Button(
			self.window,
			image=self.manage_wanted_list_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_manage_wanted_list_btn_click,
			relief="flat"
		)

		self.manage_wanted_list_btn.place(
			x=665.0,
			y=293.0,
			width=258.0,
			height=235.0
		)

		# endregion Manage Wanted List Button

		# region Sign Out Button

		self.sign_out_btn_img = PhotoImage(file=assets("landing", "sign_out_btn.png"))
		
		self.sign_out_btn = Button(
			self.window,
			image=self.sign_out_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_signout,
			relief="flat"
		)

		self.sign_out_btn.place(
			x=861.0,
			y=28.0,
			width=62.0,
			height=21.0
		)
		# endregion Sign Out Button

		self.canvas.create_rectangle(
			0.0,
			0.0,
			992.0,
			76.0,
			fill="#003049",
			outline=""
		)

		self.logo_image = PhotoImage(file=assets("landing", "logo.png"))
		
		self.logo = self.canvas.create_image(
			93.0,
			38.0,
			image=self.logo_image
		)

		self.canvas.create_text(
			128.0,
			29.0,
			anchor="nw",
			text="Police Clearance Issuance System",
			fill="#FFFFFF",
			font=(fonts.bold, 14 * -1)
		)

		self.clock = self.canvas.create_text(
			920.0,
			155.0,
			anchor="e",
			text="",
			fill="#000000",
			font=(fonts.bold, 35 * -1)
		)

		self.canvas.create_text(
			69.0,
			150.0,
			anchor="nw",
			text='{}!'.format(admin.get_name()),
			fill="#000000",
			font=(fonts.bold, 35 * -1)
		)

		self.day_name = self.canvas.create_text(
			920.0,
			190.0,
			anchor="e",
			text="",
			fill="#000000",
			font=(fonts.regular, 18 * -1)
		)
		
		self.date = self.canvas.create_text(
			920.0,
			215.0,
			anchor="e",
			text="",
			fill="#000000",
			font=(fonts.regular, 18 * -1)
		)

		self.canvas.create_text(
			69.0,
			135.0,
			anchor="nw",
			text="Welcome to the system,",
			fill="#000000",
			font=(fonts.regular, 18 * -1)
		)

		self.update_time()

	def update_time(self):
		time_string = time.strftime("%I:%M:%S %p", time.localtime())
		name_of_day = time.strftime("%A", time.localtime())
		date_string = time.strftime("%B %d, %Y")

		self.canvas.itemconfigure(self.clock, text=time_string)
		self.canvas.itemconfigure(self.day_name, text="Today is {},".format(name_of_day))
		self.canvas.itemconfigure(self.date, text=date_string)

		self.timer = threading.Timer(1, self.update_time)
		self.timer.start()

	def start(self):
		self.root.hide()
		self.window.mainloop()

	def show(self):
		self.update_time()
		self.window.deiconify()

	def hide(self):
		self.timer.cancel()
		self.window.withdraw()

	def handle_signout(self):
		self.timer.cancel()
		sign_out(self.root)

	def handle_show_give_clearance(self):
		ClientVerification(self, self.root).start()

	def handle_manage_wanted_list_btn_click(self):
		ManageWantedList(self, self.root).start()

	def handle_manage_clearance_list_btn_click(self):
		ManageClearanceList(self, self.root).start()	

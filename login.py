from assets import assets
from landing import landing_screen
from fonts import fonts
from admin import admin
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

class login_screen:
	def __init__(self):

		# Initialize App Frame Properties

		self.window = Tk()
		self.window.geometry("992x594")
		self.window.configure(bg = "#FFFFFF")
		self.window.resizable(False, False)
		self.window.wm_title("Police Clearance Issuance System")

		# Initialize Application Design and Layout

		self.canvas = Canvas(
			self.window,
			bg = "#FFFFFF",
			height = 594,
			width = 992,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge"
		)

		self.canvas.place(x = 0, y = 0)
		
		self.canvas.create_rectangle(
			627.0,
			0.0,
			992.0,
			594.0,
			fill="#003049",
			outline=""
		)

		self.canvas.create_text(
			725.0,
			230.0,
			anchor="nw",
			text="Police Clearance \nIssuance System",
			fill="#FFFFFF",
			font=(fonts.bold, 18 * -1)
		)

		self.canvas.create_rectangle(
			0.0,
			0.0,
			627.0,
			594.0,
			fill="#F6F6F6",
			outline=""
		)

		self.frame_graphics_image = PhotoImage(file=assets("login_screen","frame_graphics_image.png"))
		
		self.frame_graphics = self.canvas.create_image(
			454.0,
			297.0,
			image=self.frame_graphics_image
		)

		# region Username Input Field

		self.username_input = Entry(
			border=5,
			bg="#D9D9D9",
			fg="#000716",
			highlightthickness=0,
			relief="flat"
		)
		
		self.username_input.place(
			x=677.0,
			y=356.0,
			width=263.0,
			height=34.0
		)
		
		self.canvas.create_text(
			677.0,
			338.0,
			anchor="nw",
			text="Username",
			fill="#FFFFFF",
			font=(fonts.regular, 12 * -1)
		)

		# endregion

		# region Password Input Field

		self.password_input = Entry(
			border=5,
			bg="#D9D9D9",
			fg="#000716",
			show="●",
			highlightthickness=0,
			relief="flat"
		)

		self.password_input.place(
			x=677.0,
			y=431.0,
			width=263.0,
			height=35.0
		)

		self.canvas.create_text(
			677.0,
			414.0,
			anchor="nw",
			text="Password",
			fill="#FFFFFF",
			font=(fonts.regular, 12 * -1)
		)

		# endregion Password Input Field

		# region Sign In Button

		self.sign_btn_img = PhotoImage(file=assets("login_screen", "sign_in_btn.png"))
		
		self.sign_in_button = Button(
			self.window,
			image=self.sign_btn_img,
			borderwidth=0,
			highlightthickness=0,
			command=self.handle_login_click,
			relief="flat"
		)
		
		self.sign_in_button.place(
			x=676.8257446289062,
			y=490.9165344238281,
			width=262.88726806640625,
			height=37.7628173828125
		)
		# endregion Sign In
		return

	def start_app(self):
		self.window.mainloop()

	def reset_credential_fields(self):
		self.username_input.delete(0, len(self.username_input.get()))
		self.password_input.delete(0, len(self.password_input.get()))

	def handle_login_click(self):

		try:
			file = open("database/login_credential.txt")
		except:
			file = open("database/login_credential.txt", "w")
			file.write("username:<username>\npassword:<password>\n")
			file.close()

		file = open("database/login_credential.txt", 'r')
		data = file.readlines()
		file.close()
		is_logged_in = False

		for data in data:
			line_data = data.split(";")
			username = line_data[0].split(":")[1]
			password = line_data[1].split(":")[1]
			name = line_data[2].split(":")[1].replace('\n', '')

			if username == self.username_input.get() and password == self.password_input.get():
				is_logged_in = True
			
		self.reset_credential_fields()

		if is_logged_in:
			admin.set_name(name)
			return landing_screen(self).start()
		
		return messagebox.showerror("Invalid Credentials", "Sorry, neither the username nor the password you have entered matched from the database entries.")

	def show(self):
		self.window.deiconify()

	def hide(self):
		self.window.withdraw()
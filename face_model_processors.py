from cv2 import destroyAllWindows, VideoCapture, rectangle, putText, FONT_HERSHEY_SIMPLEX, CascadeClassifier, cvtColor, COLOR_BGR2GRAY, CASCADE_SCALE_IMAGE, resize, imwrite, imshow, waitKey, CAP_DSHOW, INTER_AREA, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, namedWindow, resizeWindow, WINDOW_NORMAL
import global_vars
from tkinter import messagebox

def get_available_camera_device():

	for i in range(0, 11):
		camera = VideoCapture(i, CAP_DSHOW)

		if camera.isOpened():
			camera.release()
			return i
		
	return -1

def draw_camera_guides(frame):
	x, y, w, h = 0, 0, 200, 70

	# Draw black background rectangle
	rectangle(frame, (x, x), (x + w, y + h), (0, 0, 0), -1)
	
	# Add texts
	putText(frame, "[SPACE] to capture.", (x + 20, y + 20), FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
	putText(frame, "[ESC] to exit.", (x + 20, y + 50), FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

def get_faces(frame):

	faceCascade = CascadeClassifier(global_vars.face_model_location)

	gray = cvtColor(frame, COLOR_BGR2GRAY)
	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags = CASCADE_SCALE_IMAGE
	)
	
	return faces

def draw_face_rectangle(faces, frame):
	for (x, y, w, h) in faces:
		rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

def has_one_face(faces):
	return len(faces) == 1


def zoom_to_client_face(face, frame):
	x, y, w, h = face

	try:
		cropped = frame[y - 60:y + h + 60, x - 60:x + w + 60]
		processed_image = resize(cropped, (323, 323))
		return True, processed_image
	except:
		return False, None

def save_capture(image):
	imwrite("client_temporary_files/client.png", image)

def capture_client_face():

	original_frame = None
	faces = None
	camera_index = get_available_camera_device()

	if camera_index == -1:
		messagebox.showinfo("Face Verification", "No camera detected. Please make sure that you have available camera.")
		return False

	cam = VideoCapture(camera_index, CAP_DSHOW)

	while True:
		capturing, frame = cam.read()

		if not capturing:
			cam.release()
			destroyAllWindows()
			messagebox.showwarning("Face Verification", "The camera seems not working. Please try again.")
			return False
		
		original_frame = frame.copy()
		draw_camera_guides(frame)
		faces = get_faces(frame)
		draw_face_rectangle(faces, frame)

		imshow("Client Verification Camera", frame)

		# Key Listeners
		key = waitKey(1) & 0xFF
		
		if key == 27 or key == 32:
			cam.release()
			destroyAllWindows()

		if key == 27: # Esc key
			messagebox.showwarning("Face Verification", "Client face verification aborted.")
			return False
		
		elif key == 32: # Space key
			break

	if not has_one_face(faces):
		messagebox.showwarning("Face Verification", "Camera frame must detect one face.")
		return False
	
	resized, final_client_image = zoom_to_client_face(faces[0], original_frame)
	
	if not resized:
		messagebox.showerror("Face Verification", "Failed to process image. Please make sure that the face is in the center.")
		return False
	
	save_capture(final_client_image)

	return True

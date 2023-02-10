import global_vars
from tkinter import messagebox
from cv2 import destroyAllWindows, rectangle, CascadeClassifier, cvtColor, COLOR_BGR2GRAY, CASCADE_SCALE_IMAGE, resize, imwrite, imshow, waitKey
from camera import open_camera, display_cam_key_guides

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

def draw_rectangle_on_face(faces, frame):
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
	imwrite("./client_temporary_files/client.png", image)

def capture_client_face():

	original_frame = None
	faces = None

	cam = open_camera()

	while True:
		capturing, frame = cam.read()

		if not capturing:
			cam.release()
			destroyAllWindows()
			messagebox.showwarning("Face Verification", "The camera seems not working. Please try again.")
			return False
		
		original_frame = frame.copy()
		display_cam_key_guides(frame)
		faces = get_faces(frame)
		draw_rectangle_on_face(faces, frame)

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

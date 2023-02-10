from cv2 import VideoCapture, CAP_DSHOW, putText, FONT_HERSHEY_SIMPLEX, rectangle

def display_cam_key_guides(frame):
	x, y, w, h = 0, 0, 200, 70

	# Draw black background rectangle
	rectangle(frame, (x, x), (x + w, y + h), (0, 0, 0), -1)
	
	# Add texts
	putText(frame, "[SPACE] to capture.", (x + 20, y + 20), FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
	putText(frame, "[ESC] to exit.", (x + 20, y + 50), FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

def get_available_camera_device():

	for i in range(0, 11):
		camera = VideoCapture(i, CAP_DSHOW)

		if camera.isOpened():
			camera.release()
			return i
		
	return -1

def open_camera():
	camera_index = get_available_camera_device()

	if camera_index == -1:
		return False
	
	return VideoCapture(camera_index, CAP_DSHOW)
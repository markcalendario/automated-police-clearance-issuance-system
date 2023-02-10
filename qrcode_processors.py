import qrcode
from camera import open_camera, display_cam_key_guides
from tkinter.messagebox import showerror, showwarning
from cv2 import imshow, destroyAllWindows, waitKey, rectangle, QRCodeDetector, COLOR_BGR2GRAY, cvtColor

def get_qr_data(frame):
	detector = QRCodeDetector()
	data = bbox = None
	
	try:
		data, bbox, _ = detector.detectAndDecode(frame)
	except:
		return None, None

	return data, bbox

def draw_rectangle_on_qr(frame, qr_pos):
	# Or else, get the position of the QR code and parse it from float into int
	point_1 = [int(point_1_floats) for point_1_floats in qr_pos[0][0]]
	point_2 = [int(point_2_floats) for point_2_floats in qr_pos[0][2]]
		
	# Draw a rectangle on the QR code position
	rectangle(frame, point_1, point_2, (0, 255, 0), 2)

def start_qrcode_scan():
	qr_data = None
	cam = open_camera()
	
	while True:
		capturing, frame = cam.read()

		if not capturing:
			cam.release()
			showerror("Camera Error", "The camera does not capturing frames.")
			return False
		
		display_cam_key_guides(frame)

		gray = cvtColor(frame, COLOR_BGR2GRAY)		
		qr_data, qr_pos = get_qr_data(gray)
		
		if qr_data:
			draw_rectangle_on_qr(frame, qr_pos)

		imshow("Clearance QR Scanner", frame)

		# Key Listeners
		key = waitKey(1) & 0xFF

		if not qr_data and key == 32:
			showwarning("Clearance QR Verification", "The current frame cannot detect QR code. Please press [SPACE] only if there's QR on the frame.")
			continue

		if key == 27: # Esc key
			qr_data = None
			showwarning("Clearance QR Verification", "Clearance verification aborted.")
			break
		
		elif key == 32:
			break

	cam.release()
	destroyAllWindows()

	return qr_data
	

	
	
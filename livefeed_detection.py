import cv2, requests, time  

import argparse
import imutils
from imutils.video import VideoStream

import pyttsx3


def predict_sign(frame, url):
	"""
	Function to return the response JSON from Deepstack's server
	containing the confidence, label and bbox's coordinates.

	params
		frame 		each image frame of the live video
		url 		Deepstack server's localhost URL

	returns
		prediction	JSON response from the server
	"""
	s = time.time()
	response = requests.post(url, files={"image": frame}).json()
	e = time.time()
	print(f"Inferences took: {e -s} seconds.")
	print(response)

	if "success" in response and response['success'] and len(response['predictions']) > 0:
		prediction = response['predictions'][0]
		for object in response["predictions"]:
			print(object["label"])
	else: 
		prediction = None
	return prediction


if __name__ == '__main__':
	# construct the argument parser and parse the arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("--deepstack-port", 
						type=str,
						default=88,
						help="url to the deepstack server's docker image")
	args = vars(parser.parse_args())

	deepstack_url = f"http://localhost:{args['deepstack_port']}/v1/vision/custom/best"

	# initialize the video stream and allow the camera sensor to warm up
	print("[INFO] starting video stream...")
	stream = VideoStream(src=0).start()
	time.sleep(2.0)

	color = (0, 255, 0)

	#initialize the Text-to-speech engine
	text_engine = pyttsx3.init()

	# loop over the frames from the video stream
	while True:	
		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 400 pixels
		frame = stream.read() 
		frame = imutils.resize(frame, width=400)
		success, encoded_image = cv2.imencode('.jpg', frame)
		source_image = content2 = encoded_image.tobytes()

		print("Predict...")
		prediction = predict_sign(source_image, deepstack_url)
		
		label = ''
		if prediction is not None:
			confidence = prediction['confidence']
			label = prediction['label']
			y_min = prediction['y_min']
			y_max = prediction['y_max']
			x_min = prediction['x_min']
			x_max = prediction['x_max']

			# display the label and bounding box rectangle on the output
			# frame 
			cv2.putText(frame, f"{label} {confidence}", (x_min, y_min - 10),
						cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
			cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 2)
		cv2.imshow("Frame", frame)

		# convert to sound
		if label:
			text = label
			text_engine.say(text)
			text_engine.runAndWait()
			
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key was pressed, break from loop
		if key == ord("q"):
			break

# do a bit of cleanup
cv2.destroyAllWindows()
stream.stop()
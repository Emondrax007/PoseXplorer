# Import necessary libraries
import cv2
from cvzone.PoseModule import PoseDetector
import send  # Assuming 'send.py' contains SMS sending functionality

# Create a PoseDetector object for pose detection
detector = PoseDetector()

# Initialize the webcam capture
cap = cv2.VideoCapture(0)

# Set the resolution of the webcam to 640x480
cap.set(3, 640)
cap.set(4, 480)

# Initialize an empty list to keep track of human detections
l = []

# Initialize a flag to control SMS sending
flag = True

# Enter an infinite loop to continuously process webcam frames
while True:
    # Read a frame from the webcam
    success, img = cap.read()

    # Detect and draw human poses on the frame
    img = detector.findPose(img)

    # Find the positions of specific body parts
    imlist, bbox = detector.findPosition(img)

    # Check if any body parts were detected
    if len(imlist) > 0:
        print("Human Detected")
        l.append(1)

    # Check if there have been more than 50 detections and the flag is still True
    if len(l) > 50 and flag:
        flag = False  # Set the flag to False to prevent multiple SMS sends
        send.sendSms()  # Call the sendSms() function to send an SMS

    # Display the frame with detected poses
    cv2.imshow("Output", img)

    # Wait for a key press and break the loop if 'q' is pressed
    q = cv2.waitKey(1)
    if q == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

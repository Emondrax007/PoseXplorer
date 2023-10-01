
# PoseXplorer

PoseXplorer is a real-time human pose detection system that uses OpenCV and the cvzone library. It captures video from a webcam, detects human poses in each frame, and sends an SMS alert when a human has been detected in more than 50 frames.

## Features
- Real-time human pose detection using a webcam.
- SMS alert system that triggers after detecting a human in more than 50 frames.
- Uses OpenCV for video capture and display.
- Uses the cvzone library's PoseDetector module for pose detection.

## Requirements
- Python 3.x
- OpenCV
- cvzone

## Installation
1. Clone this repository.
2. Install the necessary libraries using pip:
```bash
pip install opencv-python
pip install cvzone
```
3. Ensure you have a file named `send.py` that contains the functionality to send an SMS.

## Usage
1. Run the script:
```bash
   main.py
```
2. The script will start capturing video from your webcam and display it in an OpenCV window.
3. If a human is detected in the video, their pose will be drawn on the frame and "Human Detected" will be printed in the console.
4. If a human is detected in more than 50 frames, an SMS will be sent.

## Note
This script assumes that you have a file named `send.py` which contains a function `sendSms()` for sending an SMS. You need to provide this file and function yourself.

## License
This project is licensed under the terms of the MIT license.


# Home Security System Using Computer Vision and Email Alerts
This repository contains the code for an innovative home security system that utilizes computer vision techniques to detect intruders and send real-time email alerts. The project integrates video capture, human detection, and automated email notifications to provide a robust and efficient security solution for residential properties.

# Features
Real-time Video Capture: Continuously captures video from a webcam using OpenCV.
Intruder Detection: Employs a Histogram of Oriented Gradients (HOG) descriptor with a pre-trained people detector to identify intruders accurately.
Automated Email Alerts: Sends email notifications with text, image, and video attachments to alert homeowners of potential intrusions.
Optional Raspberry Pi Integration: Includes GPIO code for use with sensors on a Raspberry Pi, enhancing system versatility.
Efficient Resource Management: Manages frame capture, processing, and email dispatch seamlessly.


# Programming Language: 
- Python
  
# Libraries:
- OpenCV: For video capture and image processing
- NumPy: For numerical operations
- smtplib and email MIME: For email communication
- timeit: For performance timing

# Hardware:
- Webcam
- Optional: Raspberry Pi with GPIO sensor integration


# Usage
Start the System:
- Run the script and follow the on-screen instructions to input the initial sensor state.
- The system will continuously monitor for intruders.


Intruder Detection:
- If an intruder is detected, the system captures a frame, processes it to detect people, and highlights them with rectangles.
- An initial alert email is sent when an intruder is detected for the first time.

Email Alerts:
- If the timer exceeds a threshold, the system crops the detected region, saves it as an image, and sends emails with the cropped image and video file as attachments.

# Optional: Raspberry Pi Integration
- Uncomment the GPIO-related code and set up the GPIO pins on your Raspberry Pi for sensor input.
- Ensure you have the necessary permissions and dependencies installed for GPIO usage.

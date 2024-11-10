


Real-Time Color Space Converter using OpenCV

Overview: 
This project demonstrates real-time color space conversion of video streams or images using OpenCV. It allows users to switch between various color spaces, including RGB, HSV, LAB to visualize how different representations of color appear in real-time.

Features: 

Real-Time Video Conversion: Converts live video feed between various color spaces.
Supported Color Spaces: RGB, HSV, LAB
Image and Video Compatibility: Works only with webcam feed
Dynamic Color Space Switching: Change the color space while the application is running.
Installation and Setup: 

Prerequisites: 
Python 3.x
OpenCV (for image processing)
NumPy (for numerical computations)

Installation:
Clone the repository:
bash
Copy code
git clone <your-repository-link>
cd color-space-converter
Install required packages:
bash
Copy code
pip install opencv-python numpy
Usage: 
Running the Application: 
To start the real-time color space converter, use the following command:

bash
Copy code
python color_space_converter.py
Switching Color Spaces
Once running, you can switch between color spaces by pressing specific keys:

R- RGB
H - HSV
L- LAB


For example, pressing H will convert the video feed to the HSV color space.



Technical Details
The project utilizes OpenCV's cv2.cvtColor function to convert frames to different color spaces. The cv2.VideoCapture class captures video from the default camera, and each frame is processed individually for color space conversion.

Color space conversions include:

BGR to RGB: cv2.COLOR_BGR2RGB
BGR to HSV: cv2.COLOR_BGR2HSV
BGR to LAB: cv2.COLOR_BGR2LAB




References
OpenCV Documentation
NumPy Documentation

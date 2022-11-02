# REAL-TIME-MOTION-CAPTURE-SURVAILLANCE-SYSTEM-USING-FIREBASE

## ABSTRACT:

 Many emerging motion-related applications, such as virtual
reality, decision making, and health monitoring, demand reliability and
quick response upon input changes. Motion capture has been a wellresearched topic in the past decades with applications in many
industries. The ability to capture motion goes hand in hand with realtime capability in a system. This project gives an overview on real-time
motion capture, including frameworks, recording devices, and
algorithms. Using real-time motion capture as a tool to solve
application problems is also described. Through the years, Surveillance
included the observation from a distance by recording the captured
content by means of electronic equipment, such as closed-circuit
television (CCTV)

## PROJECT DEMO
[![image](https://user-images.githubusercontent.com/46374770/199302523-ca8a8446-eaa0-4d20-8c64-0c4ebce3ed63.png)](https://youtu.be/zWaPGsf4tB4)


## INTRODUCTION:
### NEED:
 Motion detection is the detection of the change in the position of
an object with respect to its surroundings and vice-versa. CCTV
cameras continuously record the situations. Hence there is unnecessary
memory wastage if there is nothing is happening in front of the camera.
Also the CCTV system does not provide alerts of burglary happening at
particular time. So there is a need of a system which will record the
situation only if there is some movement happening in front of the
camera. Object tracking is an important component of many vision
systems. It is used not only for visual surveillance, but also for
augmented reality, traffic control, medical imaging, gesture recognition,
etc. Here, an automated video surveillance system for real-time security
system is implemented. Here a single camera for detecting the human
motion and tracking it over time.
### OBJECTIVE:
 The main goal is to detect the object efficiently using
background subtraction techniques, which aims to reduce the cost and
to increase efficiency. This Security system presents a novel and simple
method for moving object detection. The human object is captured; a
database (server) is used to store the captured images and viewed
through remote login. Whenever human movement is captured by the
camera it is immediately detected and the object is tracked by Frame
difference method. Detection of moving object from a sequence of
frames captured from a static camera is widely performed by frame
difference method. The objective of the approach is to detect the
moving objects from the difference between the existing frame and the
reference frame. After determination of differences, in order to find an
image which shows the rate of movement, motion point must be
classified in categories. To do this, first define the moving points to be
recognized in image. Motion point is the point for which the rate of its
whitening in difference image is more than threshold rate. The inputs
from camera are continuous. Initially a particular time interval is
6
defined for generating frames called as frame interval.

## TOOLS USED:
* PYTHON
* OPEN CV
* FIREBASE
* BASE64


![image](https://user-images.githubusercontent.com/46374770/194746863-6a5cb958-4d6f-4cac-a7c7-ac525a7ba746.png) ![image](https://user-images.githubusercontent.com/46374770/194746942-6f77314c-9956-4afd-b02b-5d314a21068f.png)


## APPROACH:
When the program starts, we will capture a picture
called baseline image. This is the image without any object or
intruder. Our program will keep comparing the new frame with this
baseline image. If nobody enters or exits the frame, there will be no
difference. However, when somebody enters the frame, the contents of
the image will be different and if this difference is beyond a certain
threshold, our program will treat it as an intruder. First we will convert
the image to gray scale and soften (blur) the image using a Low Pass
Filter (LPF). A LPF is generally used in image processing to smoothen
the image (used in skin smoothening, background blurring) and a High
Pass Filter (HPF) is used to sharpen the image (sharpening of eyes and
other details). This helps to increase the accuracy by removing the
noise. The next step is to deduce the difference between the baseline
and the new frame. If a particular pixel value is greater than a certain
threshold, it will be assigned the value for White (255) else Black (0).
Now we have an image which has only 2 types of pixels (pure black or
pure white, nothing in between). This is done so that we can identify
10
the contour region around our detected object. Now we will find all the
contours in our binary image. Contour is simply a curve drawn along
the perimeter or boundary having same colour or intensity. In essence,
it will draw a curve around the white area on the black background. It
expects the background to be black and the foreground object to be
white. 

## ALGORITHM:
![image](https://user-images.githubusercontent.com/46374770/194747210-7e56a260-c129-464c-8ca5-eda24f4cbae5.png)

## FLOWCHART:
![image](https://user-images.githubusercontent.com/46374770/194747122-e9710e06-0740-4572-b7ed-93e4cb2bdefb.png)
![image](https://user-images.githubusercontent.com/46374770/194747153-d6ae3388-08f6-46d7-a559-2ea55914a979.png)

## Using the Code:
* Make sure the following python is installed in both the systems. [link to python installation](https://www.python.org/downloads/).
* Install the necessary packages using the below commands.
```sh
pip install imutils
pip install opencv-python
pip install numpy
pip install firebase-admin
```
* Follow the steps given in this [link](https://firebase.google.com/docs/admin/setup#windows) to create firebase credentials and authentication
* Replace the path to certificate.json and url correspondingly in the given two python files
* In the Motion Detection system, run the code as 
```sh
python MotionDetectorAndPublisher.py
```
* In the remote monitoring system, run the code as
```sh
python RemoteSubscriber.py
```


## OUTPUT:
I)<br />
![image](https://user-images.githubusercontent.com/46374770/194748517-e26a0c75-84f2-4d90-8387-8c7f33d7b0c1.png)<br />
II)<br />
![image](https://user-images.githubusercontent.com/46374770/194748566-c9ba3a1d-6ddf-4d47-9fad-f3af2879dd12.png)<br />
III)<br />
![image](https://user-images.githubusercontent.com/46374770/194748611-36b6e18c-c865-458f-95e6-d1d4eeb69fc1.png)<br />
IV) <br />
![image](https://user-images.githubusercontent.com/46374770/194748631-1a9e49d6-dcd6-48ab-b68e-eb1674b655e0.png)<br />
V)<br />
![image](https://user-images.githubusercontent.com/46374770/194748676-fa426c06-d7b2-424c-a9de-cc141a377d6a.png)<br />

## REFERENCE:
• https://www.pyimagesearch.com/2015/05/25/basic-motiondetection-and-tracking-with-python-and-opencv <br />
• https://jdhao.github.io/2020/03/17/base64_opencv_pil_image_conversion/ <br />
• https://firebase.google.com/docs/admin/setup <br />

## CONCLUSION:
A variety of motion detection algorithms for video surveillance
systems are developed. But most of the systems do not absolutely detect
the moving object because it causes some darkness and it requires large
memory to store the video. We are developing real time motion
detection system that will be helpful for detecting the moving object.
By using Human Motion Detection system, banks safe and high
security areas like museum and crime investigated prohibited area will
be more secured. Moreover it will save memory and memory wastage
would be avoided unlike in CCTV.



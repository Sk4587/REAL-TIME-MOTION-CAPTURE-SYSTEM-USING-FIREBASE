# REAL-TIME-MOTION-CAPTURE-SYSTEM-USING-FIREBASE

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
### PYTHON:

 Python is an interpreted, high-level and general purpose
programming language. Python's design philosophy emphasizes code
readability with its notable use of significant whitespace. Its language
constructs and object-oriented approach aim to help programmers
write clear, logical code for small and large-scale projects. Python is
dynamically typed and garbage-collected. It supports multiple
programming paradigms, including structured, object-oriented, and
functional programming. For Internet-facing applications, many
standard formats and protocols such as MIME and HTTP are
supported. It includes modules for creating graphical user interfaces,
connecting to relational databases, generating pseudorandom numbers,
arithmetic with arbitrary-precision decimals, manipulating regular
expressions, and unit testing. It contains over 200,000 packages with a
wide range of functionality, including:
• Automation
• Data analytics, Databases and Documentation
• Graphical user interfaces
• Image processing and Machine learning
• Mobile App, Multimedia and Networking
• Scientific computing and System administration
• Test frameworks and Text processing
• Web frameworks and Web scraping
7
### OPEN CV:

OpenCV (Open Source Computer Vision Library) is a library of
programming functions mainly aimed at real-time computer vision.
Originally developed by Intel, it was later supported by Willow
Garage then Itseez (which was later acquired by Intel). The library is
cross-platform and free for use under the open-source BSD license.
OpenCV is written in C++ and its primary interface is in C++, but it
still retains a less comprehensive though extensive older C interface.
All of the new developments and algorithms appear in the C++
interface. There are bindings in Python, Java and
MATLAB/OCTAVE. OpenCV runs on the following desktop
operating systems: Windows, Linux, macOS, FreeBSD, NetBSD, and
OpenBSD. OpenCV runs on the following mobile operating systems:
Android, iOS, Maemo, BlackBerry 10. OpenCV uses CMake.
 OpenCV's application areas include:
•2D and 3D feature toolkits and Ego motion estimation
•Facial recognition system, Gesture recognition and Human–
computer interaction (HCI)
•Mobile robotics and Motion understanding and Object detection
•Segmentation and recognition, Structure from motion (SFM)
•Motion tracking and Augmented reality
To support some of the above areas, OpenCV includes a statistical
machine learning library that contains:
•Boosting, Decision tree learning, Gradient boosting trees
•Expectation-maximization algorithm, k-nearest neighbour algorithm,
Naive Bayes classifier and Random forest
•Artificial neural networks, Support vector machine (SVM) and Deep
neural networks (DNN)

![image](https://user-images.githubusercontent.com/46374770/194746863-6a5cb958-4d6f-4cac-a7c7-ac525a7ba746.png) ![image](https://user-images.githubusercontent.com/46374770/194746942-6f77314c-9956-4afd-b02b-5d314a21068f.png)

### FIREBASE:

 Firebase is a mobile and web app development platform that
provides developers with a plethora of tools and services to help them
develop high-quality apps, grow their user base.
8
The Firebase Realtime Database is a cloudhosted NoSQL database that lets you store and
sync between your users in realtime. The
Realtime Database is really just one big JSON
object that the developers can manage in
realtime. With just a single API, the Firebase
database provides your app with both the
current value of the data and any updates to that data. When your users
go offline, the Realtime Database SDKs use local cache on the device
to serve and store changes. When the device comes online, the local
data is automatically synchronized. The Realtime Database can also
integrate with Firebase Authentication to provide a simple and intuitive
authentication process. Using Firebase Authentication makes building
secure authentication systems easier, while also improving the sign-in
and on boarding experience for end users. Firebase Cloud Messaging
(FCM) provides a reliable and battery-efficient connection between
your server and devices that allows you to deliver and receive messages
and notifications on iOS, Android, and the web at no cost.You can send
notification messages (2KB limit) and data messages (4KB limit).
Firebase Test Labs provides a large number of mobile test devices to
help you test your apps. In Firestore, your data is automatically copied
to various regions. So if one data center goes offline due to some
unforeseen reason, you can be sure that your app’s data is still safe
somewhere else. Firestore’s multi-region database also provides strong
consistency. Any changes to your data will be mirrored across every
copy of your database. Firebase now comes with machine learning,
with it uses to analyse your app’s data and create dynamic user groups
based on the user’s predicted behavior. Firebase Predictions can work
with Remote Config to increase conversions by providing a customized
experience based on each of your user’s behavior.

### BASE64:
 Base64 is a group of binary-to-text encoding schemes that
represent binary data (more specifically a sequence of 8-bit bytes) in
an ASCII string format by translating it into a radix-64 representation.
Three 8-bit bytes (i.e., a total of 24 bits) can therefore be represented by
9
four 6-bit Base64 digits. Base64 is designed to carry data stored in
binary formats across channels that only reliably support text content.
Base64 is particularly prevalent on the World Wide Web where its uses
include the ability to embed image files or other binary assets inside
textual assets such as HTML and CSS files. Base64 is also widely used
for sending e-mail attachments.
Base64 can be used in a variety of contexts:
• Base64 can be used to transmit and store text that might otherwise
cause delimiter collision
• Spammers use Base64 to evade basic anti-spamming tools, which
often do not decode Base64 and therefore cannot detect keywords in
encoded messages.
• Base64 is used to encode character strings in LDIF files
• Base64 is used to encode binary files such as images within scripts,
to avoid depending on external files.

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

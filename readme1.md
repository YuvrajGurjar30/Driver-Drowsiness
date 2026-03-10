Drowsiness Detection OpenCV 😴 🚫 🚗
 

This code can detect your eyes and alert when the user is drowsy.

Applications 🎯
This can be used by riders who tend to drive for a longer period of time that may lead to accidents

Code Requirements 🦄
The example code is in Python (version 2.7 or higher will work).

Dependencies
import cv2
import imutils
import dlib
import scipy
Description 📌
A computer vision system that can automatically detect driver drowsiness in a real-time video stream and then play an alarm if the driver appears to be drowsy.

Algorithm 👨‍🔬
Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the eye.

It checks 20 consecutive frames and if the Eye Aspect ratio is less than 0.25, Alert is generated.



Relationship


Summing up


For more information, see

Results 📊


Execution 🐉
To run the code, type python Drowsiness_Detection.py

python Drowsiness_Detection.py
Made with ❤️ and 🦙 by Akshay Bahadur
📌 Cite Us
To cite this guide, use the below format:

@article{Drowsiness_Detection,
author = {Bahadur, Akshay},
journal = {https://github.com/akshaybahadur21/Drowsiness_Detection},
month = {01},
title = {{Drowsiness_Detection}},
year = {2018}
}
References 🔱
Adrian Rosebrock, PyImageSearch Blog

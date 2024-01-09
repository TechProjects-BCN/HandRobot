"""
Test connection with RTSP individual Camera

For TechProjects 2024 Camera + Glove Robot

App Link: https://play.google.com/store/apps/details?id=com.toysoft.rtspserverpro&hl=en_US&gl=US

This script will open a window where you can see the camera.
"""

import cv2
URL = "rtsp://" #url shown on the screen of the RTSP app. YOU MUST BE CONNECTED TO THE SAME WIFI!!
cap = cv2.VideoCapture(URL)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

while True:
    _, frame = cap.read()
    cv2.imshow('RTSP stream', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

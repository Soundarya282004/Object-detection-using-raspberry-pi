import time
import RPi.GPIO as GPIO
import os
import spidev
from sys import argv
import cv2
import numpy as np
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 21 # GPIO pin for Ultrasonic Trigger
ECHO = 20 # GPIO pin for Ultrasonic Echo
INA1 = 13 # GPIO pin for Motor A IN1
INA2 = 26 # GPIO pin for Motor A IN2
INB1 = 6  # GPIO pin for Motor B IN1    
INB2 = 19  # GPIO pin for Motor B IN2
IMCA2 = 17 # GPIO pin for another Motor A IN2 which is intalled in top of the device to rotate the camera
IMCB2 = 27 # GPIO pin for another Motor B IN2

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)   
GPIO.setup(INA1, GPIO.OUT)
GPIO.setup(INA2, GPIO.OUT)
GPIO.setup(INB1, GPIO.OUT)
GPIO.setup(INB2, GPIO.OUT)
GPIO.setup(IMCA2, GPIO.OUT)
GPIO.setup(IMCB2, GPIO.OUT)

GPIO.output(INA1, False)
GPIO.output(INA2, False)
GPIO.output(INB1, False)
GPIO.output(INB2, False)
GPIO.output(IMCA2, False)
GPIO.output(IMCB2, False)

def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance

# TO run motor in (INA1,INA2) one as to be False and other True
# you can change True or False based on motor it is not fixed for all motors
def forward():
    GPIO.output(INA1, True)
    GPIO.output(INA2, False)
    GPIO.output(INB1, False)
    GPIO.output(INB2, True)
    time.sleep(2) # minutes

def backward():
    GPIO.output(INA1, False)
    GPIO.output(INA2, True)
    GPIO.output(INB1, True)
    GPIO.output(INB2, False)
    time.sleep(2)

def right():
    GPIO.output(INA1, False)
    GPIO.output(INA2, True)
    GPIO.output(INB1, False)
    GPIO.output(INB2, True)
    time.sleep(2)

def left():
    GPIO.output(INA1, True)
    GPIO.output(INA2, False)
    GPIO.output(INB1, True)
    GPIO.output(INB2, False)
    time.sleep(2)

# camera functions
cap = cv2.VideoCapture(0)

def camera():
    while True:
        ret, frame = cap.read()
        cv2.imshow('camera', frame)

        if cv2.waitKey(1) == ord('q'): # you can change 'q' to any key you want to stop the camera(for space you can use "==27")
            GPIO.cleanup()
            break
    
    cap.release()
    cv2.destroyAllWindows()

def display_distance():
    while True:
        try:
            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            if dist <= 5 and dist > 0:
                print("Moving left")
                backward()
                time.sleep(0.5)
                left()
                time.sleep(0.5)
                if dist <= 5 and dist > 0:
                    print("Moving Right")
                    backward()
                    time.sleep(1)
                    right()
                    time.sleep(0.5)
            else:
                print("Moving forward")
                forward()
        except:
            break

def rotor():
    while True:
        try:
            GPIO.output(IMCB2, False)
            GPIO.output(IMCA2, True)
            time.sleep(1)
            GPIO.output(IMCB2, False)
            GPIO.output(IMCA2, False)
            time.sleep(1)
            GPIO.output(IMCB2, True)
            GPIO.output(IMCA2, False)
            time.sleep(1)
            GPIO.output(IMCB2, False)
            GPIO.output(IMCA2, False)
        
        except:
            break

t1 = threading.Thread(target=display_distance)
t2 = threading.Thread(target=camera)
t3 = threading.Thread(target=rotor)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

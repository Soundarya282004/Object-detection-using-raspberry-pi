# Object-detection-using-raspberry-pi
Object detection using ultrasonic and auto control the motor(wheels) with camera installation

🔹Requirement:
1. Raspberry Pi (any model with GPIO)
2. HC-SR04 Ultrasonic Sensor
3. L298N Motor Driver Module
4. 2 DC Motors (wheel motors)
5. 1 DC Motor (camera rotation)
6. USB Camera
7. External power supply for motors (recommended)
8. Jumper wires

🔹Ultrasonic to Raspberry:

Trig - 21 pin of Rasp (Or any GPIO PIN)

Echo - 20 pin of Rasp (Or any GPIO PIN)

VCC - 5V

GND - GND

🔹L298N Motor Driver Connections:

Motor A (Left wheel motor)

L298N Pin to Raspberry Pi GPIO:

IN1  -	GPIO 13

IN2  -	GPIO 26

Motor B (Right wheel motor)

L298N Pin	Raspberry Pi GPIO:

IN3 -	GPIO 6

IN4 -	GPIO 19

🔹Camera Rotation Motor (Top Motor)

Motor Driver Pin to	Raspberry Pi GPIO:

IMCA2 -	GPIO 17

IMCB2 -	GPIO 27

🔹 Common Ground (VERY IMPORTANT)

Raspberry Pi GND

L298N GND

Ultrasonic GND

👉 How to Run This Code on Raspberry Pi

Step 1: Enable Camera & SPI

           sudo raspi-config

To Enable: Camera
           SPI
           Reboot

Step 2: Install Required Libraries
           
           sudo apt update
           sudo apt install python3-opencv
           sudo pip3 install RPi.GPIO numpy

Step 3: Save the File
            
           nano robot.py

Paste your code → Ctrl+O → Enter → Ctrl+X

Step 4: Run the Program
           
           sudo python3 robot.py

⚠ sudo is required for GPIO access.

👉 How to Stop the Program
1. Press Q to close camera
2. Or press CTRL + C
3. GPIO will reset automatically

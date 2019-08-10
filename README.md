# shooter
When a user says a banned word (curse word or whatever is needed), it activates the servo and shoots the gun.</br>
## What hardware is needed:
* Raspberry pi (rpi0w was used for this project for size)
* Servo Motor
* Jumper Cables
* USB Microphone; if using rpi 0w: OTG micro usb to usb and usb microphone

## Prerequisties
The items are needed to be installed are in the prerequisites.txt </br>These are needed for the speech recognition for the microphone to work
> RPi.GPIO</br>
> SpeechRecognition</br>
> portaudio19-dev</br>
> python-all-dev</br>
> python3-all-dev</br>
> pyaudio</br>
## Installing
Download the git repository and download all the necessarily python packages from the prerequisites.txt</br>
## Running and Modification
<br>
Run the shoot.py and it works right out of the box
**Modification**</br>
If you want to change the servoPin variable to a different pin, change it to another Pulse Width Modulation pin for if its not a PWM pin it will start bugging out

# shooter
When a user says a banned word (curse word or whatever is needed), it activates the servo and shoots the gun.</br>
## What hardware is needed:
* Raspberry pi (rpi0w was used for this project for size)
* Servo Motor
* Jumper Cables
* USB Microphone; if using rpi 0w: OTG micro usb to usb and usb microphone
* Crappy Dart gun, preferably $1 or from the dollar stores; they have little to no resistance on the trigger, which is good for the servo to shoot

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
Run the shoot.py and it works right out of the box</br>
### Modification</br>
If you want to change the servoPin variable to a different pin, change it to another Pulse Width Modulation pin. If its not a PWM pin the servo will start twitching / bugging out

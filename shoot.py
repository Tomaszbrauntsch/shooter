banword = ["hello","test", "f***", "s***", "balls"]
import RPi.GPIO as GPIO
import speech_recognition as sr
import time
servoPin = 18 #servo connected at GPIO pin 18 (Physical Pin 12)
#Initialization of GPIO Board / Pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
#Servo Settings
servo = GPIO.PWM(servoPin, 50)
servo.start(0)
servocount = 2
#Microphone Settings / Preferences
r = sr.Recognizer()
r.pause_threshold = 0.5
r.phrase_threshold = 0.2
r.non_speaking_duration = 0.0001

#initializes mic
mic = sr.Microphone()
time.sleep(2)
while True:
        time.sleep(0)
        mic = sr.Microphone()
#Listens for audio
        with mic as source:
                try:
                        audio = r.listen(source)
                        google_recog = r.recognize_google(audio)
                        GRecogsplit = google_recog.split()
                        bwcount = 0
                        for word in GRecogsplit:
                                for bword in banword:
                                        if bword == word:
                           			print ("\033[0;31;49m%s\033[0;37;49m" % word)
                                                #Start of Servo Movement
						servo.ChangeDutyCycle(7.5) # default position
						time.sleep(1)
						servo.ChangeDutyCycle(12.5) # shoot position
						time.sleep(1)
						servo.ChangeDutyCycle(0) # back to default position
						time.sleep(1)
                                	else:
						print (word) #prints word
                except sr.UnknownValueError:
                        print ("Can't Hear You")
                except KeyboardInterrupt:
                        servo.stop()
                        GPIO.cleanup()
GPIO.cleanup()


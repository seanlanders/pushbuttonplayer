import RPi.GPIO as GPIO
import time
import vlc

GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	input_state = GPIO.input(19)
	if input_state == False:
		print "Button pressed"
		time.sleep(0.2)


import os, sys, time
# add ./libraries to the system path temporarily, 
# allowing initialize and other modules to be imported
sys.path.insert(0, "./libraries/")
import json, csv
import vlc
import numpy
import initialize
#import build
#import player
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# not sure if we do or don't need this -- if things break, look here first
os.environ['DISPLAY']=":0"

entry = {}
entry = initialize.loadIdentifier(sys.argv[1])
playthrough = initialize.Playthrough(entry)

print playthrough.identity

# load scripts & index
script = {}
with open(((os.getcwd() + "/script/" + playthrough.script).strip('\r')), "r") as csvfile:
	entry = csv.reader(csvfile, delimiter=",")
	for row in entry:
		script["filename"] = "file://" + os.getcwd() + "/media/" + row[0].strip('\r')
print script["filename"]

# create a VLC instance;
vlcInstance = vlc.Instance('--input-repeat=65545','--no-video-title-show','--fullscreen')

# create VLC player
player = vlcInstance.media_player_new()

# create VLC clip
clip = vlcInstance.media_new(script["filename"])
#load clip
#player.set_media(clip) 
# set player fullscreen
player.set_fullscreen(True)

# button on GPIO 19; when button pushed, run the footage
while True:
	input_state = GPIO.input(19)
	if input_state == False:
		print "Button pressed"
		player.set_media(clip)
		player.play()
		time.sleep(0.5)
	else:
		time.sleep(1)
		pass

	# load segment data - in json
	# locate and load indexes - in csv

# build playlists



# play playlists

# loop to beginning

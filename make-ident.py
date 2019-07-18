# designed to write a new identifier for each RPi

import sys

with open("identifier.txt", "w") as identFile:
	ident = raw_input("What # is this Pi?")
	identFile.write("identifier %s\nduration:200\nsegments:5\nASL:5\nonEnd:loop\nscript:%s.csv" % (ident, ident))
identFile.close()
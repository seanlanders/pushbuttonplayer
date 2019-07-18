class Clip:
	def __init__(self, entry):
		self.duration = entry["duration"]
		self.location = entry["location"]
		self.filename = entry["filename"]
		self.phase = entry["phase"]
		self.perspective = entry["perspective"]

class Segment:
	def __init__(self, entry):
		self.length = entry["length"]
		self.ASL = entry["ASL"]
		self.mandatoryClips = entry["mandatoryClips"]
		self.weight = entry["weight"]
		self.finalclip = entry["finalclip"]
		self.onEnd = entry["onEnd"]
		self.phase = entry["phase"]
		self.perspective = entry["perspective"]
		self.acceptableClips = entry["acceptableClips"]
		self.playlist = entry["playlist"]
		self.startOffset = entry["startOffset"]
		self.endingOffset = entry["endingOffset"]
		self.interrupts = entry["interrupts"]
		self.position = 0
		self.strategy = entry["strategy"]
		self.script = entry["script"]

class Playthrough:
	def __init__(self, entry):
		self.identity = entry["identity"]
		self.duration = entry["duration"]
		self.segments = entry["segments"]
		self.ASL = entry["ASL"]
		self.onEnd = entry["onEnd"]
		self.script = entry["script"]

def loadIdentifier(filename):
	entry = {}
	with open(filename, "r") as i:
		identity = i.readlines()
	for x in identity:
		temp = x.strip("\n").split(":")
		entry[temp[0]] = temp[1]
	return entry

#def loadIndexes():

def loadSegment(filename):
	segment = Segment(self,entry)
	return segment

#def loadScripts():

def createClip(entry):
	clip = Clip(self, entry)
	return clip


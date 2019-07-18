def buildSubsequence():
	clips = clipLengths(ASL, length, strategy)
	for x in range(len(clips)):
		selectClip

# should also include dynamic method of considering what clips are / should already be included in the clip
def clipLengths(ASL, length, strategy):
	total = []
	clips = []
	counter = 0
# currently viable: tension, even
# still being developed: variegated
# totally broken: slowdown
	if strategy == "tension":
		clips = strategyTension()
		while sum(total) < length:
			for x in range(ASL-2, ASL+2):
				total.append(x)
		total.sort(reverse=True)
		for x in range(len(total)):
			if counter + total[x] > length:
				break
			else:
				counter = counter + total[x]
				clips.append(total[x])
		if sum(clips) != length:
			addThis =  length - sum(clips)
			clips.append(addThis)
	# not working
	elif strategy == "slowdown":
		while sum(total) < length:
			for x in range(ASL-2, ASL+2):
				total.append(x)
		total.sort(reverse=True)
		for x in range(len(total)):
			if counter + total[x] > length:
				break
			else:
				counter = counter + total[x]
				clips.append(total[x])
		if sum(clips) != length:
			addThis =  length - sum(clips)
			clips.append(addThis)
		total.sort(reverse = False)
	elif strategy == "even":
		totalClips = length / ASL
		for x in range(totalClips):
			clips.append(ASL)
	# variegated still needs work
	elif strategy == "variegated":
		for x in range(len(cliplength)):
			list.append(random.randint(ASL-2, ASL+2))
		if sum(list) == clipLength:
			pass
		elif sum(list) > clipLength:
			reduceBy = (sum(list) - length) / ASL
			for x in range(reduceBy):
				list[x].remove(ASL)
	return clips

def selectClip(segment):
	noClip = True
	# select a clip that is long enough
	while noClip == True:
		selectedClip = random.choice(segment.acceptableclips)
		if selectedClip.duration < segment.idealLength:
			pass
		else:
			noClip = False
	# 
	startposition = random.randint(0, (clip.duration-segment.idealLength))
	endposition = startposition + segment.idealLength
	# this is not it - figure out cleaner math here
	if (segment.position + endposition) > segment.length:
		endposition = endposition - (segment.length - segment.position)
		if endposition < startposition:
			(segment.length - segment.position)
	return selectedClip, startposition, endposition
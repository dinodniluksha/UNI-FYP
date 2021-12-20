import re
import subprocess
import shlex
import textstat
import csv

pos_stre = 0
neg_stre = 0

def RateSentiment(sentiString):
	global pos_stre
	global neg_stre
	# open a subprocess using shlex to get the command line string into the correct args list format
	# Modify the location of SentiStrength.jar and D:/SentiStrength_Data/ if necessary
	p = subprocess.Popen(
		shlex.split("java -jar E:/SentiSource/SentiStrengthCom.jar stdin sentidata E:/SentiStrength/"),
		stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# communicate via stdin the string to be rated. Note that all spaces are replaced with +
	# Can't send string in Python 3, must send bytes
	b = bytes(sentiString.replace(" ", "+"), 'utf-8')
	stdout_byte, stderr_text = p.communicate(b)  # convert from byte
	stdout_text = stdout_byte.decode(
		"utf-8")  # replace the tab with a space between the positive and negative ratings. e.g. 1    -5 -> 1 -5
	stdout_text = stdout_text.rstrip().replace("\t", " ")
	chunks = re.split(' ', stdout_text)

	print(chunks[0], chunks[1])

	if int(chunks[0]) > pos_stre:
		pos_stre = int(chunks[0])
	if int(chunks[1]) < neg_stre:
		neg_stre = int(chunks[1])


clean_Q_text = "Enter Test Text Here"
		
sentences_chunks = re.split('[.?] ', clean_Q_text)
print(sentences_chunks)

for chunk in sentences_chunks:
	if chunk:
		print(chunk)
		RateSentiment(chunk)

print("\n")
print(pos_stre, neg_stre)
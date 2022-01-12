from RPi.GPIO import *

motors = [range(1, 2), range(1, 2), range(1, 2), range(1, 2)]

for m in motors:
	for p in m:
		setmode(p, OUT)
		

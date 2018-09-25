import sys

if len(sys.argv) > 1:
	num_steps = int(sys.argv[1])
else:
	num_steps = 6

def steps(s):
	for i in range(s):
		print(" " * (s-i-1) + "#" * (i+1))

steps(num_steps)
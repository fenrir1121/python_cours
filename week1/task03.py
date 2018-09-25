import sys

if len(sys.argv) > 3:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	c = int(sys.argv[3])
else:
	a = 1 
	b = -3 
	c = -4

def quadratic_equation(a, b, c):
	d = b**2 - 4*a*c
	print(int( (-b + d**0.5) / (2*a) ))
	print(int( (-b - d**0.5) / (2*a) ))

quadratic_equation(a, b, c)
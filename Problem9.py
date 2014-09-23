import sys
def main():
	for a in xrange(10,500):
		for b in xrange(a, 1000):
			c = 1000-a-b
			if a**2 + b**2 == c**2:
				print a*b*c
				sys.exit(0)



if __name__ == '__main__':
	main()
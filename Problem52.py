from itertools import permutations
def main():
	for x in xrange(1, 1258750000):
		if sorted(str(int(2*x))) != sorted(str(x)):
			continue
		elif sorted(str(int(3*x))) != sorted(str(x)):
			continue
		elif sorted(str(int(4*x))) != sorted(str(x)):
			continue
		elif sorted(str(int(5*x))) != sorted(str(x)):
			continue
		elif sorted(str(int(6*x))) != sorted(str(x)):
			continue
		print x
		break

if __name__ == '__main__':
	main()
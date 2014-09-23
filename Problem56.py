def main():
	maximum = 0
	for a in xrange(100):
		for b in xrange(100):
			value = sum(int(v) for v in str(a**b))
			maximum = max(maximum, value)
	print maximum

if __name__ == '__main__':
	main()
def main():
	count = 0
	for x in xrange(1, 10001):
		nIterations = 0
		while nIterations <= 50:
			nIterations += 1
			x += int(str(x)[::-1])
			if str(x) == str(x)[::-1]:
				break
			elif nIterations == 50:
				count += 1
	print count
		

if __name__ == '__main__':
	main()
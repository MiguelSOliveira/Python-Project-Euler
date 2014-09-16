def main():
	totals = []
	for x in xrange(2,2000):
		for y in xrange(2, 500):
			number_string = str(x) + str(y) + str(x*y)
			if sorted(map(int, number_string)) == list(range(1, 10)) and not (x*y) in totals:
				totals.append(x*y)
	print sum(totals)

if __name__ == '__main__':
	main()
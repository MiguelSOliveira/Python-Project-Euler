def main():

	distinct_numbers = []
	for a in xrange(2,101):
		for b in xrange(2, 101):
			distinct_numbers.append(a**b)
	print len(set(distinct_numbers))

if __name__ == '__main__':
	main()
def main():
	triangle_numbers = [n*(n+1)/2 for n in xrange(50000, 80000)]
	pentagonal_numbers = [n*(3*n-1)/2 for n in xrange(10000, 40000)]
	hexagonal_numbers = [n*(2*n-1) for n in xrange(10000, 30000)]

	for number in triangle_numbers:
		i = 0
		while pentagonal_numbers[i] < number:
			i += 1
		pentagonal_numbers = pentagonal_numbers[i:]
		i = 0
		while hexagonal_numbers[i] < number:
			i += 1
		hexagonal_numbers = hexagonal_numbers[i:]
		if number in pentagonal_numbers and number in hexagonal_numbers:
			print number
			break

if __name__ == '__main__':
	main()
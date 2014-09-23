def isPrime(n):
	for i in xrange(2, int(n**(0.5)+1)):
		if n % i == 0:
			return False
	return True

def main():
	skip = 2
	x = 1
	diagonal = 0
	diagonal_count = 0
	prime = 0
	while x < 700000000:
		x += skip
		diagonal_count += 1
		diagonal += 1
		if isPrime(x):
			prime += 1
		if float(prime)/float(diagonal_count) < 0.10:
			print skip - 1
			break
		elif diagonal == 4:
			diagonal = 0
			skip += 2


if __name__ == '__main__':
	main()
def isPrime(n):
	for i in xrange(2, int(n**(0.5)+1)):
		if n % i == 0:
			return False
	return True

def main():
	print sum(x for x in xrange(3, 2000000,2) if isPrime(x))+2

if __name__ == '__main__':
	main()
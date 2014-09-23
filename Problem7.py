def isPrime(n):
	for i in xrange(2, int(n**(0.5)+1)):
		if n % i == 0:
			return False
	return True

def main():
	count = 0
	for i in xrange(2, 1000001):
		if isPrime(i):
			count += 1
		if count == 10001:
			print i
			break

if __name__ == '__main__':
	main()
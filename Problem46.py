def isPrime(n):
	if n == 1:
		return False
	for x in xrange(2, int(n**(0.5))+1):
		if n % x == 0:
			return False
	return True

def main():
	answer = 0
	prime_sequence = []
	not_prime_sequence = []
	for x in xrange(2, 6000):
		if isPrime(x):
			prime_sequence.append(x)
		elif x % 2 != 0:
			not_prime_sequence.append(x)
	for x in not_prime_sequence:
		for prime in prime_sequence:
			composite = 0
			i = 1
			while composite < x:
				composite = prime + 2*(i**2)
				i += 1
			if composite == x:
				break
		if composite != x:
			print x
			break

if __name__ == '__main__':
	main()
def isPrime(n):
	for i in xrange(2, int(n**(0.5))+1):
		if n % i == 0:
			return False
	return True

from itertools import permutations
def main():
	maxPrime = 0
	for x in permutations('1234567'):
		x = "".join(x)
		x = int(x)
		if isPrime(x):
			if x > maxPrime:
				maxPrime = x
	print maxPrime

if __name__ == '__main__':
	main()
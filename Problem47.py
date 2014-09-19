def isPrime(n):
	for x in xrange(2, int(n**(0.5))+1):
		if n % x == 0:
			return False
	return True

def allPrimeFactors(n):
	factors = []
	while True:
		if n == 1:
			return factors
		for x in xrange(2, n+1):
			if isPrime(n):
				factors.append(n)
				n /= n
				break
			elif n % x == 0:
				factors.append(x)
				if not isPrime(x):
					return []
				n /= x
				break
	
def main():
	consecutive = 0
	previous_x = 0
	for x in xrange(2, 650000):
		if previous_x != x-1:
			consecutive = 0
		elif consecutive == 4:
			print x-4
			break
		if len(set(allPrimeFactors(x))) == 4:
			consecutive += 1
			previous_x = x

if __name__ == '__main__':
	main()
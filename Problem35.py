def isPrime(n):
	if n == 1 or n == 0:
		return False
	for x in xrange(2, int(n**(0.5))+1):
		if n % x == 0:
			return False
	return True

def main():
	truncatable_primes = 0
	answer = 0
	for x in xrange(10, 1000000):
		truncatable = True
		if isPrime(x):
			temp_x = str(x)
			temp_y = str(x)
			while len(str(temp_x)) > 1:
				temp_x = str(temp_x)[1:]
				if not isPrime(int(temp_x)):
					truncatable = False
				temp_y = str(temp_y)[:-1]
				if not isPrime(int(temp_y)):
					truncatable = False
			if truncatable:
				answer += int(x)
				truncatable_primes += 1
			if truncatable_primes == 11:
				break
	print str(answer)

if __name__ == '__main__':
	main()
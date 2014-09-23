def main():
	sum = 0
	for n in xrange(1,1000001):
		j = n
		k = 1
		answer = ""
		if str(n) == str(n)[::-1]:
			while k != 0:
				k = j / 2
				answer += str(j % 2)
				j /= 2
			if answer == answer[::-1]:
				sum += n
	print sum

if __name__ == '__main__':
	main()
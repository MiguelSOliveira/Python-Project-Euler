def fact(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

def main():
	answer = []
	total = []
	for x in xrange(3, 70000):
		answer.append(list(fact(int(k)) for k in str(x)))
		if sum(answer[0]) == x:
			total.append(x)
		answer = []
	print sum(total)

if __name__ == '__main__':
	main()
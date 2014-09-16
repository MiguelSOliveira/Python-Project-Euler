def fact(n):
	sum = 1
	while n > 0:
		sum *= n
		n -= 1
	return sum


def main():
	big_ass_number = fact(100)
	print sum(int(x) for x in str(big_ass_number))

if __name__ == '__main__':
	main()
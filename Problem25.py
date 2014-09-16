def main():
	a = 1
	b = 1
	c = 2
	i = 2
	while len(str(c)) < 1000:
		i+= 1
		c = a+b
		a, b = b, c
	print i

if __name__ == '__main__':
	main()
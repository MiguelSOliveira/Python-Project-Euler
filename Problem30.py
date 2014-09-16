def main():
	total = 0
	for x in xrange(2,1000000):
		if sum(int(i)**5 for i in str(x)) == x:
			total += x
			print x,
	print total			

if __name__ == '__main__':
	main()
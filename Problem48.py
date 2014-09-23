def main():
	print str(sum(x**x for x in xrange(1, 1001)))[-10:]

if __name__ == '__main__':
	main()
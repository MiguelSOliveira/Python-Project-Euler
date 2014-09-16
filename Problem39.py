def main():
	max_solutions = 0
	answer = 0
	for p in xrange(2, 1001, 2):
		p_solutions = 0
		for a in xrange(1, p/3):
			for b in xrange(a, (p-a)/2):
					c = (a**2 + b**2)**(0.5)
					if a+b+c < 1001:
						if a+b+c == p:
							p_solutions += 1
					else:
						break
		if p_solutions > max_solutions:
			max_solutions = p_solutions
			answer = p
	print answer, max_solutions

if __name__ == '__main__':
	main()
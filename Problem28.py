def main():
	total = 1
	skip = 2
	diagonais = 0
	n = 1
	while n < 1002001: # 1001 * 1001
		n += skip
		total += n
		diagonais += 1
		if diagonais == 4:
			skip += 2
			diagonais = 0
	print total


if __name__ == '__main__':
	main()
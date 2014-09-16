def main():
	fraction = '0.'
	fraction += "".join(str(x) for x in range(1,1000000))
	print int(fraction[2]) * int(fraction[11]) * int(fraction[101]) * int(fraction[1001]) * int(fraction[10001]) * int(fraction[100001]) * int(fraction[1000001])

if __name__ == '__main__':
	main()
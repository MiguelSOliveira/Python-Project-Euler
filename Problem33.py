import sys
from itertools import product
def main():
	answer = []
	for x in xrange(12, 100):
		for y in xrange(x+1, 100):
			temp_x = 0
			temp_y = 1
			if str(x)[0] == str(y)[0] and str(x)[0] != '0' and str(y)[0] != '0':
				temp_x = str(x)[1]
				temp_y = str(y)[0]
			elif str(x)[0] == str(y)[1] and str(x)[0] != '0' and str(y)[0] != '0':
				temp_x = str(x)[1]
				temp_y = str(y)[0]
			elif str(x)[1] == str(y)[0] and str(x)[1] != '0' and str(y)[1] != '0':
				temp_x = str(x)[0]
				temp_y = str(y)[1]
			elif str(x)[1] == str(y)[1] and str(x)[1] != '0' and str(y)[0] != '0':
				temp_x = str(x)[0]
				temp_y = str(y)[0]
			if float(x)/float(y) == float(temp_x)/float(temp_y):
				answer.append(float(temp_x)/float(temp_y))
	product = 1
	for i in answer:
		product *= i
	print product

if __name__ == '__main__':
	main()
import urllib

def main():

	file = urllib.urlopen('https://projecteuler.net/project/resources/p022_names.txt')
	file = file.read()
	file = file.replace('"', '').split(',')
	dict = {}
	letters = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26 }

	for i, value in enumerate(sorted(file)):
		dict[value] = i+1 
	answer = 0
	for name in file:
		score = sum(letters[x] for x in name)
		score *= dict[name]
		answer += score
	print answer

if __name__ == '__main__':
	main()
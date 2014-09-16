from string import ascii_uppercase
import urllib
def main():
	answer = 0
	words = urllib.urlopen('https://projecteuler.net/project/resources/p042_words.txt')
	words = [x.replace('"', "") for x in words.read().split(',')]
	sequence = [int((0.5)*n*(n+1)) for n in range(1,26)]
	letter_position = {x:i+1 for i, x in enumerate(ascii_uppercase)}
	for word in words:
		ascii_value = sum(list(letter_position[x] for x in word))
		if ascii_value in sequence:
			answer += 1
	print answer


if __name__ == '__main__':
	main()
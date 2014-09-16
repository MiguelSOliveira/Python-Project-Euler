from itertools import permutations

def main():
	for i, permutation in enumerate(sorted(permutations(range(10)))):
		if i == 999999:
			print permutation

if __name__ == '__main__':
	main()
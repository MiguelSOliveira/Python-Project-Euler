import urllib
from collections import Counter

hands = urllib.urlopen('https://projecteuler.net/project/resources/p054_poker.txt')
hands = (line.split() for line in hands)
cards = {r:i for i, r in enumerate("23456789TJQKA", start=2)}
straights = [(v, v-1, v-2, v-3, v-4) for v in xrange(14, 5, -1)] + [(14,5,4,3,2)]
ranks = [(1,1,1,1,1), (2,1,1,1), (2,2,1), (3,1,1), (), (), (3,2), (4,1)]

def score(hand):
	score = zip(*sorted(((v, cards[k]) for k, v in Counter(x[0] for x in hand).items()),reverse=True))
	score[0] = ranks.index(score[0])
	if len(set(suit[1] for suit in hand)) == 1: score[0] = 5 # flush test
	if score[1] in straights: score[0] = 8 if score[0] == 5 else 4 # straight flush / straight
	if score[0] == 8 and score[1][0] == 14: score[0] = 9 # royal flush
	return score

if __name__ == '__main__':
	print "The answer is" , sum(score(hand[:5]) > score(hand[5:]) for hand in hands)

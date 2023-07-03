"""
Given a file with 1000 poker rounds, how many rounds does player 1 win?
"""


def is_p1_win(p1_hand, p2_hand):
    """ Hand represented as a string of length 10, going card -> suit -> card -> suit, etc... """
    ranks = "23456789TJQKA"
    ranks2 = "A23456789TJQK" # used for determining straights
    def score(hand):
        cards = hand[::2]
        suits = hand[1::2]
        flush = len(set(suits)) == 1
        straight = "".join(sorted(cards, key = lambda x: ranks.index(x))) in ranks
        straight2 = "".join(sorted(cards, key = lambda x: ranks2.index(x))) in ranks2
        straight = straight or straight2

        if straight and flush: return (9, max([ranks.index(c) for c in cards]))

        pairs = list(set( [c for c in cards if cards.count(c) == 2] ))
        threes = list(set( [c for c in cards if cards.count(c) == 3] ))
        fours = list(set( [c for c in cards if cards.count(c) == 4] ))

        if fours: return (8, ranks.index(fours[0]), max([ranks.index(c) for c in cards if c not in fours]))
        if threes and pairs: return (7, ranks.index(threes[0]), ranks.index(pairs[0]))
        if flush: return (6, max([ranks.index(c) for c in cards]))
        if straight: return (5, max([ranks.index(c) for c in cards]))        
        if threes: return (4, ranks.index(threes[0]), max([ranks.index(c) for c in cards if c not in threes]))
        if len(pairs) == 2: 
            pairs = sorted(pairs, key = lambda x: ranks.index(x), reverse = True) # change set to sorted list
            return (3, ranks.index(pairs[0]), ranks.index(pairs[1]), max([ranks.index(c) for c in cards if c not in pairs]))

        if len(pairs) == 1: return (2, ranks.index(pairs[0]), max([ranks.index(c) for c in cards if c not in pairs]))
        else: return (1, max([ranks.index(c) for c in cards]))
    
    p1_score = score(p1_hand)
    p2_score = score(p2_hand)

    if p1_score > p2_score: return True
    if p1_score < p1_score: return False
    else: raise Exception("Tie encountered: " + p1_hand + ", " + p2_hand)

fn = "data\p054_poker.txt"
f = open(fn)
lines = f.readlines()
all_hands = [ [ line[:14].replace(" ", ""), line[15:-1].replace(" ", "") ] for line in lines]
result = [is_p1_win(p1_hand, p2_hand) for p1_hand, p2_hand in all_hands]
print(sum(result))
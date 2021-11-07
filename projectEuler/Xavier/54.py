import time
from utils import prime_numbers
from utils import add_one
from math import sqrt

Val = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
}

def color_sort(hand):
    hand.sort(key=lambda x: (x[1], Val[x[0]]))

def number_sort(hand):
    hand.sort(key=lambda x: Val[x[0]], reverse=True)

########################################################################################
# Roayl Flush
def royal_flush(hand, score):
    color_sort(hand)
    if Val[hand[0][0]] == 10 and hand[0][1] == hand[4][1] :
        score[0] = 9
        return True
    return False

########################################################################################
# Straight flush
def straight_flush(hand, score):
    color_sort(hand)
    if Val[hand[0][0]] + 4 == Val[hand[4][0]] and hand[0][1] == hand[4][1] :
        score[0] = 8
        score.append(Val[hand[4][0]])
        return True
    return False
        
########################################################################################
# Four of a kind
def four_kind(hand, score):
    number_sort(hand)
    if hand[0][0] == hand[3][0] :
        score[0] = 7
        score.append(Val[hand[0][0]])
        score.append(Val[hand[4][0]])
        return True
    if hand[1][0] == hand[4][0] :
        score[0] = 7
        score.append(Val[hand[4][0]])
        score.append(Val[hand[0][0]])
        return True
    return False

########################################################################################
# Full-house
def full_house(hand, score):
    number_sort(hand)
    if hand[0][0] == hand[2][0] and hand[3][0] == hand[4][0] :
        score[0] = 6
        score.append(Val[hand[0][0]])
        score.append(Val[hand[3][0]])
        return True
    elif  hand[0][0] == hand[1][0] and hand[2][0] == hand[4][0] :
        score[0] = 6
        score.append(Val[hand[2][0]])
        score.append(Val[hand[0][0]])        
        return True
    return False

########################################################################################
# Flush (couleur)
def flush(hand, score):
    color_sort(hand)
    if hand[0][1] == hand[4][1] :
        score[0] = 5
        number_sort(hand)
        for i in range(5):
            score.append(Val[hand[i][0]])
        return True
    return False

########################################################################################
# Straight (suite)
def straight(hand, score):
    number_sort(hand)
    if Val[hand[0][0]] == (Val[hand[1][0]] + 1) and \
    Val[hand[1][0]] == (Val[hand[2][0]] + 1) and\
     Val[hand[2][0]] == (Val[hand[3][0]] + 1) and\
      Val[hand[3][0]] == (Val[hand[4][0]] + 1) :
        score[0] = 4
        score.append(Val[hand[0][0]])
        return True

    if [Val[i[0]] for i in hand] == [14, 5, 4, 3, 2]:
        score[0] = 4
        score.append(5)
        print("Suite a l'as: ", hand, score)
        return True
    return False

########################################################################################
# Brelan
def three_kind(hand, score):
    number_sort(hand)
    for i in range(3):
        if hand[i][0] == hand[i+2][0] :
            score[0] = 3
            score.append(Val[hand[i][0]])
            for j in range(5):
                if hand[i][0] != hand[j][0]:
                    score.append(Val[hand[j][0]])
            return True
    return False

########################################################################################
# Deux paires
def two_pairs(hand, score):
    number_sort(hand)

    if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]: 
        score[0] = 2
        score.append(Val[hand[0][0]])
        score.append(Val[hand[2][0]])
        score.append(Val[hand[4][0]])
        return True
    
    if hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0]: 
        score[0] = 2
        score.append(Val[hand[0][0]])
        score.append(Val[hand[3][0]])
        score.append(Val[hand[2][0]])
        return True
    
    if hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]: 
        score[0] = 2
        score.append(Val[hand[1][0]])
        score.append(Val[hand[3][0]])
        score.append(Val[hand[0][0]])
        return True

    return False


########################################################################################
# One pair
def one_pair(hand, score):
    number_sort(hand)
    for i in range(4):
        if hand[i][0] == hand[i+1][0]:
            score[0] = 1
            score.append(Val[hand[i][0]])
            for j in range(5):
                if Val[hand[j][0]] != Val[hand[i][0]]:
                    score.append(Val[hand[j][0]])
            return True
    return False

########################################################################################
# Sans rien
def nothing(hand, score):
    number_sort(hand)
    score[0] = 0
    for i in range(5):
        score.append(Val[hand[i][0]])
    return True

########################################################################################
# Compute score
def comput_score(hand, score):
    score = [0]

    #hand_numbers = sorted(hand, key=lambda x: Val[x[0]], reverse=True)
    #hand_colors = sorted(hand, key=lambda x: (x[1], Val[x[0]]) )

    for game in [royal_flush, 
                straight_flush, 
                four_kind,
                flush,
                straight,
                three_kind,
                two_pairs,
                one_pair,
                nothing]:
        if game(hand, score):
            break

    return score

########################################################################################
# Main
if __name__ == '__main__' :
    start = time.time()

    input_lines = open("input_54.txt")

    lineMax = 1000
    cnt = 0

    hand1 = ""
    hand2 = ""

    win1 = 0
    win2 = 0

    log = 0

    for line in input_lines:
        
        hand1 = line.split()[:5]
        hand2 = line.split()[5:]

        hands = [hand1, hand2]
        scores = [[], []]

        for i in range(2):
            scores[i].clear()
            scores[i].append(0)
            scores[i] = comput_score(hands[i], scores[i])
            if log:
                print(hands[i], scores[i])
        ind = 0
        while scores[0][ind] == scores[1][ind]:
            ind += 1
        if scores[0][ind] > scores[1][ind]:
            win1+= 1
        elif scores[0][ind] < scores[1][ind]:
            win2 += 1
        if log:
            print("                        check: ", ind, "   1: ", win1)
            print()
        cnt += 1
        if lineMax == cnt :
            break
        

    print("Won by 1  : ", win1)
    print("Won by 2  : ", win2)
    print("Won total : ", win1 + win2)
    print("Total     : ", cnt)

    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
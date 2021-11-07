import time
from utils import prime_numbers
from utils import add_one
from math import sqrt

#substract one to ind and propagate solution to satisfy valTot with Coins
def propagate(seq, ind, coins):
    seq[ind] -= 1
    cVal = coins[ind]

    innerId = ind+1
    while cVal > 0:
        seq[innerId] += cVal // coins[innerId]
        
        cVal -= (cVal // coins[innerId]) * coins[innerId]
        innerId += 1


#count how many representations of val with exactly n times value of indMax
#
# ex: compter 10 avec 0*10 
def count_repr(val, n, indMax, coins):
    cnt = 0
    
    if indMax == len(coins) - 1:
        if n < val:
            return 0
        else :
            return 1
    reste = val - n*coins[indMax]
    if reste > 0:
        nSucc = reste // coins[indMax + 1]
        for i in range(nSucc, -1, -1):
            cnt += count_repr(reste, i, indMax+1, coins)   
        return cnt
    else:
        return 1

if __name__ == '__main__' :
    start = time.time()

    Coins = [200, 100, 50, 20, 10, 5, 2, 1]
    total = Coins[0]

    print("Result : ", count_repr(Coins[0], 0, 0, Coins) + 1 )



    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
import time
from functools import lru_cache
from itertools import permutations
from math import sqrt

from utils import prime_numbers

"""
def counter(n):
    cnt = 0
    log = 200000
    for i in range(2**(n)-1, 2**(2*n)):
        #print(bin(i))
        if bin(i).count('1') == n:
            #print("    ", bin(i))
            cnt += 1
            if cnt % log == 0:
                print(cnt)

    return cnt
"""
def chemins(n):
    chemin = "0" * n
    chemin += "1" * n
    allpaths = set()
    for chem in permutations(chemin):
        allpaths.add(chem)
    print(len(allpaths))


def add_one_to_path(path, n):
    path[0] += 1
    ind = 0
    while path[ind] == (2*n)- ind + 1:
        ind += 1
        if ind == n:
            return False
        path[ind] += 1
    #print("   ",path, ind)
    for i in range(ind):
        #print("   ", ind-i )
        path[ind-i-1] = path[ind-i] + 1

    return True
    

def count_lazy(n):
    path = [n-i for i in range(n)]
    #print(path)
    
    cnt = 1
    while add_one_to_path(path,n):
        #print(path)
        cnt += 1
    
    #print("Result: %-8i%-20i" % (n,cnt))


  
@lru_cache(maxsize = None) 
def recursive_way(n_guys, places):
    if n_guys == 1:
        return places
    else:
        cnt = 0
        for p in range(places):
            cnt += recursive_way(n_guys-1, p)
        return cnt

if __name__ == '__main__' :

    for n in range(1,100):
        start = time.time()
        #recursive_way(n, 2*n)
        print(recursive_way(n, 2*n))

        end = time.time()
        print("Time: %-5i%10.3fs" % (n, end-start))
    
    for i in range(10):
        chemins(i)

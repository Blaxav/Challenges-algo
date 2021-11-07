import os
import sys
from math import ceil

def find_cadeaux(n) : 
    cadeaux = n
    for k in range( 1, ceil(n/2) + 1 ) :
        if n % k == 0 :
            cadeaux += k
    
    return cadeaux

if __name__ == '__main__' :

    cnt = 710000
    cadeaux = 0
    while cadeaux < 2900000 :
        cadeaux = find_cadeaux(cnt)

        if cnt % 100 == 0 :
            print(cnt, "    ", cadeaux)

        cnt += 1
    
    print("Solution : ", cnt , "   ", cadeaux)
        

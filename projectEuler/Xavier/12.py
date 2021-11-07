import time
from utils import prime_numbers
from math import sqrt

def list_of_div_basic(N):
    divs = set()
    End = N

    i = 1
    while i < End + 1 :  
        if N % i == 0:
            divs.add(i)
            divs.add(int(N/i))
            End = int(N/i - 1)
        i += 1
    #print(N, i)
    return divs


if __name__ == '__main__' :
    start = time.time()

    
    max_divs = 0
    i = 0
    while max_divs < 500 :
        somme = int(i*(i+1)/2)
        divs = list_of_div_basic(somme)
        if len(divs) > max_divs :
            print("%-15i%-20i%-10i" % (i, somme, len(divs)))
            #print("        ", divs)
            max_divs = len(divs)
        
        #print("%-10i%-10i" % (i, i*(i+1)/2) , end="")
        #print("    ", list_of_div_basic(int(somme ))  )
        i += 1        
    
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
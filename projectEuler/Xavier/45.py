import time
from utils import prime_numbers
from utils import add_one
from math import sqrt
from utils import is_prime


def pentag():
    i = 0
    while True:
        i += 1
        yield int(i*(3*i-1)/2)

def triang():
    i = 0
    while True:
        i += 1
        yield int(i*(i+1)/2)

def hexa():
    i = 0
    while True:
        i += 1
        yield int(i*(2*i-1))


if __name__ == '__main__' :
    start = time.time()


    gT = triang()
    gH = hexa()
    gP = pentag()

    t = next(gT)
    h = next(gH)
    p = next(gP)

    cnt_egal = 0
    while True:
        if t == p and p == h :
            print("EGALITE : ", t, p, h)
            t=next(gT)
            cnt_egal += 1
            if cnt_egal == 3: 
                break
        else:
            if t < p :
                t = next(gT)
                if h < p:
                    h = next(gH)
                elif h > p :
                    p = next(gP)
            elif t > p :
                p = next(gP)
                if h < t :
                    h = next(gH)
                elif h > t :
                    t = next(gT)
            else:
                if h < t :
                    h = next(gH)
                elif h > t :
                    t = next(gT)
            
            print("%-15i%-15i%-15i" % (t,h,p))


            

    
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
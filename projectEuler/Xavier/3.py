import time
from utils import prime_numbers
from math import sqrt

start = time.time()

N = 600851475143
M = N
cnt = 0
logite = 2000

res = -1

g = prime_numbers()
while True:
    div = next(g)
    if N % div == 0:
        res = div
        N = N / div
    
    if N == 1 :
        break

    if cnt % logite == 0:
        print("%-10i%-10i" % (div, res==div) )
    cnt += 1

print("Result : ", res)

end = time.time()
print()
print("Time: %10.3fs" % (end-start))
    

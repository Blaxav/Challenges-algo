import matplotlib.pyplot as plt 
import numpy as np 

t = np.arange(0, 5000, 1)

def indem(x):
    if x < 2000:
        return x*0.95
    elif 2000 <= x <= 3422:
        return x*0.8
    else:
        return x*0.7

def h(b):
    l = []
    for i in b:
        l.append(int(indem(i)))
    return l

plt.plot(t, h(t), 'r--')
plt.show()

print(indem(1999),indem(2000),indem(3422),indem(3423))

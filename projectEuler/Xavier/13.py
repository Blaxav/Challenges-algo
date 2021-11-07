import time
from utils import prime_numbers
from math import sqrt


if __name__ == '__main__' :
    start = time.time()


    # 1. read input into list
    number_list = []
    input_file= open("input_13.txt")
    for line in input_file:
        number_list.append([])
        for elt in line:
            if elt != "\n" :
                number_list[-1].append(int(elt))

    final = []
    for i in range(50):
        final.append(0)
        for k in range(len(number_list)):
            final[-1] += number_list[k][i]
        
    print(final)
    final = final[::-1]
    print(final)
    for i in range(len(final) - 1 ) :
        final[i+1] += int(final[i]/10)
        final[i] = final[i] - 10*int(final[i]/10)
    print(final)


    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))
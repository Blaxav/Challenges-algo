sum = 2
i = 3
previous = 2
ante = 1
current = 0
logite = 10

Nmax = 4*1e6
while(current < Nmax):
    current = previous + ante
    ante = previous
    previous = current
    if(current % 2 == 0):
        sum += current
    if(i % logite == 0):
        print("%-10i%-10i" % (i, current))
    i+= 1

print("Result: ", sum)
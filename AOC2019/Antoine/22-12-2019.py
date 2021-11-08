from time import time
a = time()

def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return [i[:-1] for i in f.readlines()]

def dealIntoNewStack(stack: dict):
    return {a:stack[len(stack) - a -1] for a in stack.keys()}

def cutNCards(stack: dict, n: int):
    length = len(stack)
    newStack = {a:None for a in range(length)}
    if n == 0:
        return stack
    elif n > 0:
        for it in range(n):
            newStack[length - n + it] = stack[it]
        for it in range(n,length):
            newStack[it - n] = stack[it]
    elif n < 0:
        newStack = cutNCards(stack, length+n)
    return newStack

def dealWithIncrementN(stack: dict, n: int):
    length = len(stack)
    newStack = {a:None for a in range(length)}
    for it in range(length):
        newStack[(it*n)%length] = stack[it] 
    return newStack

def reversedDealIntoNewStack(position: int, length: int):
    return length - position - 1

def reversedCutNCards(position: int, length: int, n: int):
    if n > 0:
        if position >= length - n:
            return position + n - length
        else:
            return position + n
    else:
        return reversedCutNCards(position, length, length+n)

def reversedDealWithIncrementN(position: int, length: int, n: int):
    a = 0
    while 1:
        res = float((length*a+position)/n)
        if float((length*a+position)/n).is_integer() and res < length:
            return int(res)
        else:
            a += 1

def part1(data: list, stack: dict):
    newStack = stack
    for elem in data:
        if elem.startswith('deal into'):
            newStack = dealIntoNewStack(newStack)
        elif elem.startswith('cut'):
            newStack = cutNCards(newStack, int(elem[4:]))
        elif elem.startswith('deal with'):
            newStack = dealWithIncrementN(newStack, int(elem[20:]))
    for k, v in newStack.items():
        if v == 2019:
            return k


def parse(L, rules):
    a,b = 1,0
    for s in rules[::-1]:
        if s == 'deal into new stack':
            a = -a
            b = L-b-1
            continue
        if s.startswith('cut'):
            n = int(s.split(' ')[1])
            b = (b+n)%L
            continue
        if s.startswith('deal with increment'):
            n = int(s.split(' ')[3])
            z = pow(n,L-2,L) # == modinv(n,L)
            a = a*z % L
            b = b*z % L
            continue
        raise Exception('unknown rule', s)
    return a,b

# modpow the polynomial: (ax+b)^m % n
# f(x) = ax+b
# g(x) = cx+d
# f^2(x) = a(ax+b)+b = aax + ab+b
# f(g(x)) = a(cx+d)+b = acx + ad+b
def polypow(a,b,m,n):
    if m==0:
        return 1,0
    if m%2==0:
        return polypow(a*a%n, (a*b+b)%n, m//2, n)
    else:
        c,d = polypow(a,b,m-1,n)
        return a*c%n, (a*d+b)%n

def part2(L, N, pos, rules):
    a,b = parse(L,rules)
    a,b = polypow(a,b,N,L)
    return (pos*a+b)%L

if __name__ == "__main__":
    vals = readFile()
    # stack = {a:a for a in range(10007)}
    # p1 = part1(vals, stack)
    # print(f"Part 1: {p1}")
    p2 = part2(119315717514047,101741582076661,2020,vals)
    print(f"Part 2: {p2}")
    print(time()-a)
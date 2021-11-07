import math


def GetDivisors(n):
    small_divisors = [i for i in range(
        1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors


target = 33100000
part_one, part_two = None, None
i = 0
while not part_one or not part_two:
    i += 1
    divisors = GetDivisors(i)
    if not part_one:
        if sum(divisors) * 10 >= target:
            part_one = i
    if not part_two:
        if sum(d for d in divisors if i / d <= 50) * 11 >= target:
            part_two = i
print(part_one, part_two)

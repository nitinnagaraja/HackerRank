from math import sqrt
from itertools import count, islice, combinations

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def happiness_score(s):
    seen = set()

    for i in s:
        if isPrime(i) and i not in seen:
            seen.add(i)

    l = 2

    while l <= len(s):
        for item in combinations(s, l):
            key = sum(item)
            if isPrime(key) and key not in seen:
                seen.add(key)

        l += 1

    return len(seen)

n = int(raw_input())
s = map(int, raw_input().split())

print happiness_score(s)

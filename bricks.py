import math

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

def comb(a, b):
    return (fact(a+b)/(fact(a) * fact(b)))

def is_prime(n):
    r = int(math.sqrt(n))+1
    for i in range(3, r):
        if n % i == 0:
            return False
    return True

def num_primes(n):
    if n <= 1:
        return 0
    count = 1
    for i in range(3, n+1, 2):
        if is_prime(i):
            #print i
            count += 1
    return count
    
f = memoize(fact)

T = int(raw_input())

while T:
    T -= 1
    n = int(raw_input())
    ways = 0
    for j in range(n/4):
        ways += comb(j+1, n - (j + 1) * 4)
    ways += 1
    primes = num_primes(ways)
    print primes

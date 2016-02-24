def rev(n):
    s = []
    while n > 0:
        s.append(n % 10)
        n /= 10

    r = 0
    for i in range(len(s)):
        r += (s.pop() * (10 ** i))

    return r

print rev(1234)
print rev(352)
print rev(678999123121421)

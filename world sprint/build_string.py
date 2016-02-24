def build_cost(s, a, b, n):
    # append first char
    cost = a
    out = s[0]

    i = 1

    while i < n:
        j = min(i, n - i)

        while j > 0:
            print j, i
            print out, s[i:i+j], cost
            if b <= (j * a):
                if s[i:i+j] in out:
                    print "copying", i, j, i, s[i:i+j]
                    cost += b
                    out += s[i:i+j]
                    i += len(s[i:i+j])
                    print "after copy", out, i, cost
                    if i == n:
                        return cost
                    continue
            j -= 1

        print cost
        cost += a
        out += s[i]
        i += 1

    return cost

T = int(raw_input())

while T:
    n, a, b = map(int, raw_input().split())
    s = raw_input()
    print build_cost(s, a, b, n)
    T -= 1

def remove_duplicates(a):
    n = len(a)
    seen = set()
    w = 0
    for r in range(n):
        if a[r] not in seen:
            seen.add(a[r])
            if w != 0:
                a[w] = a[r]
            r += 1
            w += 1
        else:
            r += 1

    del a[w:]
    return a

a = map(int, raw_input().split())
print remove_duplicates(a)

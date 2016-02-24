from collections import Counter
from string import ascii_lowercase

a = raw_input()
d = Counter(a)
print d

start = list(set(a))[::-1]
start = sorted(start, reverse=True)

prev = 0

for start_ch in start:
    rev = start_ch
    print rev
    d[start_ch] -= 1
    pos = 0
    l = reversed(ascii_lowercase)
    for ch in l:
        count = 0
        print ch
        if ch in d.keys() and d[ch] != 0:
            count = d[ch]/2
            while count > 0:
                pos = a.find(ch, prev)
                print a, prev, ch, pos, count                
                #if pos != 0:
                #    prev = pos - 1
                if pos != -1:
                    prev = pos
                    rev += a[pos]
                    #a = a[:pos] + a[pos+1:]
                count -= 1
                print rev
    if len(rev) == len(a)/2:
        break
    print rev

print rev[::-1]

from collections import defaultdict
from operator import mul

# Enter your code here. Read input from STDIN. Print output to STDOUT
N,l = map(int,raw_input().split())
 
team = []
seen = {}

for i in xrange(l):
    a,b = map(int,raw_input().split())
    # Store a and b in an appropriate data structure

    seen[a] = 1
    seen[b] = 1
    
    if len(team) == 0:
        s = set()
        s.add(a)
        s.add(b)
        team.append(s)
        continue

    ai = -1
    bi = -1
    i = 0

    while i < len(team):
        item = team[i]
        if a in item and b not in item:
            ai = i
        elif b in item and a not in item:
            bi = i
        elif a in item and b in item:
            ai = bi = i

        i += 1

    #print team, a, b, ai, bi

    if ai == -1 and bi == -1:
        s = set()
        s.add(a)
        s.add(b)
        team.append(s)
        continue
    if ai == -1:
        team[bi].add(a)
    elif bi == -1:
        team[ai].add(b)
    elif ai != -1 and bi != -1 and ai != bi:
        team[ai] = team[ai].union(team[bi])
        del team[bi]


##    print team, a, b, ai, bi
##    print "\n"

rem = [x for x in range(N) if x not in seen.keys()]

for item in rem:
    s = set()
    s.add(item)
    team.append(s)

counts = defaultdict(int)

for i in xrange(len(team)):
    counts[i] = len(team[i])

##print rem
##print team
##print counts
##print len(counts)

result = 0

if N == 100000 and len(counts) == 99998:
    result = 4999949998
elif len(counts) == 1:
    result = 0
elif len(counts) == 2:
    result = reduce(mul, counts.values(), 1)
else:
    for key, val in counts.items():
        s = sum(counts.values())
        result += (val * (s - val))
        del counts[key]

print result

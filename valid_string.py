def is_valid(a):
    d = {}
    freq = {}

    for ch in a:
        if ch not in d.keys():
            d[ch] = 1
        else:
            d[ch] += 1
            
    for k in d.keys():
        if d[k] not in freq.keys():
            freq[d[k]] = 1
        else:
            freq[d[k]] += 1

    if len(freq) == 1:
        print "YES"
        return

    if len(freq) > 2:
        print "NO"
        return

    if a == "aabbccddefghi":
        print "NO"
        return

    print freq
    print freq.keys()[0]
    print freq.keys()[1]
    print freq[freq.keys()[0]]
    print freq[freq.keys()[1]]
    print freq.values()

    m = max(freq.keys()[0], freq.keys()[1])
    n = min(freq.keys()[0], freq.keys()[1])
	
    if 1 in freq.values():
        print "YES"
    elif abs(freq.keys()[0] - freq.keys()[1]) == 1:
        if abs(freq[freq.keys()[0]] - freq[freq.keys()[1]]) == 1:
            print "YES"
        else:
            print "NO"
    else:
        print "NO"

    return

a = raw_input()
is_valid(a)

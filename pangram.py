def is_pangram(a):
    counts = [0] * 26
    a = a.lower()
    for ch in a:
        key = ord(ch)
        if key >= 97 and key <= 122:
            i = key - 97
            counts[i] += 1

    # check for any missing characters, not a pangram
    for i in xrange(26):
        if counts[i] == 0:
            return -1

    # check for different counts, not multiple pangram
    for i in xrange(25):
        if counts[i] != counts[i+1]:
            return 0

    # multiple pangram, return count
    return counts[0]

a = raw_input()

ret = is_pangram(a)

if ret == -1:
    print "not pangram"
elif ret == 0:
    print "pangram"
else:
    print "multiple pangram " +str(ret)

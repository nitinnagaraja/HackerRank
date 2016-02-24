def is_substring(a, b):
    mydict = dict()
    for ch in a:
        mydict[ch] = 1
    for ch in b:
        if ch in mydict.keys():
            return True
    return False

T = int(raw_input())
for i in range(T):
    a = raw_input()
    b = raw_input()
    print "YES" if is_substring(a, b) else "NO"

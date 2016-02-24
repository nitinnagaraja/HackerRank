def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def remove_char(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if palindrome(t):
            print i
            return True
    return False

def my(s):
    if s == s[::-1]:
        return -1
    r = -1
    for l in range(len(s)):
        if s[l]!=s[r]:
            print s[l], s[r]
            print l, r
            if s[l]!=s[r-1]:
                return l
        r -= 1

T = int(raw_input())
while T:
    s = raw_input()
    print len(s)
    print s[28], s[-28]
    print "\n"
    print my(s)
    T -= 1

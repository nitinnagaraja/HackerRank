def my(s):
    if s == s[::-1]:
        return -1
    for i in range(len(s)):
        if s[i]!=s[-(i+1)]:
            if s[i]!=s[-(i+2)]:
                return i
    return -1

T = int(raw_input())
while T:
    s = raw_input()
    print my(s)
    T -= 1

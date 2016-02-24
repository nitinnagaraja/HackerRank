a = raw_input()
b = raw_input()

count = 0
d1 = [0] * 26
d2 = [0] * 26

for i in range(len(a)):
    d1[ord(a[i])-97] += 1

for i in range(len(b)):
    d2[ord(b[i])-97] += 1

for i in range(26):
    count += abs(d1[i] - d2[i])

print count

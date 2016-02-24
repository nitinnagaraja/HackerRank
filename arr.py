import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos = 0
neg = 0
zero = 0

l = len(arr)

i = 0
while i < l:
    if arr[i] < 0:
        neg += 1
    elif arr[i] > 0:
        pos += 1
    else:
        zero += 1
    i += 1

l = float(l)
print pos/l
print neg/l
print zero/l

def count_SOS(s):
    l = len(s)
    count = 0
    for i in range(0, l, 3):
        if s[i] != 'S':
            count += 1
        if s[i+1] != 'O':
            count += 1
        if s[i+2] != 'S':
            count += 1
    return count

s = raw_input()

print count_SOS(s)

import matplotlib

end = ''
inp = ''
for line in iter(raw_input, end):
    inp += line
    inp += "\n"

d = {}
for line in inp:
    line = line.lower()
    for ch in line:
        key = ord(ch)
        if key >= 97 and key <= 122:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

print d
        
print sorted(d.items(), key = lambda x:x[1], reverse=True)

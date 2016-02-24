def sort_version_numbers(v):
    s = []
    for ver in v:
        s.append((ver.split('.')))
    s = sorted(s, key = lambda x:(x[0], x[1]))

    for i in range(len(s)):
        v = s[i][0] + '.' + s[i][1]
        s[i] = v

    print s
    
v = ["2.3", "3.2", "1.41", "1.06"]
sort_version_numbers(v)

def add_string(a, b, radix):
    carry = 0
    
    hex_mappings = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    
    if len(a) > len(b):
        # pad b
        b = ('0' * (len(a) - len(b))) + b
    elif len(b) > len(a):
        # pad a
        a = ('0' * (len(b) - len(a))) + a

    result = ['0'] * len(a)
    
    for i in xrange(len(a) - 1, -1, -1):
        s = int(a[i], radix) + int(b[i], radix) + carry
        result[i] = str(s % radix)
        carry = s/radix

    return ''.join(result)

a = raw_input()
b = raw_input()

print add_string(a, b, 2)

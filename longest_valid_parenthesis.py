import sys

def longest_valid_parenthesis(s):

    if len(s) == 0:
        return 0

    start = 0
    # skip closing ones at the start
    while start < len(s) and s[start] == ')':
        start += 1

    max_length = 0
    l = 0
    stack = []
    prev = 0
    old = 0

    for i in range(start, len(s)):
        if s[i] == '(':
            stack.append(i)
            old = l
        if s[i] == ')':

            if len(stack) == 0:
                continue

            cur = stack.pop()

            print stack, cur, i
            if cur < prev + 2:
                l += 2
                prev = i
            else:
                print cur, prev
                l = 2

        if l > max_length:
            max_length = l

    if len(stack) == 0:
        max_length = max_length + old

    return max_length

print longest_valid_parenthesis('()(())')
#print "\n"
#print longest_valid_parenthesis('()(()')
#print "\n"
#print longest_valid_parenthesis('((()')

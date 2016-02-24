def match_parenthesis(s):
    stack = []
    mapping = {'(' : ')', '{' : '}', '[' : ']'}
    open_set = set(mapping.keys())
    close_set = set(mapping.values())
    for ch in s:
        if ch in open_set:
            stack.append(ch)
        if ch in close_set:
            if ch != mapping[stack.pop()]:
                return False

    return len(stack) == 0

s = raw_input()
print match_parenthesis(s)
        

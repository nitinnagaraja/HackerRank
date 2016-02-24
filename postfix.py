def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    

def  rpn_calculate(tokens):
    stack = []
    res = 0

    if len(tokens) == 0:
        print "Invalid input"
        return

    for ch in tokens:
        if is_integer(ch):
            stack.append(int(ch))
        else:
            if len(stack) < 2:
                print "Invalid input"
                return
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if ch == '+':
                    res = op1 + op2
                elif ch == '-':
                    res = op2 - op1
                elif ch == '*':
                    res = op1 * op2
                else:
                    if op1 == 0:
                        print "Invalid input"
                        return
                    res = op2 / op1
                stack.append(res)

    if len(stack) > 1:
        print "Invalid input"
        return
    
    print res

rpn_calculate(['3', '4', '5', '*', '-'])
rpn_calculate(['10', '100', '-', '90', '+'])
rpn_calculate([ '4', '5', '+', ')'])
rpn_calculate([''])
rpn_calculate(['6', '6', '-', '6', '6', '-', '/'])

rpn_calculate(['1', '1', '-', '1', '1', '-', '1', '+', '/'])

def longestValidParentheses(s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        stack = []
        pairs = []
        
        for i in xrange(len(s)):
            if s[i] == '(':
                l = [i, -1]
                stack.append(l)
            else:
                if len(stack) == 0:
                    continue
                stack[-1][1] = i
                t = tuple(stack.pop())
                while len(pairs) > 0 and pairs[-1][0] > t[0] and pairs[-1][0] < t[1] and pairs[-1][1] > t[0] and pairs[-1][1] < t[1]:
                    del pairs[-1]
                pairs.append(t)

        if len(pairs) == 0:
            return 0

        end = pairs[0][1]
        l = end - pairs[0][0] + 1
        maxl = l

        for i in xrange(1, len(pairs)):
            item = pairs[i]
            if item[0] == end + 1:
                l += (item[1] - item[0] + 1)
            else:
                l = item[1] - item[0] + 1

            if l > maxl:
                maxl = l

            end = item[1]

        return maxl

##print longestValidParentheses(")(()((((())")
###print "\n"
##print longestValidParentheses('()(()')
###print "\n"
##print longestValidParentheses('((()')

print longestValidParentheses(raw_input())

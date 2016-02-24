def simplifyPath(path):
        """
        :type path: str
        :rtype: str
        """
        dirs = filter(None, path.split("/"))
        
        stack = []
        
        for item in dirs:
            if item == ".":
                continue
            
            if item == "..":
                if len(stack) != 0:
                    stack.pop()
                    continue
            else:
                stack.append(item)

    
        if len(stack) == 0:
            return "/"

        return "/" + "/".join(stack)

path = raw_input()
print simplifyPath(path)

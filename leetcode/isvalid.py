s = "()"
# s = "()[]{}"
# s = "(]"

def isValid(s):
    stack = []
    d= {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for c in s:
        if c in d:
            if not stack or stack.pop() != d[c]:
                return False
        else:
            stack.append(c)

    return stack == []

print(isValid(s))
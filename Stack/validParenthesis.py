def isValid(s: str) -> bool:
    '''
    LeetCode #20: Valid Parenthesis
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    '''
    if len(s) % 2 != 0:
        return False
    
    stack = []

    for i in s:
        if i == '(' or i == '[' or i =='{':
            stack.append(i)
        elif len(stack) == 0:
            return False
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif i == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif i == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False



print(isValid("()"))   # Outputs True
print(isValid("()[]{}"))   # Outputs True
print(isValid("(]"))   # Outputs False
print(isValid("([])"))   # Outputs True
print(isValid("([)]"))   # Outputs False

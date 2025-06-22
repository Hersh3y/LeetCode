def isValid(s: str) -> bool:
    '''
    LeetCode #20: Valid Parenthesis
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    :type s: str
    :rtype: int
    '''
    stack = []
    hashmap = {'}':'{',')':'(',']':'['}
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif not stack:
            return False
        elif hashmap[i] == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack


print(isValid("()"))   # Outputs True
print(isValid("()[]{}"))   # Outputs True
print(isValid("(]"))   # Outputs False
print(isValid("([])"))   # Outputs True
print(isValid("([)]"))   # Outputs False
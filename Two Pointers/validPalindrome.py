def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    l = 0
    r = len(s) - 1
    while r > l:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama")) # Outputs True
print(isPalindrome("race a car")) # Outputs False
print(isPalindrome(" ")) # Outputs True
def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stringlist = []
    for i in s:
        if i.isalnum():
            stringlist.append(i.lower())
    return stringlist == stringlist[::-1]


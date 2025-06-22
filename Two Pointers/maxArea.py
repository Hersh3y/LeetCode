def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    l = 0
    r = len(height) - 1
    while r > l:
        area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, area)
        if height[r] < height[l]:
            r -= 1
        else:
            l += 1
    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7])) # Outputs 49
print(maxArea([1,1])) # Outputs 1
print(maxArea([1,7,2,5,4,7,3,6])) # Outputs 36
print(maxArea([2,2,2])) # Outputs 4
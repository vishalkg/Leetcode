def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """

    """
    # Approach 1: Find max on the left and right of an element
    # Water stored at that index = min(left_max,right_max)-height[index]
    # Space: O(n), Time: O(n)
    left = [0]*len(height);left[0] = height[0]
    right = [0]*len(height);right[len(height)-1] = height[-1]
    for i in range(1,len(height)):
        left[i] = max(left[i-1],height[i])
    for i in range(len(height)-2,-1,-1):
        right[i] = max(right[i+1],height[i])
    water = 0
    for i in range(len(height)):
        water += min(left[i],right[i])-height[i]
    return water
    """

    # Approach 2: Optimizing for space
    # Calculate water at an i|j whichever(height[i],height[j]) is smaller
    # based on current left_max and right_max
    left_max = right_max = 0
    i,j = 0,len(height)-1
    water = 0
    while i<j:
        if height[i]<height[j]:
            if height[i]>left_max:
                left_max = height[i]
            else:
                water += left_max-height[i]
                i += 1
        else:
            if height[j]>right_max:
                right_max = height[j]
            else:
                water += right_max-height[j]
                j -= 1
                
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
            
        
# Simple Binary Search

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums)==1:
        return 0 if target<=nums[0] else 1
    if target>nums[-1]: return len(nums)
    if target<nums[0]: return 0
    s,e = 0,len(nums)-1
    while s<=e:
        m = (s+e)//2
        if nums[m] == target:
            return m
        else:
            if target>nums[m]: s = m+1
            else: e = m-1
    return s

nums,target = [1],1
print(searchInsert(nums,target)) # Output 0
nums,target = [1,3],2
print(searchInsert(nums,target)) # Output 1
# Idea: The array can contain at most n positive integers
# Find a valid integer and put it at its correct position using swapping

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    
    def swap(nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    while i<len(nums):
        if nums[i]==i+1 or nums[i]<=0 or nums[i]>len(nums):
            i += 1
        elif nums[nums[i]-1] != nums[i]:
            swap(nums,i,nums[i]-1)
        else:
            i += 1
        #print(nums)
    i = 0
    while i<len(nums) and nums[i]==i+1:
        i += 1
    return i+1

nums = [3,1,-1,-1]
print(firstMissingPositive(nums))
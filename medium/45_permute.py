# All entries are unique
# Call the same function recursively for nums[0:i]+nums[i+1:]
# Combine nums[i] with the result

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums)<=1:
        return [nums]
    if len(nums)==2:
        return [[nums[0],nums[1]],[nums[1],nums[0]]]
    
    ans = []
    for i in range(len(nums)):
        temp = nums[0:i]+nums[i+1:]
        sub_list = permute(temp)
        for entry in sub_list:
            ans.append([nums[i]]+entry)
    return ans
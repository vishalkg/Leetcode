# First decide, in which section min element lies
# Then based on target value, manage the start/end lable

def searchInRotatedSortedArray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(n) Soln
        '''
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1
        '''
        if len(nums)==0:
            return -1
        if len(nums)==1:
            if nums[0] == target: return 0
            else: return -1
        
        # O(log n) soln
        start = 0
        end  = len(nums)-1
        while start < end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            if nums[start]<=nums[mid]:
                if target>=nums[start] and target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target>nums[mid] and target<=nums[end]:
                    start = mid+1
                else:
                    end = mid-1
        if nums[start]==target:
            return start
        return -1
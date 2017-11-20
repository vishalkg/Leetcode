def searchRange(self, nums, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==[]:
            return [-1,-1]
        if nums[0]==nums[-1]==t:
            return [0,len(nums)-1]
        if not nums[0]<=t<=nums[-1]:
            return [-1,-1]
        '''s,e = 0,len(nums)-1
        result = [-1,-1]
        while s<=e:
            #print(s,e)
            m = (s+e)//2
            if (m==0 or nums[m-1]<t) and nums[m]==t:
                result[0] = m
                break
            elif nums[m]<t:
                s = m+1
            else:
                e = m-1
        if result[0] == -1:
            return [-1,-1]

        # We found the occurence of 1st element
        # We can do the same for the index of last element or we can optimize it a bit
        # Instead of searching from index = 0, set start index = index of 1st occurence
        else:
            s,e = result[0],len(nums)-1
            while s<=e:
                m = (s+e)//2
                if (m==len(nums)-1 or nums[m+1]>t) and nums[m]==t:
                    result[1] = m
                    break
                elif nums[m]>t:
                    e = m-1
                else:
                    s = m+1
        return result
        '''
        # Approach 2: Find any index of occurence and build the range in both directions
        # In worst cases it can be more expensive but mostly efficient than 1st approach 
        s,e = 0,len(nums)-1
        while s<e:
            m = (s+e)//2
            if nums[m]<t:
                s = m+1
            elif nums[m]>t:
                e = m-1
            else:
                s = e = m
        if nums[s]!=t:
            return [-1,-1]
        while s>=0 and nums[s]==t:
            s -= 1
        while e<len(nums) and nums[e]==t:
            e += 1

        return [s+1,e-1]
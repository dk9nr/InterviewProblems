def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last=0
        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                last+=1
                nums[last]=nums[i]
        return last+1
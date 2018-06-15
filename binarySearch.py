def searchInsert(self, nums, target):
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            if nums[0]!=target and nums[1]!=target:
                return 1
        n=len(nums)
        mid=len(nums)/2
        if nums[mid]==target:
            return mid
        if target>mid:
            self.searchInsert(nums[mid:n],target)
        if target<mid:
            self.searchInsert(nums[0:mid],target)
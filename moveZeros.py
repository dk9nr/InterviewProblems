def moveZeroes(self, nums):
        last=0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[last]=nums[i]
                last+=1
        for i in range (last,len(nums)):
            nums[i]=0
        
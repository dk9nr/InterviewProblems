def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left=0
        mid=0
        right=len(nums)-1
        
        while mid<=right:
            if nums[mid]==0:
                nums[mid],nums[left]=nums[left],nums[mid]
                left+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[right],nums[mid]=nums[mid],nums[right]
                right-=1
        return nums
        

if __name__ == "__main__":
    print(sortColors([2,1,0,0,2,1,2,1,0]))
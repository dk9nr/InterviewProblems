def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        mini=min(nums[0],nums[1])
        maxi=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            if nums[i]<mini:
                mini=nums[i]
            elif nums[i]<maxi:
                maxi=nums[i]
            else:
                return True
        return False

if __name__ == "__main__":
    
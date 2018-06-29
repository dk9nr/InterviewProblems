def threeSum(nums):
        results=[]
        nums.sort()
        for i in range (0,len(nums)-2):
            for j in range (i+1,len(nums)-1):
                for k in range (j+1,len(nums)):
                    if nums[i]+nums[k]+nums[j]== 0:
                        if [nums[i],nums[j],nums[k]] not in results:
                            results.append([nums[i],nums[j],nums[k]])
        return results

if __name__ == "__main__":
    arr=[-1,-2,-3,0,1,2,3,4]
    x= threeSum(arr)
    print (arr)
    print (x)
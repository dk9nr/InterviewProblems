def reverse(nums, start, end):
    while start<end:
        nums[start],nums[end] = nums[end],nums[start]
        start+=1
        end-=1

def shift(nums,k):
    reverse(nums,0,len(nums)-1)
    reverse(nums,0,k-1)
    reverse(nums,k,len(nums)-1)


if __name__ == "__main__":

    nums=[1,2,3,4,5,6]
    shift(nums,2)
    print (nums)
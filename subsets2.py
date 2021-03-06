def subsets(nums):
    l=[]
    nums.sort()
    backtrack(l,[],nums,0)
    return l

def backtrack(l,tempList,nums,start):
    l.append(tempList)
    for i in range (start,len(nums)):
        
        tempList.append(nums[i])
        backtrack(l,tempList.copy(),nums,i+1)
        tempList.pop()




def permute(nums): 
   l = []
   backtrack2(l, [], nums)
   return l

def backtrack2(l, tempList, nums):
    if len(tempList) == len(nums):
        l.append(tempList)
    else:
      for i in range(len(nums)):
        if (nums[i] in tempList):
            continue
        tempList.append(nums[i])
        backtrack2(l, tempList.copy(), nums)
        print (tempList)
        tempList.pop()
        print (tempList)

if __name__ == "__main__":
    print(permute([1,2,9]))
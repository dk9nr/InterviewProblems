def subsets(nums):
    helper(nums,[],0,[])
        
def printset(n):
    for i in n:
        if i != None:
            print (i)
    
def helper(given_array,subset,i,res):
    if i == len(given_array):
        res.append(subset)
    else:
        helper(given_array,subset.append(given_array[i]),i+1,res)
        helper(given_array,subset,i+1,res)

if __name__ == "__main__":
    subsets([1,2])


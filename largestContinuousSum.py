#whiteboard implementation
def lcs(arr):
    cs=ms=arr[1]
    for number in arr[1:]:
        cs=max(cs+number,number)
        ms=max(cs,ms)
    print (ms)

#answer
def largestContinuousSum(arr):
    if len(arr)==0:
        return
    maxSum=currentSum=arr[0]
    for num in arr[1:]:
        currentSum=max(currentSum+num, num)
        maxSum=max(currentSum, maxSum)
    return maxSum


if __name__ == "__main__":
    arr = [1,2,-1,3,4,10,10,-10,-1]
    arr = [-2,8,9,-2,2]
    lcs(arr)
from heapq import heappush, heappop
import collections
def topKFrequent(nums, k):
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        heap=[]
        answers=[]
        for value in hash:
            heappush(heap, [-hash[value],value])
        while k>0:
            a=heappop(heap)
            answers.append(a[1])
            k-=1
        return answers

def topKFrequent2(nums,k):
    if len(nums) < k:
            return []
    frequency = collections.Counter(nums)
    bucket = collections.defaultdict(list)
    for key in frequency:
        f = frequency[key]
        bucket[f].append(key)
    res = []
    count = len(nums) # the upper limit for res
    print (bucket)
    while len(res) < k:
        if bucket[count]:
            
            res += bucket[count]
        count -= 1
    return res
        

if __name__ == "__main__":
    print(topKFrequent2([1,2,9],2))
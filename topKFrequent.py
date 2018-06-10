def topKFrequent(self, nums, k):
        heap=[]
        answers=[]
        counter={}
        for i in nums:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        for i in counter:
            heapq.heappush(heap,[-counter[i],i])
        while k>0:
            k-=1
            answers.append(heapq.heappop(heap)[1])
        return answers
        
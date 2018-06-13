from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        one=Counter(nums1)
        two=Counter(nums2)
        a=[]
        for i in one:
            if i in two:
                x=min(one[i],two[i])
                b=([i]*x)
                a+=b
                
        return a
        
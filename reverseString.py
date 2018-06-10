def reverseString(self, s):
        s=list(s)
        ans=[]
        for letter in s:
            ans.insert(0,letter)
        return "".join(ans)
def titleToNumber(self, s):
        answer=0
        s=list(s)
        mult=1
        for letter in s[::-1]:
            answer+= (ord(letter)-64)*mult
            mult*=26
        return answer
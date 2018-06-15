import collections
def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    s=list(s)
    if len(s)==1:
        return 0


    c = collections.Counter(s)
    for i in range(0,len(s)):
        print (c[s[i]])
        if c[s[i]] == 1:
            return i
    return -1


if __name__ == '__main__':
    firstUniqChar('dddccdbba')
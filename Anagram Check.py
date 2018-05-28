# White implementation
def AC (s1,s2):
    d1= {}
    d2 = {}
    for letter in s1:
        if letter not in d1:
            d1.letter:1
        else:
            d1.letter.value=d1.letter.value + 1
    for letter in s2:
        if letter not in d2:
            d2.letter:1
        else:
            d2.letter.value=d2.letter.value + 1
    for key in d1:
        if key not in d2:
            return False
        if key.value != d2.key.value:
            return False
        return True

# First solution
def anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s=s.replace(' ','').lower()
    t=t.replace(' ','').lower()
    
    if(len(s)!=len(t)):
        return False
    counter = {}
    for letter in s:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    for letter in t:
        if letter in counter:
            counter[letter] -= 1
        else:
            return False

    for k in counter:
        if counter[k]!=0:
          return False
    
    return True
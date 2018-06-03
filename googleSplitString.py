def solution(S, K):
    # write your code in Python 3.6
    dashcount=0
    lettercount=0
    for char in S:
        if char == "-":
            dashcount+=1
        else:
            lettercount+=1
    num= lettercount//K
    new=""
    count=0
    for char in S[::-1]:
        if count == num:
            new+"-"
            count+=1
        else:
            new+char
            count += 1
    print (new.upper())

def splitgroups(A,K):
    A=A.replace("-","")
    A=list(A)
    for i in range(len(A)-K,0,-K):
        A.insert(i,"-")
    A="".join(A)
    print (A.upper())


def hehexD(a, b):
    characters = a.split('-')
    string = ''
    if len(a) % b != 0:
        string += (characters[0:b-1])
    else:
        string += (characters[0:b])
    for c in range(b, len(characters), b):
        string += charactersstr([c: c+b])
    return string
    
if __name__ == "__main__":
    hehexD('r',1)


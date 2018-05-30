#whiteboard implementation
def sr(s):
    final = ""
    hash= {}
    sorry=set()
    for letter in s:
        if letter not in hash:
            hash[letter]=1
        else:
            hash[letter] += 1
    
    for letter in s:
        if letter in sorry:
            continue    
        else:
            final += letter
            final += str(hash[letter])
            sorry.add(letter)
    print (final)
        


if __name__ == "__main__":
    s="AAAAYYBBBBNNNNN"
    sr(s)
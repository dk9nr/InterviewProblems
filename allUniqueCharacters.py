#whiteboard implementation
def auc(s):
    unique =set()
    for char in s:
        if char in unique:
            return False
        else:
            unique.add(char)
    return True


if __name__ == "__main__":
    s="abcdef"
    if auc(s):
        print ('true!')
    else:
        print ('false')
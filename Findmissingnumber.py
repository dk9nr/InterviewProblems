#whiteboard implementation
def finder (arr1,arr2):
    s=set()
    for number in arr2:
        s.add(number)
    for number in arr1:
        if number not in s:
            print (number)
        else:
            continue

if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7]
    arr2 = [3,7,2,1,4,6]
    finder(arr1,arr2)

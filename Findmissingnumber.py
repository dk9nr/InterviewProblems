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


#better solution, accounts for duplicates
def finder2 (arr1, arr2):
    sum=0
    for number in arr1:
        sum+=number
    for number in arr2:
        sum-=number
    print (sum)


if __name__ == "__main__":
    arr1 = [1,1,2,3,4,5,6,7]
    arr2 = [3,7,2,1,4,6,5,]
    finder(arr1,arr2)
    finder2(arr1,arr2)

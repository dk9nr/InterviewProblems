#whiteboard implementation
def lcs(arr):
    min=-999999999
    sum=0
    for number in arr:
        if number != 0:
            if number < 0 and number > min:
                min=number
            elif number > 0:
                sum +=number
            else:
                print("hi")
    if min==0 and sum==0:
        print (0)
    elif sum==0:
        print (min)
    else:
        print (sum)


if __name__ == "__main__":
    arr = [1,2,-1,3,4,10,10,-10,-1]
    lcs(arr)

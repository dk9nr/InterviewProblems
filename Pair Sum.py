#whiteboard implementation
def pair_sum (arr,k):
    s= set()
    answers= []
    for number in arr:
        value= k - number
        if value in set:
            answers.append((number,value))
        s.append(number)
    
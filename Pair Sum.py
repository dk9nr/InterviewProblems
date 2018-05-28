#whiteboard implementation
def pair_sum (arr,k):
    s= set()
    answers= []
    for number in arr:
        value= k - number
        if value in set:
            answers.append((number,value))
        s.append(number)

#answer
def pair_sum(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    
    
    # FOR TESTING
    return len(output)
    # Nice one-liner for printing output
    #return '\n'.join(map(str,list(output)))
def flip_horizontal_axis(matrix):
    new=[]
    for i in matrix[::-1]:
        new.append(i)
    print (new)
    return new
        
       

if __name__ == "__main__":
    flip_horizontal_axis([[1,0,0],[0,0,1]])
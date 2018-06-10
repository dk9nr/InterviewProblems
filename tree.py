# def number_of_leaves(self,root):
        # if self.root.left_child==None:
        #     if self.root.right_child==None:
        #         self.count+=1
        # self.root.left_child.number_of_leaves(self)
        # self.root.right_child.number_of_leaves(self)
        # return self.count

        # if root.left_child==None
        # return self.number_of_leaves(root.left_child)


# def merge_ranges(input_range_list):
#     output=[]
#     upper=input_range_list[0][1]
#     lower=input_range_list[0][0]
#     for i in input_range_list:
        
#         if i[0] <= upper:
#             if i[1]>upper:
#                 upper=i[1]
#         else:
#             output.append([lower,upper]
#             lower=i[0]
#             upper=i[1]
        
def dashSplit(S,K):
    s=S.replace("-","")
    s=list(s)
    for letter in range (len(s)-K,0,-K):
        s.insert(letter,"-")
    s="".join(s)
    print (s)

        
       

if __name__ == "__main__":
    (dashSplit("hello-ar",2))
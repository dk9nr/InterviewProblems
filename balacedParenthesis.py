#whiteboard implementation
class Stack(object):

    def __init__(self):
        self.body=[]
        self.length=0
    
    def isEmpty(self):
        if self.body==[]:
            return True
        else:
            return False

    def push(self,value):
        self.body.append(value)
        self.length += 1

    def pop(self):
        self.body.pop()
        self.length -= 1

    def peek(self):
        if not self.isEmpty():
            return self.body[self.length-1]
        else:
            return False


def bc(s):
    stk=Stack()
    for c in s:
        if c == "(" or c== "[" or c== "{":
            stk.push(c)
        elif c == ")" and stk.peek() == "(":
            stk.pop()
        elif c == "]" and stk.peek() == "[":
            stk.pop()
        elif c == "}" and stk.peek() == "{":
            stk.pop()
            
        elif c == ")" and stk.peek() != "(":
            return False
        elif c == "]" and stk.peek() != "[":
            return False
        elif c == "}" and stk.peek() != "{":
            return False
    if stk.isEmpty():
        return True
        
        




if __name__ == "__main__":
    if bc('[[[]])]'):
         print ("True")
    else:
        print ("False")
    
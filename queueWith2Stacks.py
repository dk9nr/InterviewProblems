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


class Queue(object):
    def __init__(self):
        self.stk1=Stack()
        self.stk2=Stack()
        self.pushStack=self.stk1
        self.popStack=self.stk2

    def enqueue(self,value):
        self.pushStack.push(value)
        return str(self.pushStack.peek())

    def dequeue(self):
        while self.pushStack.isEmpty() == False:
            self.popStack.push(self.pushStack.peek())
            self.pushStack.pop()
        peekValue= self.popStack.peek()
        self.popStack.pop()
        return str(peekValue)
        
        




if __name__ == "__main__":
    q=Queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q.dequeue)
    
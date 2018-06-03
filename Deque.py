#whiteboard implementation
class Deque (object):
    def __init__(self):
        self.body=[]
        self.size=0
    
    def push_front(self,value):
        self.body.insert(0,value)
        self.size += 1

    def push_back(self,value):
        self.body.append(value)
        self.size += 1

    def pop_front (self):
        self.body.pop(0)
        self.size -= 1

    def pop_back (self):
        self.body.pop()
        self.size -= 1

if __name__ == "__main__":
    s=Deque()
    s.push_back(9)
    print (s.body)

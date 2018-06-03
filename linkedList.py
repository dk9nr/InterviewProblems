#whiteboard implementation
class node(object):

    def __init__(self,value=None):
        self.value= value
        self.next= None
        self.prev= None

class LinkedList(object):

    def __init__(self):
        head= node()
        tail= node()
        head.next=tail
        tail.prev=head

    def insert(self,value):
        new=node(value)
        





if __name__ == "__main__":
    q=Queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q.dequeue)
    
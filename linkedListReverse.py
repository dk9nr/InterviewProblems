#whiteboard implementation
class node(object):

    def __init__(self,value=None):
        self.value= value
        self.next= None

def reverse(head):
    current = head
    prev= None
    next=None

    while current:
        next=current.next
        current.next=prev
        prev=current
        current=next
    return prev

    
        




if __name__ == "__main__":
    a = node(1)
    b = node(2)
    c = node(3)
    d = node(4)

    a.next=b
    b.next=c
    c.next=d

    print (a.next.value)
    print (b.next.value)
    print (c.next.value)
    reverse(a)
    print (d.next.value)
    print (c.next.value)
    print (b.next.value)
    
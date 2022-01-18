class Node:
    def __init__(self, item,next):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None

    def push(self,value):
        if not self.front:
            self.front =Node(value,None)
            return
        node = self.front
        while node and node.next:
            node = node.next
        node.next = Node(value,None)



    def pop(self):
        if not self.front:
            return None
        node = self.front
        self.front = self.front.next
        return node.item

    def is_empty(self):
        return self.front is None



def test_queue():
    #  스택은 3가지 기능이 필요하다 1. push 2. pop 3. is_empty
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.is_empty()

test_queue()
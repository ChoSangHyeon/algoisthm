# Chapter09_25. 원형 큐 디자인 (259p)
# 난이도 : ★★
# Leet code Num. : 622

# 원형 큐를 디자인 하라
# MyCircularQueue circularQueue = new MyCircularQueue(5); // 크기를 5로 지정
# circularQueue.enQueue(10);    // true 리턴
# circularQueue.enQueue(20);    // true 리턴
# circularQueue.enQueue(30);    // true 리턴
# circularQueue.enQueue(40);    // true 리턴
# circularQueue.Rear();         // 40 리턴
# circularQueue.isFull;         // false 리턴
# circularQueue.deQueue();      // true 리턴
# circularQueue.deQueue();      // true 리턴
# circularQueue.enQueue(50);    // true 리턴
# circularQueue.enQueue(60);    // true 리턴
# circularQueue.Rear();         // 60
# circularQueue.Front();        // 30 리턴
class Node:
    def __init__(self, item,next):
        self.item = item
        self.next = next

class circularQueue:
    def __init__(self):
        self.head = None

    def MyCircularQueue(self,int):
        node = Node(self, None)
        self.head = None
        self.head.next  = node
        while int>0:
            node.next = node
            int -=1
        node.next = self.head
        return
    def enQueueu(self,val):
        node = self.head
        node.item = val
        for i in range(len(node)-1):
            node = node.next
        node.next = self.head

    def deQueue(self):
        node = self.head
        node.item = None
        for i in range(len(node) - 1):
            node = node.next
        node.next = self.head


    def Rear(self):
        node = self.head
        for i in range(len(node) - 1):
            node = node.next
        return node.item

    def Front(self):
        node = self.head
        node = node.next
        return node.item

    def isFull(self):
        



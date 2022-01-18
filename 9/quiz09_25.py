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

class MyCircularQueue:
    def circularQueue(self,int):
        while int >0:
            Node(self,None,Node.Next)
            


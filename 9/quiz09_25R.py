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
class MyCircularQueue:

    def __init__(self, k: int):
        self.cular = [0] * k
        self.maxlen = k
        self.count = 0
        self.front = 0
        self.rare = 0

    def enQueue(self, val: int) -> bool:
        if self.isFull():
            return False
        self.cular[self.rare] = val
        self.rare = (self.rare + 1) % self.maxlen
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.cular[self.front] = None
        self.front = (self.front + 1) % self.maxlen
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cular[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cular[self.rare - 1]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.maxlen:
            return True
        return False

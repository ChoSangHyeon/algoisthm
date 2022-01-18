# Chapter09_24. 스택을 이용한 큐 구현 (257p)
# 난이도 : ★
# Leet code Num. : 225

# 스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
# push(x) : 요소 x를 큐 마지막에 삽입한다.
# pop() : 큐 처음에 있는 요소를 삭제한다.
# peek() : 큐 처음에 있는 요소를 조회한다.
# empty() : 큐가 비어 있는지 여부를 리턴한다.

# Myqueue queue = new Myqueue();
# queue.push(1);
# queue.push(2);
# queue.peek();  // 1 리턴
# queue.pop();  // 1 리턴
# queue.empty();    // false 리턴
class Node:
    def __init__(self, item,next):
        self.item = item
        self.next = next
class queue:
    def __init__(self):
        self.front = None
    def push(self,value):
        if self.front is None:
            self.front = Node(self,value)
            return
        node = self.front
        while node.next:
            node = node.next
        node.next = Node(self.value)
        return

    def pop(self):
        if not self.front:
            return None
        node = self.front
        self.front = self.front.next
        node.next = None
        return node.item

    def peek(self):
        if not self.front:
            return None
        return self.front.item

    def is_empty(self):
        return self.front is None


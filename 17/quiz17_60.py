# Chapter17_60. 삽입 정렬 리스트 (500p)
# 난이도 : ★★
# Leet code Num. : 147

# 연결 리스트를 삽입 정렬로 정렬하라

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def insert(lst):
    node, prev = lst, None
    cnt = 0
    while node:
        next, node.next = node.next, prev
        prev,node = node, next
        cnt += 1

    for i in range(cnt):
        for _ in range(i):
            if node.next.val > node.val:
                node.next.val, node.val = node.val, node.next.val
            node = node.next

    node1, prev1 = lst, None
    while node1:
        next1, node1.next = node1.next, prev1
        prev1,node1 = node1, next1

    return node1


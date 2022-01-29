# Chapter17_60. 삽입 정렬 리스트 (500p)
# 난이도 : ★★
# Leet code Num. : 147

# 연결 리스트를 삽입 정렬로 정렬하라

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def insert(lst):
    head = lst[:]
    while lst.next:

        while lst:
            a = lst.val
            if lst.next.val < lst.val:
                lst.next.val = lst.val


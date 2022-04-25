# Chapter08_15. 역순 연결 리스트 (219p)
# 난이도 : ★
# Leet code Num. : 206

# 연결 리스트를 뒤집어라
# 예제 1.
# 입력 >> 1->2->3->4->5->NULL
# 출력 >> 5->4->3->2->1->NULL

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseList(self, node: ListNode) -> ListNode:
        rev = None
        slow = node
        while slow:
            rev, rev.next, slow = slow, rev, slow.next
        return rev

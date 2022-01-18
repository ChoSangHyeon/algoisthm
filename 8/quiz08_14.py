# Chapter08_14. 두 정렬 리스트의 병합 (213p)
# 난이도 : ★
# Leet code Num. : 21

# 정렬되어 있는 두 연결 리스트를 합쳐라
# 예제 1.
# 입력 >> 1->2->4, 1->3->4
# 출력 >> 1->1->2->3->4->4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
#
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if (not l1) or (l2 and l1.val > l2.val):
#             l1, l2 = l2, l1
#         if l1:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1

#
# l1 1[-> 2[-> 3]] --> 2[->3[]]       --> 1[->1[->4[]]] --> 1[->4[]] --> 4[]      --> 2[->3[]]--> 3[] --> none
# l2 1[-> 1[-> 4]]     1[->1[->4[]]]      2[->3[]]          2[->3[]]     2[->3[]]     4[]         4[]     4[]

dum = ListNode()
tail = dum

print(dum)
print(tail)

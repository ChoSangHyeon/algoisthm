# Chapter08_18. 홀짝 연결 리스트 (233p)
# 난이도 : ★★
# Leet code Num. : 328

# 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라
# 예제 1.
# 입력 >> 1->2->3->4->5->NULL
# 출력 >> 1->3->5->2->4->NULL
# 예제 2.
# 입력 >> 2->1->3->5->6->4->7->NULL
# 출력 >> 2->3->6->7->1->5->4->NULL

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def evenOddList(self, node: ListNode) -> ListNode:
        odd = node
        even = node.next
        even_head = node.next
        while even or even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head

        return node



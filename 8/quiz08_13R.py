# Chapter08_13. 팰린드롬 연결 리스트 (201p)
# 난이도 : ★
# Leet code Num. : 234

# 연결 리스트가 팰린드롬 구조인지 판별하라 (팰릳드롬의 정의가 기억나지 않는다면 138페이지를 다시 참고하라,)
# 예제 1.
# 입력 >> 1->2
# 출력 >> false
# 예제 2.
# 입력 >> 1->2->2->1
# 출력 >> true

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        print(slow.val)
        print(fast.next)
        print(head)
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev



head1 = [1,2,3,2,2]
head2 = ListNode([1,2,3,3])

hi = Solution()
print(hi.isPalindrome(head1))
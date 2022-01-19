# Chapter09_29. 보석과 돌 (298p)
# 난이도 : ★
# Leet code Num. : 771

# J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? (대소문자를 구분한다)
# 예제 1.
# 입력 >> J = "aA", S = "aAAbbbb"
# 출력 >> 3
import collections

class ListNode:
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.next = None

class SJ:
    def __init__(self):
        self.size = 1000
        self.dic = collections.defaultdict()

    def stone(j,s):
        



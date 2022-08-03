# Chapter09_29. 보석과 돌 (298p)
# 난이도 : ★
# Leet code Num. : 771

# J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? (대소문자를 구분한다)
# 예제 1.
# 입력 >> J = "aA", S = "aAAbbbb"
# 출력 >> 3
def sj(j,s):
    dic = []
    cnt = 0
    for i in j:
        dic.append(i)
    for k in s:
        if k in dic:
           cnt += 1
    return cnt
    print(dic)
print(sj('aA','adsdAf'))

# =====================
# import collections
#
# class ListNode:
#     def __init__(self,key=None,val=None):
#         self.key = key
#         self.val = val
#         self.next = None
#
# class SJ:
#     def __init__(self):
#         self.size = 1000
#         self.dic = collections.defaultdict()
#         self.cnt = collections.Counter
#
#     def stone(self,j,s):
#         for _ in j:
#
#         index = j % self.size
#         if not self.dic:
#             self.dic[index] = ListNode(j,s)
#         temp = self.dic[index]
#
#


# 해시테이블을 이용한 풀이

def hashSol(j:str,s:str) -> int:
    freqs = {}
    count = 0
    for char in s:
        # 여기에서 값이 없음을 IF문으로 처리해줬었는데 defaultdict를 사용하면 값이없을때 초기값부여가 쉽다.
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    for char in j:
        if char in freqs:
            count += freqs[char]
    return count
    

print(hashSol('ac','accCccAs'))

# Chapter09_31. 상위 K 빈도 요소 (307p)
# 난이도 : ★★
# Leet code Num. : 347

# 상위 K 이상 등장하는 요소를 추출하라
# 예제 1.
# 입력 >> nums = [1, 1, 1, 2, 2, 3], k = 2
# 출력 >> [1, 2]
import collections

#
# def count(nums:list,k:int):
#     a = list(sorted(list(set(nums)), key=lambda x: nums.count(x), reverse=True))[:k]
#     b = sorted(list(set(nums)), key=lambda x: nums.count(x), reverse=True)[:k]
#     d = list(set(nums))
#     c = sorted(list(set(nums)), key=lambda x: d.count(x), reverse=True)[:k]
#     return print(a,b,c)

def tok(nums,k):
    print(collections.Counter(nums))
    print(collections.Counter(nums).most_common())
    print(list(zip(*collections.Counter(nums).most_common())))
    print(list(zip(collections.Counter(nums).most_common())))
    return list(zip(*collections.Counter(nums).most_common(k)))[0]

# from collections import Counter
# def top(nums, k):
#     cnt = Counter(nums)
#     print(cnt)
#     print(cnt.most_common())
#     most_common_k = cnt.most_common(k)
#     print(most_common_k)
#     answer = [num[0] for num in most_common_k]
#     return answer

nums = [1,2,3,6,7,5,5,5,5,6]
k = 2
print(tok(nums,k))

# class Solution1:
#     def topKFrequent(self, nums, k):
# #         zip 함수는 여러개의 리스트를 묶어주는데 가장 수가 적은 리스트 기준으로 묶고 나머지는 버린다.
# #         
# #         아스테리스크(*)는 언패킹의 개념으로 출력에서 리스트를 풀어해쳐서 작성하는 모습을 볼수있다. 그리고 입력파라미터로 사용되면 
# #         입력값이 여러개가 들어와도 그것을 리스트로 묶어서 처리하게된다 print문과 매우 유사하다.
#         return list(zip(*collections.Counter(nums).most_common(k)))[0]
#
# import heapq
# from typing import List
#
#
# class Solution2:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freqs = collections.Counter(nums)
#         freqs_heap = []
#         # 힙에 음수로 삽입
#         for f in freqs:
#             heapq.heappush(freqs_heap, (-freqs[f], f))
#
#         topk = list()
#         # k번 만큼 추출, 민 힙 이므로 가장 작은 음수 순으로 추출
#         for _ in range(k):
#             topk.append(heapq.heappop(freqs_heap)[1])
#
#         return topk

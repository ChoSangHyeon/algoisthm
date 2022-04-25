import collections
import heapq

# def heapq1(nums,k):
#     heap1 = list()
#     for i in nums:
#         heapq.heappush(heap1,-i)
#     for _ in range(k-1):
#         heapq.heappop(heap1)
#     return -heapq.heappop(heap1)

a = [3,2,3,1,2,4,5,5,6]
k = 4

# def heapq2(nums,k):
#     heapq.heapify(nums)
#     for _ in range(len(nums)-k):
#         heapq.heappop(nums)
#     return heapq.heappop(nums)
#
# def heapq3(nums,k):
#     return heapq.nlargest(k,nums)[-1]

def heapq4(nums,k):
    return sorted(nums,reverse=True)[k-1]

print(heapq4(a,k))
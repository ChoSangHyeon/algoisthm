# 두배열의 교집합
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.
#
# 349
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
import bisect


def insert(nums1:list[int],nums2:list[int]):
    if not nums1 or not nums2:
        return
    res = set()
    nums2.sort()
    for i in nums1:
        idx = bisect.bisect_left(nums2,i)
        if idx < len(nums2) and nums2[idx] == i:
            res.add(i)
    return list(res)
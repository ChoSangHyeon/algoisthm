#회전 정렬된 배열 검색
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown
# pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1]
# , ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example,
# [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the
# index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

#33

# #Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


def search(lst: list[int], target: int) -> int:
    pivot = 0
    if lst[0] > lst[-1]:
        start, end = 0, len(lst) - 1
        while start <= end:
            mid = (start+end)//2
            if lst[start] < lst[mid]:
                start = mid+1
            elif lst[start] > lst[mid]:
                end = mid
            if end-start <=1:
                pivot = end
                break
    if pivot!=0:
        lst1= lst + lst[:pivot]
    else:
        lst1 = lst
    def gogo(st,ed):
        if st <= ed:
            mid = (st+ed)//2
            if lst1[mid] > target:
                return gogo(st,mid-1)
            elif lst1[mid] < target:
                return gogo(mid+1,ed)
            else:
                return mid
        else:
            return -1

    a = gogo(pivot, len(lst1) - 1)
    if a == -1:
        return -1
    if target <= lst[-1]:
        return a
    else:
        return a - len(lst)

nums = [4,5,6,7,8,9,0,1,2]
target = 1
print(search(nums,target))

# def bs_rotated(nums, target):
#     def bs(lst, start, end):
#         if start > end:
#             return -1
#
#         mid = (start + end) // 2
#         if lst[mid] < target:
#             return bs(lst, mid + 1, end)
#         elif lst[mid] > target:
#             return bs(lst, start, mid - 1)
#         else:
#             return mid
#
#     if not nums:
#         return -1
#
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] > nums[right]:
#             left = mid + 1
#         else:
#             right = mid
#
#     added = nums + nums[:left]
#
#     result = bs(added, left, len(added) - 1)
#     return result if result == -1 else result % len(nums)

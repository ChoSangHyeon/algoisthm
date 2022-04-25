#이진검색
# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums. If
# target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#704
#Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

def ejin(nums,target):
    sta,end = 0,len(nums)-1
    def infun(st,ed):
        mid = (st+ed)//2
        if nums[mid] < target:
            # 리턴 -1을 그대로 가져오거나 리턴값이 존재하면 포도시 가져옴
            return infun(mid,ed)
        elif nums[mid] > target:
            return infun(st,mid)
        else:
            return mid
    return infun(sta,end)
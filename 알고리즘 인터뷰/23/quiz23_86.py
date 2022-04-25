import sys


def findMax(nums:list[int])->int:
    curNum = 0
    maxNum = -sys.maxsize
    for num in nums:
        curNum = max(num, curNum+num)
        maxNum = max(maxNum,curNum)

    return maxNum
def findMax1(nums:list[int])->int:
    for i in range(1,len(nums)):
        if nums[i-1]>0:
            nums[i] = nums[i-1]+nums[i]
    return max(nums)
# 두수의합2
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order
# find two numbers such that they add up to a specific target number. Let these two numbers
# be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer
# array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.
#
# Your solution must use only constant extra space.
#
# 167
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
#
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
import bisect


def sum_num(numbers,target):
    res = []

    def find_num(lst, base, idx):
        hi = bisect.bisect_left(lst, target - base)
        print(idx)
        print(hi)
        if hi < len(lst) and lst[hi] == target - base:
            print('hi')
            return hi + idx
        else:
            return -1

    for a in range(len(numbers) - 1):
        temp = find_num(numbers[a + 1:], numbers[a], a)
        if temp != -1:
            res.append(a + 1)
            res.append(temp + 2)
    res.sort()
    return res

def tow(numbers,target):
    i,j = 0,len(numbers)-1
    while i <= j:
        if numbers[i]+numbers[j]-target < 0:
            i +=1
        elif numbers[i]+numbers[j]-target > 0:
            j -=1
        else:
            return [i+1,j+1]
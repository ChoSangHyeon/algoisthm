# Chapter07_09. 세 수의 합 (184p)
# 난이도 : ★★
# Leet code Num. : 15

# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
# 예제 1.
# 입력 >> nums = [-1, 0, 1, 2, -1, -4]
# 출력 >> [ [-1, 0, 1], [-1, -1, 2] ]

from typing import List



def threeSum( nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 합 `sum` 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # `sum = 0`인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results
a = [1,2,4,4,5,5,5,6,10,-2,-4,-5,-7,-10]
a.sort()
print(a)
print(threeSum(a))

# def three(num1 : list[int])->list[list[int]]:
#     num = sorted(num1)
#     i=0.5
#     j=len(num)-1
#     map = {}
#     return1 = []
#     for a, b in enumerate(num):
#         map[b] = a
#     while len(num)-1 >= int(i):
#         if -(num[int(i)]+num[int(j)]) in range(num[int(i)],num[int(j)]):
#             for a, b in enumerate(num):
#
#                 if -(num[int(i)]+num[int(j)]) in map and a != map[num[int(i)]] and a != map[num[int(j)]]:
#                     c = [num[int(i)], num[map[-(num[int(i)]+num[int(j)])]], num[int(j)]]
#                     return1.append(c)
#         i += 0.5
#         j -= 0.5
#
#     return return1
#
#
# if __name__ == "__main__":
#     nums = [-1, 0, 1, 2,-2, 5, -4]
#     print(three(nums))



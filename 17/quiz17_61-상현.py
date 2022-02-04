# # Chapter17_61. 가장 큰 수 (504p)
# # 난이도 : ★★
# # Leet code Num. : 179
#
# # 항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라
# # 예제 1.
# # 입력 >> [10, 2]
# # 출력 >> "210"
# # 예제 2.
# # 입력 >> [3, 30, 34, 5, 9]
# # 출력 >> "9534330"
#
# def bigg(lst):
#     #입력받은 리스트의 인덱스를 한번씩 입력
#     for a in range(len(lst) - 1):
#         # 입력값을 이용해 내림차순 인덱스를 만든다.
#         wall = len(lst) - 1 - a
#         # 내림차순으로 점차적으로 적어질 range 범위에서 붙어잇는 리스트에서 문자열 합에서 가장 큰값을
#         #  만들기위해 비교하고 바꿔준다.
#         for i in range(wall):
#             if str(lst[i]) + str(lst[i + 1]) < str(lst[i + 1]) + str(lst[i]):
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#     # 0만있으면 0 반환
#     if sum(lst) == 0:
#         return '0'
#     # 정수인 리스트를 문자열로 바꿔준다.
#     b = list(map(str, lst))
#     # 빈칸없애줘서 리턴한다.
#     return ''.join(b)
#
# a = [3, 30, 34, 5, 9]
# print(bigg(a))
#
# #========================================================================================
# class LargerNumKey(str):
#     def __lt__(x, y):
#         return x + y > y + x
#
#
# class Solution:
#     def largestNumber(self, nums):
#         largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
#         return '0' if largest_num[0] == '0' else largest_num
#
# from functools import cmp_to_key
#
# class Solution:
#     def largestNumber(self, nums):
#         def cmp_key(x,y):
#             if x+y > y+x:
#                 return 1
#             elif(x==y):
#                 return 0
#             else:
#                 return -1
#         nums = [str(n) for n in  nums]
#         nums.sort(key = cmp_to_key(cmp_key), reverse = True)
#         return ''.join(nums).lstrip('0') or '0'
#
#
# # Chapter17_61. 가장 큰 수 (504p)
# 난이도 : ★★
# Leet code Num. : 179

# 항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라
# 예제 1.
# 입력 >> [10, 2]
# 출력 >> "210"
# 예제 2.
# 입력 >> [3, 30, 34, 5, 9]
# 출력 >> "9534330"

nums = [3, 30, 300, 3000, 34, 5, 9, 95]

li = list(map(str, nums))
print('1:', li)
# 1: ['3', '30', '300', '3000', '34', '5', '9', '95']

li.sort(reverse = True)
print('2:',li)
# 2: ['95', '9', '5', '34', '3000', '300', '30', '3']
check = li[:]

while True: # Thanks to 선주님, 민수님, 재훈님, 태영님
    for i in range(1, len(li)):
        if (li[i-1] + li[i]) < (li[i] + li[i-1]):
            li[i-1], li[i] = li[i], li[i-1]
            print('3:', li)
    if check == li :
        break
    else:
        check = li[:]

print('4:',li)
# 4: ['9', '95', '5', '34', '3', '30', '300', '3000']

answer = str(int(''.join(map(str, li))))

print(answer)

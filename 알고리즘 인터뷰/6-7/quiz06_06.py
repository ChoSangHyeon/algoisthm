# Chapter06_06. 가장 진 팰린드롬 부분 문자열 (159p)
# 난이도 : ★★
# Leet code Num. : 5

# 가장 긴 팰린드롬 부분 문자열을 출력하라.
# 예제 1.
# 입력 >> "babad"
# 출력 >> "bab" (또는 "aba")
# 예제 2.
# 입력 >> "cbbd"
# 출력 >> "bb"

def longest_pali(input: str):
    def long(left:int,right:int):
        while left>=0 and right <=len(input) and input[left] == input[right-1]:
            left -= 1
            right += 1
        return input[left+1:right-1]
    if len(input) <2 or input == input[::-1]:
        return input
    pali = []
    a = ''
    for char in input:
        pali.append(char.lower())
    for b in range(len(input)-1):
       a = max(a,long(b,b+2),long(b,b+1),key=len)
    return a


# def longest_pali(input: str):
#     if len(input)<2 or input == input[::-1]:
#         return input
#     list = []
#     pali = []
#     k = 0
#     i = 0
#     j = i+1
#     n = i+2
#     for char in input:
#         list.append(char.lower())
#     while k < len(list):
#         try:
#             while j < len(list):
#                 if list[i] == list[j]:
#                     i -= 1
#                     j += 1
#                     if i < 0 or j > len(list)-1:
#                         raise
#                 else:
#                     raise
#             raise
#         except:
#             pali.append(''.join(list[i+1:j]))
#             k += 1
#             i = k
#             j = k +1
#     k = 0
#     i = k
#     while k < len(list):
#         try:
#             while n < len(list)+1:
#                 if list[i] == list[n]:
#                     i -= 1
#                     n += 1
#                     if i < 0 or n > len(list):
#                         raise
#                 else:
#                     raise
#             raise
#         except:
#             pali.append(''.join(list[i+1:n]))
#             k += 1
#             i = k
#             n = k + 2
#     long = []
#     for i in range(len(pali)):
#         long.append(len(pali[i]))
#         a = pali[long.index(max(long))]
#     return a
# if __name__ == "__main__":
#
#     i = 'tommmot'
#     print(longest_pali(i))
#
#
# def long(s: str)->str:
#     def expand(left:int,right:int)->str:
#         while left >= 0 and right <= len(s) and s[left]==s[right-1]:
#             left -= 1
#             right += 1
#         return s[left+1:right-1]
#     result = ''
#     print(range(len(s)-1))
#     i = 0
#     for i in range(len(s)-1):
#         result = max(result,expand(i,i+2),expand(i,i+1),key=len)
#     return result

if __name__ == "__main__":
    print(longest_pali('zxcvbnbvcxzxcvbcxcvbnm,,mnbvccxcvbnbvcxcvbn'))
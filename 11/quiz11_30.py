# Chapter09_30. 중복문자 없는 가장 긴 부분 문자열(303p)
# 난이도 : ★★
# Leet code Num. : 3

# 중복 문자가 없는 가장 긴 부분 문자열 (Substring)의 길이를 리턴하라.
# 예제 1.
# 입력 >> "abcabcbb"
# 출력 >> 3
# 예제 2.
# 입력 >> "bbbbb"
# 출력 >> 1
# 예제 3.
# 입력 >> "pwwkew"
# 출력 >> 3

def sub(s:str):
    used = {}
    max_len = start =0
    for index,char in enumerate(s):
        print(used)
        if char in used and start <= used[char]:
            start = used[char]+1
        else:
            max_len = max(max_len,index - start +1)
        used[char]=index
    return max_len

print(sub("abcabcfbb"))


# def sub(s:str):
#     temp_in = []
#     temp_out = []
#     output = []
#     for i in s:
#         temp_in.append(i)
#     l = 0
#     while l < len(temp_in):
#         for n, g in enumerate(temp_out):
#             if temp_in[l] == g:
#                 output.append(len(temp_out))
#                 l = l - (n +1)
#                 temp_out.clear()
#
#
#         temp_out.append(temp_in[l])
#         print(temp_out)
#         l += 1
#     output.append(len(temp_out))
#     return max(output)
#
#

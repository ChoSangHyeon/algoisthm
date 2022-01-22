# def letterCombinations(input: str):
#     def dfs(deep, stack):
#         # 끝까지 탐색하면 백트래킹
#         if len(stack) == len(input):
#             result.append(stack)
#             return
#
#         # 숫자에 해당하는 모든 문자열 반복
#         for j in dic[input[deep]]:
#             dfs(deep + 1, stack + j)
#         return
#     # 예외 처리
#     if not input:
#         return []
#
#     dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
#            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#     result = []
#     dfs(0, "")
#
#     return result

def letterCombinations(digits):
    if not digits: return []
    letter = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    for digit in digits:
        if not result:
            result = letter[digit]
        else:
            temp = []
            for i in result:
                for j in letter[digit]:
                    temp.append(i + j)
            result = temp
    return result

print(letterCombinations('236'))
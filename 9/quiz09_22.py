# Chapter09_22. 일일 온도 (252p)
# 난이도 : ★★
# Leet code Num. : 739

# 매일의 화씨 온도 (F) 리스트 T를 입력 받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라
# 예제 1.
# 입력 >> T = [73, 74, 75, 71, 69, 72, 76, 73]
# 출력 >>     [1,   1,  4,  2,  1,  1,  0,  0]

def whather(tem:list[int])->list[int]:
    aws = [0]*len(tem)
    stack = []
    for num,f in enumerate(tem):
        while stack and f > tem[stack[-1]]:
            sub = stack.pop()
            aws[sub] = num - sub
        stack.append(num)
    return aws
T = [73, 74, 75, 71, 69, 72, 76, 73]
print(whather(T))
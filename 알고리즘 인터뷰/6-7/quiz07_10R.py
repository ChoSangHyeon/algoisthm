# Chapter07_10. 배열 파티션 1 (190p)
# 난이도 : ★
# Leet code Num. : 561

# n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
# 예제 1.
# 입력 >> [1, 4, 3, 2]
# 출력 >> 4

def party(num : list[int])->int:
    num.sort()
    i = 0
    list_sum = []
    while i < len(num):
        list_sum.append(min(num[i],num[i+1]))
        i += 2
    return sum(list_sum)

a= [1,2,3,4,4,3,3,2,3,4,]
print(party(a))
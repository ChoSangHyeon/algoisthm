# Chapter09_21. 중복 문자 제거 (247p)
# 난이도 : ★★★
# Leet code Num. : 316

# 중복된 문자를 제외하고 사전식 순서 (Lexicographical Order)로 나열하라
# 예제 1.
# 입력 >> "bcabc"
# 출력 >> "abc"
# 예제 2.
# 입력 >> "cbacdcbc"
# 출력 >> "acdb"


a = 'ffiisdjefajhkldfaasdvjlkasdjf'
b = []
c = (''.join(sorted(a)))
for char in c:
    b.append(char)
i = 0
while i < len(b)-1:
    if b[i] == b[i+1]:
        del b[i+1]
        i -= 1
    i +=1
d = (''.join(sorted(b)))
print(d)
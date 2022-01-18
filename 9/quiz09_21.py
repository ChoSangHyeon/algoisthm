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


a = 'cbfafdegecaddecbg'
b = []
c = []
d = []
for char in a:
    b.append(char)
for num,char in enumerate(b):
    j = 0
    while j < len(c):
        if char == b[c[j]]:
            c.pop(j)
        j += 1
    c.append(num)
print(c)
for k in c:
    d.append(b[k])
e = ''.join(d)
print(e)


# last_occur = {c: i for i, c in enumerate(s)}

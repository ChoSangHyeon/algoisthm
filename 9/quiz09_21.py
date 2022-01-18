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
import collections
s = 'ghcdadcbihghhhhgh'
counter,seen,stack = collections.Counter(s),set(),[]
for char in s:
    counter[char] -= 1
    if char in seen:
        continue
    print(stack+['hihi']+[char])
    print(f'seen:{seen}')
    while stack and char < stack[-1] and counter[stack[-1]]>0:
        seen.remove(stack.pop())
    stack.append(char)
    seen.add(char)
print(''.join(stack))


# last_occur = {c: i for i, c in enumerate(s)}

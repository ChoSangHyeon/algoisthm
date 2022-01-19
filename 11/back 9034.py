#테스트 개수
import sys

c=int(input())

def hi(a):
    cnt = 0
    if not a:
        return 'No'
    for o in a:
        if o == '(':
            cnt += 1
        elif o == ')':
            cnt -= 1
        if cnt < 0:
            return 'No'
    if cnt == 0:
        return 'Yes'
    else:
        return 'No'



for i in range(0,c):
    b = sys.stdin.readline()
    print(hi(b))
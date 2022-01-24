import sys

c = int(input())
main = []
# main = [['0','1','1','0','1','0','0'],
# ['0','1','1','0','1','0','1'],
# ['1','1','1','0','1','0','1'],
# ['0','0','0','0','1','1','1'],
# ['0','1','0','0','0','0','0'],
# ['0','1','1','1','1','1','0'],
# ['0','1','1','1','0','0','0']]
for _ in range(c):
    k = list(sys.stdin.readline())
    k.pop()
    main.append(k)
row = len(main)
col = len(main[0])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

house = []
cnt = 0
for a in range(row):
    for b in range(col):
        if main[a][b] == '1':
            cnt += 1
            # cnt1 = gogo(a,b)
            stack = [[a,b]]
            while stack:
                x,y = stack.pop()
                if main[x][y] == '1':
                    house.append(cnt)
                    main[x][y] = '0'
                    for i in range(4):
                        a1 = x + dx[i]
                        b1 = y + dy[i]
                        if a1 < 0 or b1 < 0 or a1 >= row or b1 >= col or main[a1][b1] == '0':
                            continue
                        stack.append([a1,b1])
ans = []
print(cnt)
for i in range(cnt):
    ans.append(house.count(i+1))
ans.sort()
for i in ans:
    print(i)
# Chapter13_32. 섬의 개수 (331p)
# 난이도 : ★★
# Leet code Num. : 200

# 1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을때, 섬의 개수를 계산하라.
# (연결되어 있는 1의 덩어리 개수를 구하라)
# 예제 1.
# 입력 >> 11110
#        11010
#        11000
#        00000
# 출력 >> 1
# 예제 2.
# 입력 >> 11000
#        11000
#        00100
#        00011
# 출력 >> 3

def grid_dfs(input: 'list[list[int]]')->int:
    dx = [0, 0, 1,-1]
    dy = [1,-1, 0, 0]
    row = len(input)
    col = len(input[0])
    cnt = 0
    for a in range(row):
        for b in range(col):
            if input[a][b] == 1:
                cnt +=1
                stack = [[a,b]]
            

                while stack:
                    a1,b1 = stack.pop()
                    input[a1][b1] = 0
                    for i in range(4):
                        x = a1 + dx[i]
                        y = b1 + dy[i]
                        if x < 0 or y < 0 or x >= row or y >= col or input[x][y] == 0:
                            continue
                        stack.append([x,y])

    return cnt

def grid_dfs2(input:'list[list[int]]'):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    row = len(input)
    col = len(input[0])
    cnt = 0

    def ing(x,y):
        if x<0 or y<0 or x >= row or y >= col:
            return
        # print(f'x = {x+1}  y = {y+1}')
        if input[x][y] == 1:
            input[x][y] = 0
            for i in range(4):
                ing(x+dx[i],y+dy[i])
        else:
            return

    for a in range(row):
        for b in range(col):
            if input[a][b] == 1:
                cnt += 1
                ing(a,b)
    return cnt
a = [[1,1,1,1,0],
     [1,1,0,1,0],
     [1,1,0,0,0],
     [0,0,0,0,1]]
print(grid_dfs(a))
print(grid_dfs2(a))













    # Input: grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]
# assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
# assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]
#
#
# def island_dfs_stack(grid):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     rows, cols = len(grid), len(grid[0])
#     cnt = 0
#
#     for row in range(rows):
#         for col in range(cols):
#             if grid[row][col] != '1':
#                 continue
#
#             cnt += 1
#             stack = [(row, col)]
#
#             while stack:
#                 x, y = stack.pop()
#                 grid[x][y] = '0'
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#                     if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
#                         continue
#                     stack.append((nx, ny))
#     return cnt
#
# assert island_dfs_stack(grid=[
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]) == 1
# assert island_dfs_stack(grid=[
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]) == 3
#
#
# def island_dfs_recursive(grid):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     m = len(grid)
#     n = len(grid[0])
#     cnt = 0
#
#     def dfs_recursive(r, c):
#         if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
#             return
#
#         # 방문처리
#         grid[r][c] = '0'
#         for i in range(4):
#             dfs_recursive(r + dx[i], c + dy[i])
#         return
#
#     for r in range(m):
#         for c in range(n):
#             node = grid[r][c]
#             if node != '1':
#                 continue
#
#             cnt += 1
#             dfs_recursive(r, c)
#
#     return cnt
#
# assert island_dfs_recursive(grid=[
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]) == 1
# assert island_dfs_recursive(grid=[
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]) == 3

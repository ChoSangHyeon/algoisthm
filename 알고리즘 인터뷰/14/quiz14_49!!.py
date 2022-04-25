# Chapter14_49. 최소 높이 트리 (416p)
# 난이도 : ★★
# Leet code Num. : 310

# 노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록을 리턴하라
# 예제 1.
# 입력 >> n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 출력 >> [1]
# 예제 2.
# 입력 >> n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 출력 >> [3, 4]
import collections

def long(n,edges):
    if n <= 1:
        return [0]
    dic = collections.defaultdict(list)
    for a,b in edges:
        dic[a].append(b)
        dic[b].append(a)
    res = []
    for i in range(n+1):
        if len(dic[i])==1:
            res.append(i)
    while n > 2:
        n -= len(res)
        new = []
        for leaf in res:
            print(f'dic:{dic}')
            print(f'leaf : {leaf}')
            bibi = dic[leaf].pop()
            print(dic)
            dic[bibi].remove(leaf)

            if len(dic[bibi]) == 1:
                new.append(bibi)
        res = new
    return res

n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(long(n,edges))

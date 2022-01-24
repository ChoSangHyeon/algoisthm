# Chapter12_31. 코스 스케줄 (365p)
# 난이도 : ★★
# Leet code Num. : 207

# 0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0, 1] 쌍으로 표현하는 n개의 코스가 있다.
# 코스 개수 n과 이 쌍들을 입력으로 받았을 때, 모든 코스가 완료 가능한지 판별하라
# 예제 1.
# 입력 >> 2, [[1, 0]]
# 출력 >> true
# 예제 2.
# 입력 >> 2, [[1, 0], [0, 1]]
# 출력 >> false

import collections
from typing import List



def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        visited.add(i)

        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False

    return True
print(canFinish(2,[[1,0],[0,3],[2,3],[2,4],[1,2],[3,4]]))
# import collections
# from typing import List
#
#
# def canFinish( numCourses: int, prerequisites: List[List[int]]) -> bool:
#     graph = collections.defaultdict(list)
#     # 그래프 구성
#     for x, y in prerequisites:
#         graph[x].append(y)
#
#     traced = set()
#     visited = set()
#
#     def dfs(i):
#         # 순환 구조이면 False
#         if i in traced:
#             return False
#         # 이미 방문했던 노드이면 True
#         if i in visited:
#             return True
#
#         traced.add(i)
#         for y in graph[i]:
#             if not dfs(y):
#                 return False
#         # 탐색 종료 후 순환 노드 삭제
#         traced.remove(i)
#         # 탐색 종료 후 방문 노드 추가
#         visited.add(i)
#
#         return True
#
#     # 순환 구조 판별
#     for x in list(graph):
#         if not dfs(x):
#             return False
#
#     return True
# Chapter14_43. 이진 트리의 직경 (390p)
# 난이도 : ★
# Leet code Num. : 543

# 이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라
# 예제 1.
# 입력 >> 1
#        | \
#        2  3
#      / |
#     4  5
# 출력 >> 가장 긴 경로 : 3
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value == None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent
    # root = make_tree_by(lst,0)


def long(lst):
    root = make_tree_by(lst,0)
    res = []
    def dfs(node):
        left = right = 0
        if node.left:
            left = dfs(node.left) +1
        if node.right:
            right = dfs(node.right) +1
        res.append(left+right)
        return max(left,right)

    dfs(root)
    print(res)
    return max(res)


print(long(lst=[3, 9, 20, 4, 6, 15, 7]))
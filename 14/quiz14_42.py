# Chapter14_42. 이진 트리의 최대 깊이 (387p)
# 난이도 : ★
# Leet code Num. : 104

# 이진 트리의 최대 깊이를 구하라
# 예제 1.
# 입력 >> [3, 9, 20, null, null, 15, 7]
# 출력 >> 3
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

def make_lst_by(root):
    if not root:
        return []

    lst = []
    q = deque([root])

    while q:
        node = q.popleft()
        lst.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return lst

def test_max_depth(lst):
    root = make_tree_by(lst, 0)
    if not root:
        return 0

    q = deque([root])
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth

# assert test_max_depth(lst=[]) == 0
assert test_max_depth(lst=[3, 9, 20, None, None, 15, 7]) == 3

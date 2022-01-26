# Chapter14_50. 정렬된 배열의 이진 탐색 트리 변환 (425p)
# 난이도 : ★
# Leet code Num. : 108

# 오름차순으로 정렬된 배열을 높이 군형 (Height Balanced) 이진 탐색 트리로 변환하라
# 예제 1.
# 입력 >>  0
#       |  |
#      -3  9
#       |  |
#      -10  5
# 출력 >> [0, -3, 9, -10, null, 5]
import collections

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(lst):
    if not lst:
        return None

    mid = len(lst) // 2

    node = TreeNode(lst[mid])
    node.left = sorted_array_to_bst(lst[:mid])
    node.right = sorted_array_to_bst(lst[mid + 1:])

    return node


def make_lst_by_bst(root, limit):
    if not root:
        return []

    lst = []
    q = collections.deque([root])

    while q:
        if len(lst) > limit:
            break

        node = q.popleft()
        if node:
            lst.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            lst.append(None)

    return lst

def test_sorted_array_to_bst(lst):
    if not lst:
        return []
    root = sorted_array_to_bst(lst)
    return make_lst_by_bst(root, len(lst))


assert test_sorted_array_to_bst(lst=[-10, -3, 0, 5, 9]) == [0, -3, 9, -10, None, 5]
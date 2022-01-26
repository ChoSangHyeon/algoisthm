# Chapter14_44. 가장 긴 동일 값의 경로  (393p)
# 난이도 : ★
# Leet code Num. : 687

# 동일한 값을 지닌 가장 긴 경로를 찾아라
import collections


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
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


def make_tree(lit,idx):
    main = None
    if idx < len(lit):
        val = lit[idx]
        if val == None:
            return
        main = TreeNode(val)
        main.left = make_tree(lit,2*idx+1)
        main.right = make_tree(lit,2*idx+2)
    return main




def long(lis):
    a = make_tree(lis,0)

    res = []
    if lis is None:
        return 0

    def dfs(node):
        left = right = 0
        if node.left:
            if node.val == node.left.val:
                left = dfs(node.left) + 1
            else:
                left = 0
                dfs(node.left)
        if node.right:
            if node.val == node.right.val:
                right = dfs(node.right) + 1
            else:
                right = 0
                dfs(node.right)
        res.append(left + right)
        return max(left, right)

    dfs(root)
    print(res)
    return max(res)
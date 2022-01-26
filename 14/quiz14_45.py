# Chapter14_45. 이진 트리 반전 (397p)
# 난이도 : ★
# Leet code Num. : 226

# 이진트리 반전
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def reverse(root):
    if root is None:
        return root

    def rev(node):
        if node.left:
            rev(node.left)
        if node.right:
            rev(node.right)
        node.right, node.left = node.left, node.right
        return

    rev(root)
    return root
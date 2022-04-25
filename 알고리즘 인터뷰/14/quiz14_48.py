# Chapter14_48. 균형 이진 트리 (413p)
# 난이도 : ★
# Leet code Num. : 110

# 이진 트리가 높이 균형 (Height-Balanced) 인지 판단하라
# 예제 1.
# 입력 >> [3, 9, null, null, 15, 7]
# 출력 >> true
# 예제 2.
# 입력 >> [1, 2, 2, 3, 3, null, null, 4, 4]
# 출력 >> false

def lenth(tree):
    if tree is None:
        return True
    res = []

    def dfs(node):
        left = right = 0
        if node.left:
            left = dfs(node.left) + 1
        if node.right:
            right = dfs(node.right) + 1
        res.append(abs(left - right))
        return max(left, right)

    dfs(tree)
    print(res)
    if max(res) >= 2:
        a = False
    else:
        a = True
    return a

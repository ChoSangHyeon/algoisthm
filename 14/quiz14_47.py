# Chapter14_47. 이진 트리 직렬화 & 역직렬화 (406p)
# 난이도 : ★★
# Leet code Num. : 297

# 이진 트리를 배열로 직렬화하고, 반대로 역직렬화 하는 기능을 구현하라.
# 즉, 다음과 같은 트리는 [1, 2, 3, null, null, 4, 5] 형태로 직렬화 할 수 있을 것이다
# 예제 1.
# 출력 >>  1
#        / |
#       2  3
#          | \
#          4  5
import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lister(input):
    if input is None:
        return []
    q = collections.deque([input])
    lst = []
    while q:
        node = q.popleft()
        if node:
            lst.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        else:
            lst.append('#')
    return lst

def make_tree(tree, idx):
    main = None
    if idx < len((tree)):
        val = tree[idx]
        if val == None:
            return

        main = TreeNode(val)
        main.left = make_tree(tree, 2 * idx + 1)
        main.right = make_tree(tree, 2 * idx + 2)
    return main


class Codec:

    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    # 역직렬화
    def deserialize(self, data: str) -> TreeNode:
        # 예외 처리
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root

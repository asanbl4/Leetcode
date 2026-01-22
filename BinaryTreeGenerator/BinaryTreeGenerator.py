from jedi.inference.context import TreeContextMixin


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateBinaryTree(arr: list) -> TreeNode:
    if not arr or arr[0] is None:
        return None

    nodes = [None] * len(arr)
    for i, val in enumerate(arr):
        if val is not None:
            nodes[i] = TreeNode(val)

    for i in range(len(arr)):
        if nodes[i] is None:
            continue

        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < len(arr):
            nodes[i].left = nodes[left_i]
        if right_i < len(arr):
            nodes[i].right = nodes[right_i]

    return nodes[0]

if __name__ == '__main__':
    arr = [1, 2, 3, None, 5, None, 7]
    root = generateBinaryTree(arr)
    print(root.val)                 # 1
    print(root.left.val)            # 2
    print(root.left.left)           # None (because arr[3] was None)
    print(root.left.right.val)      # 5

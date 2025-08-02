class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateBinaryTree(arr: list):
    nodes = []
    for i in range(len(arr)):
        node = TreeNode(val=arr[i])
        nodes.append(node)
    nodes.insert(0, None)

    for i in range(1, len(nodes)):
        if 2 * i < len(nodes):
            nodes[i].left = nodes[2 * i]
            nodes[i].right = nodes[2 * i + 1]
        else:
            nodes[i].left = None
            nodes[i].right = None
        # print(nodes[i].val, nodes[i].left.val if nodes[i].left else None, nodes[i].right.val if nodes[i].right else None)
    return nodes[1]

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(generateBinaryTree(arr))
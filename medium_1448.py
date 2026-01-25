from BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, localMax=root.val) -> int:
            count = 0
            if not node:
                return count
            if node.val >= localMax:
                count = 1
            count += dfs(node.left, max(node.val, localMax))
            count += dfs(node.right, max(node.val, localMax))
            return count
        return dfs(root, root.val)

solution = Solution()
root = generateBinaryTree([3,1,4,3,None,1,5])
print(solution.goodNodes(root))
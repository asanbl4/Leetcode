from typing import Optional
from BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        return max(self.maxDepth(left), self.maxDepth(right)) + 1

solution = Solution()
root = generateBinaryTree([3,9,20])
print(solution.maxDepth(root))






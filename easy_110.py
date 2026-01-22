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

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = root.left
        right = root.right
        if abs(self.maxDepth(left) - self.maxDepth(right)) > 1:
            return False
        if self.isBalanced(left) and self.isBalanced(right):
            return True
        return False

solution = Solution()
root = generateBinaryTree([1,2,2,3,3,None,None,4,4])
print(solution.isBalanced(root))






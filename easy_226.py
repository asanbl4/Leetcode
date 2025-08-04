from typing import Optional
from BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

solution = Solution()
print(solution.invertTree(generateBinaryTree([2,1,3])).right.val)

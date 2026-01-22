from typing import Optional

from Leetcode.BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree


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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        leftDepth = self.maxDepth(left) if left else 0
        # print("left depth:", leftDepth)
        rightDepth = self.maxDepth(right) if right else 0
        # print("right depth:", rightDepth)
        return max([
            leftDepth + rightDepth,
            self.diameterOfBinaryTree(left),
            self.diameterOfBinaryTree(right)
        ])

solution = Solution()
root = generateBinaryTree([1,2,3,4,5])
print(solution.diameterOfBinaryTree(root))

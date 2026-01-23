from BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        try:
            if p.val != q.val:
                return False
        except Exception:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

solution = Solution()
p = generateBinaryTree([1,2,1])
q = generateBinaryTree([1,2,1])

print(solution.isSameTree(p, q))
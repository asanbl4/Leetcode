from typing import Optional
from BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree

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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # print(root.val if root else None, subRoot.val)
        if not root:
            return False
        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            if not self.isSameTree(root, subRoot):
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            return True

solution = Solution()
root = generateBinaryTree([1,1])
subRoot = generateBinaryTree([1])
print(solution.isSubtree(root, subRoot))

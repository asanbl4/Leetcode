from typing import Optional
from BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: TreeNode, inorder: list[TreeNode]):
            if not node:
                return None
            dfs(node.left, inorder)
            inorder.append(node)
            dfs(node.right, inorder)
            return [i.val for i in inorder]
        return dfs(root,[])[k - 1]

solution = Solution()
root = generateBinaryTree([5,3,6,2,4,None,None,1])
print(solution.kthSmallest(root,3))


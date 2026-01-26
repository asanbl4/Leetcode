from typing import List, Optional
from BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        rootIdx = inorder.index(root.val)
        leftInorder = inorder[:rootIdx]
        rightInorder = inorder[rootIdx + 1:] # without the root
        leftPreorder = preorder[1:len(leftInorder) + 1]
        rightPreorder = preorder[len(leftInorder) + 1:]
        # print(leftInorder, leftPreorder)
        # print(rightInorder, rightPreorder)
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        return root

solution = Solution()
print(solution.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]).right.right.val)
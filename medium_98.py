from typing import Optional

from BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMin(self, root, minn):
       if not root:
           return minn
       if root.val == minn:
           return False
       return self.findMin(root.left, min(root.val, minn))
    def findMax(self, root, maxx):
        if not root:
            return maxx
        if root.val == maxx:
            return False
        return self.findMax(root.right, max(root.val, maxx))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, ancestor, direction) -> bool:
            if not node:
                return True
            base = (direction == "left" and node.val < ancestor.val) or (
                        direction == "right" and node.val > ancestor.val)
            print("min", self.findMin(node.right, node.val), node.val)
            print("max", self.findMax(node.left, node.val), node.val)
            left = (dfs(node.left, node, direction="left") and self.findMax(node.left, node.val) == node.val)
            right = (dfs(node.right, node, direction="right") and self.findMin(node.right, node.val) == node.val)
            return base and left and right

        print("min", self.findMin(root.right, root.val), root.val)
        print("max", self.findMax(root.left, root.val), root.val)
        return dfs(root.right, root, direction="right") and self.findMax(root.left, root.val) == root.val and \
                dfs(root.left, root, direction="left") and self.findMin(root.right, root.val) == root.val

solution = Solution()
# root = generateBinaryTree([2,1,3])
# root = generateBinaryTree([32,26,47,19,None,None,56,None,27])
# root = generateBinaryTree([5,4,6,None,None,3,7])
# root = generateBinaryTree([3,1,5,0,2,4,6,None,None,None,3])
print(solution.isValidBST(root))
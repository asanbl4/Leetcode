from typing import Optional, List

from libpasteurize.fixes.fix_imports2 import all_modules_subpattern

from BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        ans = []
        if root:
            ans.append([root])
        for level in ans:
            newLevel = []
            for node in level:
                left = node.left
                right = node.right
                newLevel.append(left if left else None)
                newLevel.append(right if right else None)
            normalized = [el for el in newLevel if el]
            if not normalized:
                break
            ans.append(normalized)
        return [[i.val for i in level] for level in ans if level]

solution = Solution()
root = generateBinaryTree([3,9,20,None,None,15,7])
print(solution.levelOrder(root))


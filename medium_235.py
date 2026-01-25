from BinaryTreeGenerator.BinaryTreeGenerator import generateBinaryTree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isDescendant(self, root: TreeNode, target: TreeNode) -> bool:
        if not root:
            return False
        if root.val == target.val:
            return True
        return self.isDescendant(root.left if root.val > target.val else root.right, target)
    def depth(self, root, target, i=1):
        if not root:
            return i
        if root.val == target.val:
            return i + 1
        return self.depth(root.left if root.val > target.val else root.right, target, i + 1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root


root = generateBinaryTree([3,1,4,None,2])
p = TreeNode(2)
q = TreeNode(3)
solution = Solution()
print(solution.lowestCommonAncestor(root, p, q).val)


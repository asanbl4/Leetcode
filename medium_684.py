from typing import List
from collections import deque


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = list(range(len(edges) + 1))  # each node is root of own subtree
        print(root)
        def find_root(node):
            if root[node] != node:
                root[node] = find_root(root[node])
            return root[node]

        for node1, node2 in edges:
            root1, root2 = find_root(node1), find_root(node2)
            print(node1, root1, node2, root2)
            if root1 == root2:
                return [node1, node2]

            root[root2] = root1
            # root[root1] = root2 also works






solution = Solution()
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(solution.findRedundantConnection(edges))

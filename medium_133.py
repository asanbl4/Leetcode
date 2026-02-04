from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def createGraph(adjList) -> Optional[Node]:
    values = []
    nodes = []
    def findOrCreateNode(val) -> Node:
        nonlocal values, nodes
        if val in values:
            idx = values.index(val)
            node = nodes[idx]
        else:
            node = Node(val)
            values.append(val)
            nodes.append(node)
        return node

    for i in range(len(adjList)):
        value = i + 1
        node = findOrCreateNode(value)
        neighbors = adjList[i]
        node.neighbors = list(map(lambda x: findOrCreateNode(x), neighbors))
    return nodes[0] if nodes else None





class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        visited = {}
        valList = []
        nodeList = []
        def bfs(graphNode):
            nonlocal visited, valList, nodeList
            if not graphNode:
                return None

            if graphNode.val in valList:
                idx = valList.index(graphNode.val)
                clonedNode = nodeList[idx]
            else:
                valList.append(graphNode.val)
                clonedNode = Node(graphNode.val)
                nodeList.append(clonedNode)
            for neighbor in reversed(graphNode.neighbors):
                if clonedNode.val not in visited:
                    # print("not in visited", visited, clonedNode.val, neighbor.val)
                    visited[clonedNode.val] = [neighbor.val]
                    clonedNode.neighbors.append(bfs(neighbor))
                else:
                    # print("in visited", visited, clonedNode.val, neighbor.val)
                    if not neighbor.val in visited[clonedNode.val]:
                        visited[clonedNode.val].append(neighbor.val)
                        clonedNode.neighbors.append(bfs(neighbor))
            return clonedNode
        return bfs(node)




solution = Solution()
graphNode = createGraph([[2,4],[1,3],[2,4],[1,3]])



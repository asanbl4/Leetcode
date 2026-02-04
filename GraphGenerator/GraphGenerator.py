class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def generateGraph(adjList: list):
    graph_vals = []
    graph_nodes = []
    for adjacency in adjList:
        if adjacency[0] not in graph_vals:
            node1 = Node(adjacency[0])
            graph_vals.append(adjacency[0])
            graph_nodes.append(node1)
        else:
            idx = graph_vals.index(adjacency[0])
            node1 = graph_nodes[idx]
        if adjacency[1] not in graph_vals:
            node2 = Node(adjacency[1])
            graph_vals.append(adjacency[1])
            graph_nodes.append(node2)
        else:
            idx = graph_vals.index(adjacency[1])
            node2 = graph_nodes[idx]
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)
    return graph_nodes


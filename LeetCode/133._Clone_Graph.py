from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    """
        1. DFS traverse the graph
        2. Create a new node for each node in the graph
        3. Create a dictionary to store the mapping between the old node and the new node
        4. For each node in the graph, add the neighbors to the new node
        5. Return the new node
    """
    def __init__(self):
        self.mapping = {} # new_replicas_of_each_node # we can take a list insted of a dictionary as index referes to the node
        self.visited = [0 for _ in range(101)] # visited[i] = 1 means node i has been visited
    
    def dfs_traverse(self, node: Optional['Node']) -> None:
        if not node or self.visited[node.val]: # if node is None or already visited
            return
        
        self.visited[node.val] = 1

        for each_neighbor in node.neighbors:
            self.dfs_traverse(each_neighbor)
            
        new_neighbors=[
            self.mapping.get(each_neighbor.val) for each_neighbor in node.neighbors
        ]
        new_node = Node(
            val=node.val,
            neighbors=new_neighbors
        )
        self.mapping[node.val] = new_node
            
        return

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: # empty graph
            return Node()
        self.dfs_traverse(node)
        return self.mapping[node.val]

if __name__ == '__main__':
    obj = Solution()
    # adjList = [[2,4],[1,3],[2,4],[1,3]]
    node = Node(1)
    print(obj.cloneGraph(node))
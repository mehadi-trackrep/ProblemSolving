from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        par = [i for i in range(n)] # every one is a parent of itself in initial state
        
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x, y) -> bool: # return True if 2 nodes are already connected.
            px = find(x)
            py = find(y)
            par[px] = py
            return True if px == py else False
        
        extracted_calbles = 0 # it's for tracking the extras that will connect the other clusters
        
        for each_connection in connections:
            if union(each_connection[0], each_connection[1]):
                extracted_calbles += 1
        
        """
            Now, we have to check how many clusters.
            And how many cables are extra.
            As there is a logic of connecting n nodes with n-1 edges at least.
        """
        total_clusters = len(set(find(i) for i in range(n)))
        
        return -1 if extracted_calbles < total_clusters - 1 else total_clusters - 1
    
obj = Solution()
print(
    obj.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]])
    # obj.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]])
    # obj.makeConnected(n = 5, connections = [[0,1],[0,2],[3,4],[2,3]])
)
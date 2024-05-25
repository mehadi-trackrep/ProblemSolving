from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        
        def find(r):
            if par[r] == r:
                return r
            par[r] = find(par[r])
            return par[r]
        
        for each_edge in edges:
            u, v = each_edge[0], each_edge[1]
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return each_edge
            par[pu] = pv
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected[0]) # total nodes; 0 to n-1
        par = [i for i in range(n)] # par[i] = i; initially number of components/groups/sets = n

        def find(r):
            if par[r] == r:
                return r
            par[r] = find(par[r])
            return par[r]
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1: # find & union
                    u = find(i)
                    v = find(j)
                    if u != v:
                        par[u] = v # union
        ans = set()
        for i in range(n):
            par_i = find(i)
            ans.add(par_i)
        
        return len(ans)
        

obj = Solution()
# ans = obj.findCircleNum(isConnected=[[1,1,0],[1,1,0],[0,0,1]])
ans = obj.findCircleNum(isConnected=[[1,0,0],[0,1,0],[0,0,1]])

print(ans)
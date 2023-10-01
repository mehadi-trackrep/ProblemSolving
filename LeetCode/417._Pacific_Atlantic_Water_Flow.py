from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            1. isPacificOcean(): if the (r,c) can go to inside (0,n-1) to (m-1, 0)
            2. isAtlanticOcean()
        '''
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()

        ans = []

        def dfs(r, c, visited, prevHeight):
            if (r,c) in visited or (r<0 or r>=ROWS or c<0 or c>=COLS) \
                or heights[r][c] < prevHeight: return
            visited.add((r,c))

            dfs(r, c+1, visited, heights[r][c]) # right shift
            dfs(r, c-1, visited, heights[r][c]) # left shift
            dfs(r-1, c, visited, heights[r][c]) # upward
            dfs(r+1, c, visited, heights[r][c]) # downward

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        # print(pac, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    ans.append([r,c])

        # print(ans)
        return ans

if __name__ == '__main__':
    obj = Solution()
    assert(obj.pacificAtlantic(
            [[1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]]
        ) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    )
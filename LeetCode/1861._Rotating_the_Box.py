from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ans = []
        
        m, n = len(box), len(box[0])

        for i in range(m): # row wise traverse
            the_row = []
            hash_count = 0
            for j in range(n): # column wise traverse
                if box[i][j] == '#' and j < n-1:
                    the_row.append('.')
                    hash_count += 1
                elif box[i][j] == '*' or j == n-1:
                    # print("--> j, hash_count: ", j, hash_count)
                    tj = j
                    if box[i][j] == '*':
                        the_row.append('*')
                        tj -= 1
                    else:
                        the_row.append('.')
                        if box[i][j] == '#':
                            hash_count += 1
                    while hash_count > 0:
                        the_row[tj] = '#'
                        hash_count -= 1
                        tj -= 1
                else:
                    the_row.append(box[i][j]) # '.'
            ans.append(the_row)
        
        # print("==>ans: ", ans)
        
        ## rotate the box
        ans2 = []
        for i in range(n):
            the_row = []
            for j in range(m):
                the_row.append(ans[j][i])
            ans2.append(the_row[::-1])
        return ans2


if __name__ == "__main__":
    obj = Solution()

    assert obj.rotateTheBox(
        box = [["#",".","#"]]
    ) == [["."],["#"],["#"]]

    assert obj.rotateTheBox(
        box = [
                ["#","#","*",".","*","."], 
                ["#","#","#","*",".","."], 
                ["#","#","#",".","#","."]
            ]
    ) == [
            [".","#","#"],
            [".","#","#"],
            ["#","#","*"],
            ["#","*","."],
            ["#",".","*"],
            ["#",".","."]
        ]
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sz = len(s)
        hash_map = {}
        k = 10
        ans = []
        for i in range(sz - k + 1):
            ss = s[i:i+k]
            if ss in hash_map:
                hash_map[ss] += 1
                if hash_map[ss] == 2:
                    ans.append(ss)
            else:
                hash_map[ss] = 1
        return ans
from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXORs = []
        sofar_xor_val = 0
        
        for val in arr:
            sofar_xor_val ^= val
            prefixXORs.append(sofar_xor_val)
        
        answer = []
        for each_query in queries:
            l, r = each_query[0], each_query[1]
            if l >= 1:
                answer.append(
                    prefixXORs[r] ^ prefixXORs[l-1]
                )
            else:
                answer.append(prefixXORs[r])
        
        return answer
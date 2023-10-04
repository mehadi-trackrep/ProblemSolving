from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_prefix = strs[0]
        for each_str in strs:
            l = len(min_prefix)
            sz = len(each_str)
            i = 0
            while i<sz:
                if i<l and each_str[i] == min_prefix[i]:
                    i += 1
                    continue
                break
            min_prefix = min_prefix[:i]

        return min_prefix
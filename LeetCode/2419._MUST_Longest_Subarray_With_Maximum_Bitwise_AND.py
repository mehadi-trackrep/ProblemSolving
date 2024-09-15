from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        i, j = 0, 0
        ans, ln = 1, len(nums)

        while j < ln:
            if nums[j] != max_num: i = j
            ans = max(ans, j - i + 1)
            j += 1
            
        return ans
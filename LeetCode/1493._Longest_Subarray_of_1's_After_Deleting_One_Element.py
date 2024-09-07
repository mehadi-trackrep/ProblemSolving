from typing import List

class Solution:
    """
        Using template 1: shrinkable approach
    """
    def longestSubarray(self, nums: List[int]) -> int:
        i, j = 0, 0
        cnt, ans = 0, 0 # cnt means number of zeros.
        ln = len(nums)
        
        for _ in range(ln):
            cnt += 1 if nums[j] == 0 else 0
            
            while cnt > 1:
                cnt -= 1 if nums[i] == 0 else 0
                i += 1
                
            ans = max(ans, (j - i))  ## note that the window is of size `j - i + 1`. We use `j - i` here because we need to delete a number.
            
            j += 1
        
        return ans
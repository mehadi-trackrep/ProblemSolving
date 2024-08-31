from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        ans = 1
        psum = 0
        ln = len(nums)
        
        nums.sort()
        
        for _ in range(ln):
            psum += nums[j] # cumulative sum
            # if the window is invalid then make it valid again by shifting i pointer [while loop]
            while ((j - i + 1) * nums[j] - psum) > k:
                psum -= nums[i]
                i += 1
            ans = max(ans, (j - i + 1))
            j += 1
        
        return ans
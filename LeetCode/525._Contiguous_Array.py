from typing import List

class Solution:
    """
        Here, we use same logic of `finding the longest substring containing vowels
        in even counts` but excluding the bitmasking.
        We can do that no need here instead we can use prefixSum strategy by not only
        adding value also subtracting cause, we have to track the "count".
        
        V.V.I. MUST ref ==> https://leetcode.com/problems/contiguous-array/solutions/4881359/easy-explanation-hashmap-beats-93-29-c-java-python3-kotlin/ 
    """
    def findMaxLength(self, nums: List[int]) -> int:
        ln = len(nums)
        sum_sofar = 0
        max_len = float('-inf')
        mp = {}
        
        for i in range(ln):
            sum_sofar += 1 if nums[i] == 1 else -1
            
            if sum_sofar == 0: # the valid window started from 0th index
                max_len = i + 1
            elif sum_sofar in mp: # this sum already found earlier, so, earlier index to current index is a valid window
                max_len = max(max_len, i - mp[sum_sofar])
            else:
                mp[sum_sofar] = i # track first time occurance of the prefix sum / so far sum

        return max_len
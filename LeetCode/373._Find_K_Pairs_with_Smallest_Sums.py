from typing import List
from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        
        for num in nums1:
            heappush(pq, (num + nums2[0], 0)) # sum & which index of nums2 taken
        
        len_nums2 = len(nums2)
        ans = []
        
        while k and pq:
            top = heappop(pq)
            
            s, nums2_pos = top[0], top[1]
            ans.append([s - nums2[nums2_pos], nums2[nums2_pos]]) # s - nums2[nums2_pos] == nums1
            
            if nums2_pos + 1 < len_nums2:
                heappush(
                    pq,
                    (
                        s - nums2[nums2_pos] + nums2[nums2_pos+1],
                        nums2_pos + 1
                    )
                )
            
            k -= 1
        
        return ans
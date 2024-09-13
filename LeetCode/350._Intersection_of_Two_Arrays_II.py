from typing import List



class Solution1:
    # Using Hashing.. 
    # T.C.: O(MAX) , MAX = 1001
    # Auxiliary space: O(MAX)
    

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = [0] * 1001
        freq2 = [0] * 1001

        for num in nums1:
            freq1[num] += 1
        for num in nums2:
            freq2[num] += 1
        
        ans = []

        for i in range(1001):
            mn = min(freq1[i], freq2[i])
            if mn:
                ans.extend([i] * mn)
            
        return ans

class Solution:
    # Using Two Pointers.. 
    # T.C.: O(nlogn) for using sort.
    # Auxiliary space: O(1)

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()
        
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return ans
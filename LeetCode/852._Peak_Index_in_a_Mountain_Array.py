from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def binary_search(l, h) -> int: # return position/index
            if h >= l:
                m = (l + h) // 2
                if arr[m-1] < arr[m] > arr[m+1]:
                    return m
                elif arr[m-1] < arr[m] < arr[m+1]: # down slope section to left, so search in right
                    return binary_search(m+1, h)
                else: # down slope section to right, so search in left
                    return binary_search(l, m-1)
            else: # if m (mid) will be 2 then l to m-1 ==> 0 to 1, and always there will be a solution, so 1 will be the answer.
                return 1
            
        return binary_search(0, len(arr)-1)



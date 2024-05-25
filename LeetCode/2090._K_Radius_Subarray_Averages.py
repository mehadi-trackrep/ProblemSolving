from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        """
            1. We will have three pointers.
                start, center, end.
                output = []
            2. first window calculation: [0 -> k -> 2*k]
            3. # filling -1 for the first centers
                    for idx in range(0, k):
                        ...
            4. iterate it till end < sz # calculate avg (integer division); 
            5. # filling -1 for the last centers
                for idx in range(sz-k, sz):
                    ...
        """
        # 1)
        output = []
        sz = len(nums)
        window_start = 0
        window_center = k
        window_end = 2*k
        dividend = 2*k + 1

        # 2)
        i = s = 0
        while 2*k < sz and i <= 2*k: # 1st window calculation
            s += nums[i]          
            i += 1
            
        # 3)
        for idx in range(0, k):
            if idx >= sz: break
            output.append(-1)

        # 4)
        while window_end < sz:
            output.append(s // dividend)
            window_end += 1
            if window_end >= sz: break
            s = s - nums[window_start] + nums[window_end]
            window_start += 1
            window_center += 1
        
        # 5)
        for _ in range(window_center, sz):
            output.append(-1)
        
        return output

obj = Solution()
obj.getAverages(nums=[8], k=1000)
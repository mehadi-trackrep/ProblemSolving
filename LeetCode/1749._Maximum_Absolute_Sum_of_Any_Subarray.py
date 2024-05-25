from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currentIndexSum = overallMaximumSum = 0
        for num in nums:
            print("--> currentIndexSum: ", currentIndexSum)
            a = num
            b = currentIndexSum + num
            if a < 0 and b < 0:
                currentIndexSum = min(a, b)
            else:
                if a > 0:
                    if abs(b) >= a:
                        currentIndexSum = b
                    else:
                        currentIndexSum = a
                else:
                    if abs(a) >= b:
                        currentIndexSum = a
                    else:
                        currentIndexSum = b
            overallMaximumSum = max(overallMaximumSum, abs(currentIndexSum))
        return overallMaximumSum


obj = Solution()
# obj.maxAbsoluteSum([1,-3,2,3,-4])
# print("====================================")
obj.maxAbsoluteSum([2,-5,1,-4,3,-2])
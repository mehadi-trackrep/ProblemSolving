from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        sz = len(height)
        mx_area = 0
        l, r = 0, sz-1

        while l<r:
            mx_area = max(
                 mx_area
                ,(r - l) * ( min(height[l], height[r]) )
            )
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                l += 1
                r -= 1

        return mx_area

if __name__ == "__main__":
    obj = Solution()
    assert obj.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert obj.maxArea([1,1]) == 1
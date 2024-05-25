from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sz = len(nums)
        l, r = 0, sz-1
        for idx in range(sz):
            if nums[idx] != val:
                l += 1
            else:
                if nums[r] != val:  # swap
                    nums[l] = nums[r]
                    nums[r] = '_'
                    l += 1
                else:  # just replace with right pointer
                    nums[r] = '_'
                    r -= 1
        print(nums)
        return sz-r


if __name__=="__main__":
    obj = Solution()
    # obj.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
    obj.removeElement(nums = [3, 2, 2, 3], val = 3)
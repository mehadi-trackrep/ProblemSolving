from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:  # it's the same concept of Linked List Cycle II (2 times loop, 1x-2x speed, 1x-1x speed)
        sz = len(nums)
        slow = fast = nums[0]
        while True:
            slow = nums[slow]  # 1 step
            fast = nums[nums[fast]]  # 2 steps
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]  # 1 step
            fast = nums[fast]  # 1 step
        return fast

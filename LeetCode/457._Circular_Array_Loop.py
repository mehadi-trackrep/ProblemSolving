from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        sz = len(nums)
        for i in range(sz):
            slow, fast = i, i
            is_forward_direction = nums[slow] > 0 # True / False
            while True:
                # Shifting slow pointer 1 step based on index value criteria
                slow = self.next_step(slow, nums[slow], sz)
                if self.if_not_cycle(slow, is_forward_direction, nums, sz):
                    break

                # Shifting fast pointer 2 steps based on index value criteria
                fast = self.next_step(fast, nums[fast], sz)
                if self.if_not_cycle(fast, is_forward_direction, nums, sz):
                    break
                fast = self.next_step(fast, nums[fast], sz)
                if self.if_not_cycle(fast, is_forward_direction, nums, sz):
                    break
                if slow == fast:
                    return True
        return False

    def next_step(self, current_pointer, current_pointer_value, array_size) -> int:
        next_pointer = (current_pointer + current_pointer_value) % array_size
        if next_pointer < 0:
            next_pointer += array_size
        return next_pointer

    def if_not_cycle(self, current_pointer, prev_direction, array, array_size) -> bool:
        current_direction = array[current_pointer] > 0
        if (current_direction != prev_direction) or (abs(array[current_pointer]) % array_size):
            return True # not a cycle
        return False


obj = Solution()
print(obj.circularArrayLoop([-2, -3, -9]))
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_arr = []
        s = 0
        for num in nums:
            s += num # inclusive
            self.prefix_sum_arr.append(s)

    def sumRange(self, left: int, right: int) -> int:
        left_val = self.prefix_sum_arr[0] if left == 0 else (self.prefix_sum_arr[left] - self.prefix_sum_arr[left-1])
        return self.prefix_sum_arr[right] - self.prefix_sum_arr[left] + left_val

if __name__ == '__main__':
    obj = NumArray(
        nums=[-2, 0, 3, -5, 2, -1]
    )
    assert obj.sumRange(0, 2) == 1
    assert obj.sumRange(2, 5) == -1
    assert obj.sumRange(0, 5) == -3
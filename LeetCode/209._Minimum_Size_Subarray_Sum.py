from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, counter = 0, 0, 1 # counter 1 means still this window is towards valid but 0 means it's now a  invalid window.
        so_far_sum, sz = 0, len(nums)
        min_window_length = sz + 1

        print("==> nums: {}".format(nums))
        
        while end < sz:
            so_far_sum += nums[end]

            if so_far_sum >= target:
                counter = 0

            while counter == 0:
                print("--> start: {}, end: {}".format(start, end))
                min_window_length = min(min_window_length, end - start + 1)
                
                so_far_sum -= nums[start]
                if so_far_sum < target:
                    counter = 1

                start += 1

            end += 1

        return min_window_length if min_window_length != sz + 1 else 0

if __name__ == '__main__':
    obj = Solution()
    assert obj.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
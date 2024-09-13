
class Solution:
    """
        Hacks:-
            if we have contiguous subarray like [4, 5, 6, 8]
            then we can get total 4 * (4+1) / 2 = 10 different subarrays from it.
                4 * (4+1) / 2 == 1 + 2 + 3 + 4
            Where either all are correct or some might be incorrect.
            We can easily exclude the incorrect subarrys from result/ans.
            
            Formula: 
                total_subarray_count_with_bound(right) - total_subarray_count_with_bound(left - 1)
    """
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        def total_subarray_count_with_bound(boundary) -> int:
            ans, cnt = 0, 0
            for num in nums:
                if num <= boundary:
                    cnt += 1
                    ans += cnt
                else:
                    cnt = 0
            return ans

        return total_subarray_count_with_bound(right) - total_subarray_count_with_bound(left - 1)
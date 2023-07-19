class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        # print("nums   : {}".format(nums))
        # print("indices: {}\nk: {}\n".format([idx for idx in range(len(nums))], k))

        for right in range(len(nums)):
            curr *= nums[right]
            # print("curr: {}, right: {}".format(curr, right))
            while curr >= k:
                curr //= nums[left]
                left += 1
                # print("--> curr: {}, left: {}".format(curr, left))
            """
Approach:-
    Key idea: Whenever you see a problem asking for the number of subarrays, 
    think of this: at each index, how many valid subarrays end at this index? 
    Let's split the 8 subarrays by their ending indices:

    [10]
    [5], [10, 5]
    [2], [5, 2]
    [6], [2, 6], [5, 2, 6]
Do you notice a pattern? For each index, the number of subarrays ending at 
that index is the length of the window after reaching that index. For any 
given ending index right, a subarray could start at any index between 
left and right, which is a total of right - left + 1 (the window size) 
starting indices.

V.V.I. ==> We calculate the total subarrays in a window when 
            3 the curr product will be < k (after while loop) so that the
            left and right index will be adjusted!!
            For example: 
                k = 19
                [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3]
                ----------------------------------------------
                Iterations:-
                Step-1: [10]; left = 0, right = 0; curr = 10 (YES)
                Step-2: [10, 9]; left=0, right=1; curr = 90 (NO) --> run the while loop for getting curr < k condition meet,
                                 because we have to get the right window which elements product < k
                                 and then the left, right indices will be adjusted (respect the conditions)
                        So, after while loop, the curr = 9; left=1, right=1
                        then we get the subarray --> [9] (YES) --> ans += 1
                        => ans += (right - left + 1)
                Step-3:
                        [9, 10]; left=1, right=2; curr = 90 (NO)
                            after while loop --> curr = 10; left=2, right=2
                            [10] (YES)
                Step-4: [10, 4]
                ...
            """

            ans += right - left + 1

        return ans


if __name__ == '__main__':  ## subarray --> window (so, sliding window technique)
    obj = Solution()
    ans = obj.numSubarrayProductLessThanK(
        nums=[10,5,2,6],
        k=100
    )
    print("ans: ", ans)

    ans = obj.numSubarrayProductLessThanK(
        nums=[1,2,3],
        k=0
    )
    print("ans: ", ans)
    ans = obj.numSubarrayProductLessThanK(
        nums=[10,9,10,4,3,8,3,3,6,2,10,10,9,3],
        k=19
    )
    print("ans: ", ans)
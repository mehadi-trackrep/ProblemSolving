class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:



if __name__ == '__main__':  ## subarray --> window (so, sliding window technique)
    obj = Solution()
    ans = obj.numSubarrayProductLessThanK(
        nums=[1,1,1],
        k=2
    )
    print("ans: ", ans)

    ans = obj.numSubarrayProductLessThanK(
        nums=[1,2,3],
        k=3
    )
    print("ans: ", ans)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int: ## Kadane's Algorithm
        currentIndexSum = overallMaxSum = nums[0]
        sz = len(nums)
        for idx in range(1, sz):
            currentIndexSum = max(nums[idx], nums[idx]+currentIndexSum)
            overallMaxSum = max(overallMaxSum, currentIndexSum)
        return overallMaxSum

if __name__ == '__main__':
    obj = Solution()
    nums = [-2, -4, 5, 4, -1, 7, 8]
    print(obj.maxSubArray(nums))

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sz = len(nums)
        new_index = 1
        for i in range(1, sz): # i == r (fast runner)
            if nums[i-1] != nums[i]:
                nums[new_index] = nums[i] # new_index == l (slow runner)
                new_index += 1
        return new_index

        
if __name__ == '__main__':
    obj = Solution()
    ans = obj.removeDuplicates(
        nums=[0,0,1,1,1,2,2,3,3,4]
    )
    print(ans)
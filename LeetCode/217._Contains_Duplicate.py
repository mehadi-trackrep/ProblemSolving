class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ans = False
        nums.sort()
        sz = len(nums)
        for idx in range(1, sz):
            if nums[idx] == nums[idx-1]:
                ans = True
        return ans

        ''' Approach 2:-
            if len(set(nums)) == len(nums):
                return False
            else:
                return True
        '''

if __name__ == '__main__':
    obj = Solution()
    nums = [4,2,3,1]
    print(obj.containsDuplicate(nums))

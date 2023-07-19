class Solution: ## O(n)
    def canJump(self, nums: list[int]) -> bool:
        sofar_mx_jump_index = 0
        sz = len(nums)
        if sz == 1:
            return True
        for idx in range(sz-1):
            if nums[idx] == 0:
                if sofar_mx_jump_index <= idx:
                    return False
            sofar_mx_jump_index = max(sofar_mx_jump_index, (idx + nums[idx]))
        return True if sofar_mx_jump_index >= sz-1 else False

class Solution1: ## O(n)
    def canJump(self, nums: list[int]) -> bool:
        sz = len(nums)
        sofar_max_jump_index = 0
        for idx in range(sz):
            if sofar_max_jump_index < idx: # it means that we couldn't reach this current index (idx) so, we don't need to check the later indices!!
                return False
            sofar_max_jump_index = max(sofar_max_jump_index, idx+nums[idx])
        return True

if __name__ == '__main__':
    obj = Solution()
    nums = [2,3,1,1,4]
    # nums = [3,2,1,0,4]
    # nums = [3,3,1,0,2,0,1]
    # nums = [3,3,1,0,1,0,1]
    nums = [0]
    nums = [0,2,3] # False
    nums = [3,1,1,0,2,3] # False
    # nums = [3,1,2,0,2,3] # True
    print(obj.canJump(nums))
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        lefts = []
        rights = []
        sz = len(nums)
        product = 1
        for i in range(sz):
            lefts.append(product)
            product *= nums[i]
        
        product = 1
        for i in range(sz):
            rights.append(product)
            product *= nums[sz-i-1]
        
        rights.reverse()
        for i in range(sz):
            nums[i] = lefts[i] * rights[i]
        
        return nums

if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2, 3, 4]
    nums = [-1,1,0,-3,3]
    print(obj.productExceptSelf(nums))
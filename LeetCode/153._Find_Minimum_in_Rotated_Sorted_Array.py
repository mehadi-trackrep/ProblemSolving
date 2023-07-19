import math

def binary_search(nums: list) -> int:
    sz = len(nums)
    left = 0
    right = sz-1

    cnt = 0

    while left < right:
        mid = int((left + right)/2)
        if mid+1 < sz:
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
        if mid-1 > 0:
            if nums[mid] < nums[mid-1]:
                return nums[mid]
        ### TEST started
        # print("left: {}, right: {}, mid: {}".format(left, right, mid))
        # cnt += 1
        # if cnt == 10:
        #     break
        ### TEST ended
        if nums[mid] < nums[right]: # if it's in a sorted segment then search in backward segment..
            right = mid
        if nums[mid] > nums[right]: # if it's not in a sorted segment then search in forward segment..
            left = mid
    return nums[0]

class Solution:
    def findMin(self, nums: list[int]) -> int:
        return binary_search(nums)

if __name__ == '__main__':
    obj = Solution()
    nums = [6,7,0,1,2,4,5]
    nums = [4,5,6,7,0,1,2]
    nums = [11,13,15,17]
    nums = [2,1]
    print(obj.findMin(nums))
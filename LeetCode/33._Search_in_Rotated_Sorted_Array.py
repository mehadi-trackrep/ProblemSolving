class Solution_1: ## TC: O(3*logn)
    def binary_search_for_min_value_index(self, nums) -> int:
        sz = len(nums)
        lh = 0
        rh = sz-1
        mid = None
        while lh < rh:
            mid = (lh + rh) // 2
            print("--> lh: {}, rh: {}, mid: {}".format(lh, rh, mid))
            if mid+1 < sz and nums[mid] > nums[mid+1]:
                return mid+1
            if mid-1 > 0 and nums[mid] < nums[mid-1]:
                return mid
            if nums[mid] > nums[rh]:
                lh = mid
            if nums[mid] < nums[rh]:
                rh = mid
        return 0
    def binary_search_for_value_x(self, nums, lh, rh, target) -> int:
        mid = None
        while lh <= rh:
            mid = (lh + rh) // 2
            print("==> lh: {}, rh: {}, mid: {}".format(lh, rh, mid))
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                rh = mid-1
            if nums[mid] < target:
                lh = mid+1
        return -1
    def search(self, nums: list[int], target: int) -> int:
        min_value_index = self.binary_search_for_min_value_index(nums)
        print("--> min_value_index: ", min_value_index)
        result_from_lh_window = self.binary_search_for_value_x(nums, 0, min_value_index-1, target)
        print("--> result_from_lh_window: ", result_from_lh_window)
        result_from_rh_window = self.binary_search_for_value_x(nums, min_value_index, len(nums)-1, target)
        print("--> result_from_rh_window: ", result_from_rh_window)
        if result_from_lh_window == -1:
            return result_from_rh_window
        if result_from_rh_window == -1:
            return result_from_lh_window

class Solution: ## TC: O(logn)
    def binary_search(self, nums, target) -> int:
        lh = 0
        rh = len(nums) - 1
        while lh <= rh:
            mid = (lh+rh) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[lh]: ## thinking about [left to mid] unrotated segment
                if target < nums[mid] and target >= nums[lh]:
                    rh = mid-1
                else:
                    lh = mid+1
            else: ## [left to mid] is not a ascending segment (here, the minimum value exists)
                ## and the mid value exists in the last sorted segment
                if target > nums[mid] and target <= nums[rh]:
                    lh = mid+1
                else:
                    rh = mid-1
        return -1
    '''
        If the nums[] is rotated then it will have two sorted segments!!
        Otherwise itself a single sorted array only. :) 
    '''
    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target)


if __name__ == '__main__':
    obj = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    # nums = [1]
    # target = 0
    # nums = [5,1,3]
    # target = 5
    print(obj.search(nums, target))
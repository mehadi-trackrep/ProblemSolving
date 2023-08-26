class Solution: #O(n) or O(nlogn)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k ## V.V.I. ==> reassigned k to track the index of the kth largest element in the sorted array, as we will compare index to index!!

        def quickSelect(l, r): # two pointers -> left & right == l, r
            ## STEP 1:- PARTITIONING
            pivot, pivot_idx_pointer = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot: ## less or equal items should be shifted to left side segment
                    nums[i], nums[pivot_idx_pointer] = nums[pivot_idx_pointer], nums[i]
                    pivot_idx_pointer += 1
            nums[pivot_idx_pointer], nums[r] = nums[r], nums[pivot_idx_pointer] ## here pivot == nums[r]

            ## STEP 2:- RECURSIVE CALLS
            if pivot_idx_pointer > k: # then have to search in left side segment
                return quickSelect(l, pivot_idx_pointer-1)
            elif pivot_idx_pointer < k: # then have to search in right side segment
                return quickSelect(pivot_idx_pointer+1, r)
            else:
                return nums[pivot_idx_pointer]
        
        return quickSelect(0, len(nums)-1)

class Solution1: #O(n) using 'counting'

    def findKthLargest(self, nums: list[int], k: int) -> int:
        offset = 10000
        nums = [num + offset for num in nums] ## shifted all nums in positive range
        mx = max(nums) # then find the maximum number
        freq = [0] * (mx + 1)

        for num in nums:
            freq[num] += 1

        for num in range(mx, -1, -1):
            cnt = freq[num]
            if k-cnt <= 0:
                ans = num - offset
                break
            elif k-cnt > 0:
                k -= cnt

        return ans

if __name__=='__main__':
    arr = [3,2,1,5,6,4]
    while True:
        k = int(input("Enter the value of k: "))
        # obj = Solution()
        obj = Solution1()
        print(obj.findKthLargest(arr, k))
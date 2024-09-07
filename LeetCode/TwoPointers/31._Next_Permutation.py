from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
The steps are the following:

Find the break-point, i: Break-point means the first index i from the back of the given array where arr[i] becomes smaller than arr[i+1].
For example, if the given array is {2,1,5,4,3,0,0}, the break-point will be index 1(0-based indexing). Here from the back of the array, index 1 is the first index where arr[1] i.e. 1 is smaller than arr[i+1] i.e. 5.
To find the break-point, using a loop we will traverse the array backward and store the index i where arr[i] is less than the value at index (i+1) i.e. arr[i+1].
If such a break-point does not exist i.e. if the array is sorted in decreasing order, the given permutation is the last one in the sorted order of all possible permutations. So, the next permutation must be the first i.e. the permutation in increasing order.
So, in this case, we will reverse the whole array and will return it as our answer.
If a break-point exists:
Find the smallest number i.e. > arr[i] and in the right half of index i(i.e. from index i+1 to n-1) and swap it with arr[i].
Reverse the entire right half(i.e. from index i+1 to n-1) of index i. And finally, return the array.        
        
        """
        ln = len(nums)
        pivot_index = -1 # break-point
        
        for j in range(ln-2, -1, -1):
            if nums[j] < nums[j+1]: # got it
                pivot_index = j
                break
        
        if pivot_index == -1:
            return nums.sort()
        
        min_max, min_max_idx = 500, -1
        for i in range(pivot_index+1, ln):
            if nums[i] > nums[pivot_index]:
                if nums[i] < min_max:
                    min_max = nums[i]
                    min_max_idx = i
        
        # swap
        t = nums[pivot_index]
        nums[pivot_index] = nums[min_max_idx]
        nums[min_max_idx] = t
        
        nums[pivot_index+1:] = sorted(nums[pivot_index+1:])
        
        return nums
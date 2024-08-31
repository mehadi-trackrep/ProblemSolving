from typing import List

class Solution:
    """
        It's like prefixSum but here we don't store the prefix sums into any array.
        Instead of it, we just move forward by adding the current element into a variable like sum.
            - sum += nums[i]
        * We will use the math "modulus" - reminder trick.
            Suppose, input array: [23, 2, 4, 7] & k = 6
            So, 
                0th index prefix sum = 23 --> 23 % 6 = 5
                1th index prefix sum = 25 --> 25 % 6 = 1
                2th index prefix sum = 29 --> 29 % 6 = 5
                    STOP!
                    
                    Let's see here that we get the reminders 5, 1, 5 at 0th, 1th and 3th indices.
                    Now, the reminder 5 repeated (already exist in a hashmap).
                    That means, in the subarray there is an another subarray whose sum is divisible by k -> sum / k = 0
                    
                    Cause, we can write this:- 
                        (sum1 + sum2) % k = sum1 % k + sum2 % k
                        here,   sum1 = 23        --> 23 % 6 = 5
                                sum2 = 2 + 4 = 6 --> 6 % 6 = 0
                        so, 5 + 0 = 5 that repeated at 2th index. :D
                        
                3th index prefix sum = ... (no need to go this step, we will get the result in the previous step)

        Anyway, we have to store the index. It's for identifying how many elements there in the subarray.
        Cause, the subarray length here should be >= 2.
        
        ** 
        [[ 0 is always a multiple of k. ]]
            corner case1: if the first element is divisible by k, then we the hashmap entry will be {0: 0} [0 reminder: 0th index]
                        That's why we have to keep an initial entry {0: -1} [0 reminder: -1th index]
                        So that we can compare like 0 - (-1) = 1 means this subarray has a single element. 
        
            corner case2: if we have contiguous 0s like [5, 0, 0, 0] & k = 3
                        answer - True
                        Here, we have to keep the first reminder 0; we should not override here
                        at interation 3 we have the hashmap like 
                                {
                                    5%3 : 0 (2 : 0),
                                    0%3 : 1 (0 : 1)
                                }

        N.B. During iteration, if we get the current reminder already exist in hashmap but the subarray length is 1.
            That means this subarray is invalid for this particular problem.
            So, we do not override the hashmap entry.
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: -1} # key = reminder : value = index
        psum = 0
        idx = -1
        
        for num in nums:
            idx += 1
            psum += num
            r = psum % k # current state reminder
            if r not in hashmap:
                hashmap[r] = idx
            elif idx - hashmap[r] > 1:
                return True
            else: # if idx - hashmap[r] == 1
                pass # don't update the 

        return False
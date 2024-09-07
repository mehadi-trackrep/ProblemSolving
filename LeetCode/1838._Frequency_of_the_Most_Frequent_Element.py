from typing import List

class Solution:
    """
        Template-1: Sliding Window (Shrinkable)
    """
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        ans = 1
        psum = 0
        ln = len(nums)
        
        nums.sort()
        
        for _ in range(ln):
            psum += nums[j] # cumulative sum
            # if the window is invalid then make it valid again by shifting i pointer [while loop]
            while ((j - i + 1) * nums[j] - psum) > k:
                psum -= nums[i]
                i += 1
            ans = max(ans, (j - i + 1))
            j += 1
        
        return ans

class Solution1:
    """
        Template-2: Sliding Window (Non-shrinkable)
        For this problem, both of the approaches will work.
        Cause we need the "Maximum".
        ** If we need the minimum then we need to use the shrinkable approach - inner while loop.
            
            
            ## N.B. 
                1) for getting MAX, the condition is after the while loop / invalid checking point
                2) for getting MIN, the condition is in the while loop / invalid checking point
                
            Suppose input array = [1, 1, 1, 39997, 5, 10] & k = 6 --> output: 3 [1, 1, 1]
            
            state 1: sum = 1 [1 <= 6] - valid ;;            num = 1 (index - 0)     ==> i = 0; j = 0; ans = 1
            state 2: sum = 2 [2 <= 6] - valid ;;            num = 1 (index - 1)     ==> i = 0; j = 1; ans = 2
            state 3: sum = 3 [3 <= 6] - valid ;;            num = 1 (index - 2)     ==> i = 0; j = 2; ans = 3
                - state 3 is valid because:
                            (j-i+1)*arr[j] - sum (this means that total number of operations done to make all the elements equal to arr[j])
                        =   (2+1)*1 - 3 = 0 <= 6 (0 operations used! :D still left 6)
            state 4: sum = 40000 [40000 > 6] - invalid ;;   num = 39997 (index - 3) ==> i = 1; j = 3; ans = 3
            state 5: sum = 40005 [40005 > 6] - invalid ;;   num = 5 (index - 4)     ==> i = 2; j = 4; ans = 3
            state 6: sum = 40015 [40015 > 6] - invalid ;;   num = 10 (index - 5)    ==> i = 3; j = 5; ans = 3
                here, states 4 to 5, the ith pointer moves in every step that's why j - i + 1 keeps same, at least not increased as we need MAX, so if
                it gets increased then the answer might be wrong. :)
                
        ```
            int i = 0, j = 0;
            for (; j < N; ++j) {
                // CODE: use A[j] to update state which might make the window invalid
                if (invalid()) { // Increment the left edge ONLY when the window is invalid. In this way, the window GROWs when it's valid, 
                                    // and SHIFTs forward one times when it's invalid
                    // CODE: update state using A[i]
                    ++i;
                }
                // after `++j` in the for loop, this window `[i, j)` of length `j - i` MIGHT be valid.
            }
            return j - i; // There must be a maximum window of size `j - i`.
        ```
        
        V..V..I
            #   Why is (j - i + 1) * A[j] - sum <= k valid?
                (j - i + 1) is the length of the window [i, j]. We want to increase all the numbers in the 
                window to equal A[j], the number of operations needed is (j - i + 1) * A[j] - sum which should be <= k. 
                For example, assume the window is [1,2,3], increasing all the numbers to 3 will take 3 * 3 - (1 + 2 + 3) 
                operations.
    """
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        ans = 1
        psum = 0
        ln = len(nums)
        
        nums.sort()
        
        for _ in range(ln):
            psum += nums[j] # cumulative sum
            # if the window is invalid then make it valid again by shifting i pointer [while loop]
            if ((j - i + 1) * nums[j] - psum) > k:
                psum -= nums[i]
                i += 1
            j += 1
        
        return j - i
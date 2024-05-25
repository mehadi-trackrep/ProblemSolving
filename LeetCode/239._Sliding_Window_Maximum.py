from typing import List


class Solution:
    def cleanup_less_and_out_of_window_values_from_input_list(
            self, current_window_top_indices, nums, current_index
    ):
        # here, we will remove the lower values from last of the list
        # intuition: কোন কিউ এর শেষ থেকে যদি কোন কিছুর ছোট বা সমান সব গুলা বাদ দিতে দিতে কিউ এর প্রথমে যেতে থাকি তাহলে কিউ এর
        #   0th index এ যে থাকবে সেই সব থেকে বড় হবে এদের মধ্যে।
        # চাইলে উল্টাটাও করা যাবে। কিন্তু উপরেরটাতে আমরা সব সময় জানবো যে, 0th index এই সব থেক বড় টা থাকবে।
        while current_window_top_indices and nums[current_window_top_indices[-1]] <= nums[current_index]:
            _ = current_window_top_indices.pop()

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            Approach:-
                    ** w == k (here)
                Use an extra array (deque) for keeping tack of current window top indices (max) and
                next possible maximums for next windows, where the first element will be always maximum
                if the length of this array > the window length then have to remove the first index
                & if the values also less than the current pointer value then also remove/delete those.
                It will have T.C - O(n*w) in worst case, avg.case - O(n) & T.C - O(1) in best case.
                And S.C. - O(w).
                ------------------
                In the naive approach for finding maximum from this current window is always - O(w).

                And for iterating the window over the input array, T.C. - O(n).

                So, Final T.C. for both - O(n * w).
                It depends on:- 
                    The values in the list can be:-
                        - Strictly increasing
                        - Strictly decreasing
                        - Constant
                        - Mixed, for example, increasing, decreasing, constant, then decreasing again, 
                        then constant, then increasing, then constant and then decreasing

        """
        if not nums:
            return []

        output = []
        sz = len(nums)
        current_window_top_indices = []
        if len(nums) < k:
            k = len(nums)

        # Firstly catch up the first window.
        for i in range(k):  # 0 to k-1
            # first cleanup & then append the new one
            self.cleanup_less_and_out_of_window_values_from_input_list(
                current_window_top_indices,
                nums,
                i
            )
            current_window_top_indices.append(i)

        output.append(
            nums[
                current_window_top_indices[0]
            ]
        )

        # Final iteration up to last of the nums array
        for i in range(k, sz):
            # 1) first cleanup
            self.cleanup_less_and_out_of_window_values_from_input_list(
                current_window_top_indices,
                nums,
                i
            )
            # 2) check if the 0th index fallen out of the current window, remove it
            if current_window_top_indices and current_window_top_indices[0] <= (i - k):
                _ = current_window_top_indices.pop(0)
            # 3) append the current index
            current_window_top_indices.append(i)
            # 4) append the current window max value (which is the 0th value of the auxiliary array)
            output.append(
                nums[
                    current_window_top_indices[0]
                ]
            )

        return output

    """
        To recap, the solution can be divided into the following parts:
    
    1) First, we validate the inputs. If the input list is empty, we return an empty list and if the window size 
    is greater than the list length, we set the window to be the same size as the input list.
    
    2) Then, we process the first w elements of the input list. We will use a deque to store the indexes of the 
    candidate maximums of each window.
    
    3) For each element, we perform the clean-up step, removing the indexes of the elements from the deque 
    whose values are smaller than or equal to the value of the element we are about to add to the deque. 
    Then, we append the index of the new element to the back of the deque.
    
    4) After the first w elements have been processed, we append the element whose index is present at the front of 
    the deque to the output list as it is the maximum in the first window.
    
    5) After finding the maximum in the first window, we iterate over the remaining input list. 
    For each element, we repeat Step 3 as we did for the first w elements.
    
    6) Additionally, in each iteration, before appending the index of the current element to the deque, 
    we check if the first index in the deque has fallen out of the current window. If so, we remove it from the 
    deque.
    
    7) Finally, we return the list containing the maximum elements of each window.
    
    """
from typing import List

class Solution:
    """
        # Moore Voting Algorithm
            Select candidate and if equal increase count else count --
            if count == 0 then current element is the new candidate
        Ref: https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly/?envType=problem-list-v2&envId=xix1yu51&difficulty=EASY
        
    """
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate: count += 1
            else: count -= 1
        
        return candidate
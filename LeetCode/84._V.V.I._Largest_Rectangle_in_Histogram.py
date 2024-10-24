from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ln = len(heights)
        stack = [] # keeping the tuple of start index and the height on that position which can extend upto the last of the array
                    # if anyone can't extend forward till end then we have to pop the value and calculate the max area
        max_area = -1
        
        for cur_pos in range(ln):
            
            cur_height = heights[cur_pos]
            start = cur_pos
            
            while stack and cur_height < stack[-1][1]: # couldn't extend the top item so pop it from the `monotoinic` stack
                top = stack.pop()
                max_area = max(
                    max_area,
                    (cur_pos - top[0]) * top[1]
                )
                start = top[0] # pushing the start to backwards for keeping the same heights in max area calculation

            stack.append((start, cur_height))
        
        # now looking into the solid start-height pairs where each one will be extended till end of the list.
        while stack:
            top = stack.pop()
            max_area = max(
                max_area,
                (ln - top[0]) * top[1]
            )
        
        return max_area
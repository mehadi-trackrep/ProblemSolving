from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
            Intuition:
            ----------
            At first, we have to sort, cause check them in Greedy way.
            As, we have to remove minimum number of intervals.
            
            So, when comparing the two overlapping intervals side-by-side
            then we must remove the one where `end` is `greater` than the other.
            Cause, `greater end` indicates that there is change to overlap this interval with the next
            one or others. That's why!
        """
        intervals.sort() # it will automatically sort by start value
        minCount = 0
        prevEnd = intervals[0][1] # minEnd
        
        for start, end in intervals[1:]:
            if start >= prevEnd: # doesn't overlap
                prevEnd = end
            else:
                minCount += 1
                prevEnd = min(prevEnd, end)
        
        return minCount
                
        
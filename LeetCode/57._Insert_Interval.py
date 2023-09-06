from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
            Approach:-
                ix, iy = intervals[i][0], intervals[i][1]
                x, y = newInterval[0], newInterval[1]

                we will traverse the intervals.
                and non-overlapping intervals will be added to the left and right of the newInterval
                and overlapping intervals will be merged with the newInterval
                So, ultimately we will have 3 sections/segments of intervals.
        """
        sz = len(intervals)
        start, end = newInterval[0], newInterval[1]
        left, right = [], []

        for i in range(sz):
            start_i, end_i = intervals[i][0], intervals[i][1]
            if end_i < start:
                left.append((start_i, end_i))
            elif end < start_i:
                right.append((start_i, end_i))
            else:
                start = min(start, start_i)
                end   = max(end, end_i)

        ans_temp = left + [(start, end)] + right
        return [list(each_interval) for each_interval in ans_temp]

if __name__ == '__main__':
    obj = Solution()
    # intervals = [[1, 3], [6, 9]]
    # newInterval = [2, 5]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(obj.insert(intervals, newInterval))
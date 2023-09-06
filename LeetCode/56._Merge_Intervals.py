from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sz = len(intervals)
        ans = [] # we have to compare the current interval with the last added interval in "ans"
        '''
            For this, we can use negative index to get the last element in a list.
            And we have to find the end value which is the maximum value of all overlapping intervals.
            As the start will be the first one's start value.
        '''
        intervals.sort(key=lambda x: x[0])
        for i in range(sz):
            if not ans or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans


if __name__ == '__main__':
    obj = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(obj.merge(intervals))
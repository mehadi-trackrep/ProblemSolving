from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashmap = defaultdict(list)
        h = []

        # generate distances without the root as origin same (0, 0) for all points
        for each_point in points:
            d = each_point[0] * each_point[0] + each_point[1] * each_point[1]
            hashmap[d].append(each_point)
            heappush(h, d)

        ans = []
        while k:
            top = heappop(h)
            cnt = len(hashmap[top])
            top_points = hashmap[top]

            if k - cnt >= 0:
                ans.extend(top_points)
                k -= cnt
            else: 
                ans.extend(top_points[0:k])
                k = 0

        
        return ans
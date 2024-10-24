from typing import List
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.all_points_mp = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.all_points_mp[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        px, py = point[0], point[1]
        ans = 0
        for each_point in list(self.all_points_mp): # taking each point as a diagonal and then found the new two corner points if they exists then yes it formas a square!
            x, y = each_point[0], each_point[1]
            """
                N.B. Here, we have to be sure that this (x,y) diagonal point actually can make a sqaure with (px, py)
                Conditions:-
                    if abs(x - px) == abs(y - py) [means dx = dy]
                    and same point couldn't be, mean (x,y) != (px, py)
            """
            if (abs(x - px) != abs(y - py)) or x == px or y == py:
                continue
            x1, y1 = x, py
            x2, y2 = px, y
            ans += (
                self.all_points_mp[(x1, y1)] * 
                self.all_points_mp[(x2, y2)] *
                self.all_points_mp[(px, py)]
            )
        return ans
            

# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
cases = ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
all_points = [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]

for i, case in enumerate(cases):
    # point = input("Enter x.y format string as point: ").strip().split(".")
    if not all_points[i]:
        continue
    point = all_points[i][0]
    if case == "add":
        obj.add(point)
    elif case == "count":
        param_2 = obj.count(point)
        print(param_2)
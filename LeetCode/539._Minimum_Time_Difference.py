from typing import List

class Solution:
    def calculateMinDiff(self, st, bt, isCircularCheck=False) -> int:
        st_list = st.split(":") # st -> small time
        bt_list = bt.split(":") # bt -> big time
        
        st_h, st_m = int(st_list[0]), int(st_list[1])
        bt_h, bt_m = int(bt_list[0]), int(bt_list[1])

        # print(f"st_h, st_m: {st_h}, {st_m}")
        # print(f"bt_h, bt_m: {bt_h}, {bt_m}")
        
        if isCircularCheck:
            return (24*60 - (bt_h*60 + bt_m)) + (st_h*60 + st_m)
        else:
            return (bt_h*60 + bt_m) - (st_h*60 + st_m)

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ln = len(timePoints)
        min_res = self.calculateMinDiff(timePoints[0], timePoints[ln-1], isCircularCheck=True)

        for i in range(1, ln):
            diff = self.calculateMinDiff(timePoints[i-1], timePoints[i])
            min_res = min(min_res, diff)
        
        return min_res            
    
if __name__=="__main__":
    obj = Solution()
    # print(obj.findMinDifference(["23:59","00:00"]))
    print(obj.findMinDifference(["12:12","00:13"]))
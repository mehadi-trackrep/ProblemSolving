from typing import List
from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        pq = []
        """
            This method is direct code of LC - 373 with a very litte change!
        """
        for num in nums1:
            heappush(pq, (num + nums2[0], 0)) # sum & which index of nums2 taken
        
        len_nums2 = len(nums2)
        ans = []
        
        while k and pq:
            top = heappop(pq)
            
            s, nums2_pos = top[0], top[1]
            ans.append(s)
            
            if nums2_pos + 1 < len_nums2:
                heappush(
                    pq,
                    (
                        s - nums2[nums2_pos] + nums2[nums2_pos+1], # s - nums2[nums2_pos] == nums1
                        nums2_pos + 1
                    )
                )
            
            k -= 1
        print(f"==> ans: {ans}")
        return ans

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        res = mat[0]
        for i in range(1, m):
            res = self.kSmallestPairs(
                nums1 = res, 
                nums2 = mat[i], 
                k = k
            )
        print(f"res: {res}")
        return res[k-1]

if __name__=="__main__":
    obj = Solution()
    print(obj.kthSmallest(
        # mat=[[1,3,11],[2,4,6]],
        # mat=[[1,7,11],[2,4,6]],
        # mat=[[1,1,2],[1,2,3]],
        mat = [[1,10,10],[1,4,5],[2,3,6]],
        k = 7
    ))
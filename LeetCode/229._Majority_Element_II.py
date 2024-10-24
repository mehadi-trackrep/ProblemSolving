from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        if ln < 3: return [set(nums)]
        
        nums.sort()
        cnt = 1
        major_cnt = ln // 3
        ans = set()

        for i in range(1, ln):
            if nums[i] == nums[i-1]:
                cnt += 1
                print(f"\t\t\tcnt: {cnt}")
                if cnt > major_cnt:
                    ans.add(nums[i])
            else:
                cnt = 1
            print(f"=> idx: {i}, cnt: {cnt}")
        
        return list(ans)
    

if __name__=="__main__":
    obj = Solution()
    print(obj.majorityElement(nums=[1,2,1,2,1,2,3,2]))
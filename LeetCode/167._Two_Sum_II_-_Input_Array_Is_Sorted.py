from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        ans = []
        while l < r:
            if numbers[l] + numbers[r] == target:
                ans.append(l+1)
                ans.append(r+1)
                break
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return ans

if __name__ == '__main__':
    obj = Solution()
    assert obj.twoSum([2,7,11,15], 9) == [1,2]
    assert obj.twoSum([2,3,4], 6) == [1,3]
    assert obj.twoSum([-1,0], -1) == [1,2]
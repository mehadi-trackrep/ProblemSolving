
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ...
        

if __name__ == '__main__':
    obj = Solution()
    assert obj.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
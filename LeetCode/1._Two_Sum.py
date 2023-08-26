class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = []
        hash_table = dict()
        size = len(nums)
        for idx in range(0, size):
            if (target - nums[idx]) in hash_table:
                indices.append(idx)
                indices.append(hash_table[target - nums[idx]])
                break
            hash_table[nums[idx]] = idx
        return indices

if __name__ == '__main__':  ## AC (hash table - dictionary)
    obj = Solution()

    res = obj.twoSum(
        nums=[8,2,10,4,1,3],
        target=9
    )
    print(res)

    res = obj.twoSum(
        nums=[3,2,-2,4],
        target=6
    )
    print(res)

    res = obj.twoSum(
        nums=[0,4,3,0],
        target=0
    )
    print(res)

    res = obj.twoSum(
        nums=[-10,4,3,0],
        target=-6
    )
    print(res)

    res = obj.twoSum(
        nums=[-10,4,-3,0],
        target=-13
    )
    print(res)
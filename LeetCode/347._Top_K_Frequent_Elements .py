from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## it's kinda bucket sorting
        d, res = {}, []
        size = len(nums)
        ## freq_wise_values = [[]] * (size+1) # it gives incorrect output! Cause:- 
        '''
            This creates a list where all elements are references to the same inner empty list. 
            If you modify the content of one inner list, it will affect all other inner lists since 
            they are the same object in memory.
        '''
        freq_wise_values = [[] for _ in range(size + 1)] # it gives correct output! Cause:-
        '''
            This creates a list where each element is a separate, distinct empty list.
            Modifying one inner list will not affect the others since they are separate objects.
        '''

        # Step - 1: calculating each value frequency TC: O(n)
        for val in nums:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1

        # Step - 2: put each value's frequency in the frequency wise values array! TC: O(n)
        for num, freq in d.items():
            freq_wise_values[freq].append(num)

        # Step - 3: traversing from last towards first index and retrieve total k elements sequentially, TC: O(n)
        for freq in range(size,-1,-1):
            curr_nums = freq_wise_values[freq]
            if len(res)+len(curr_nums) <= k:
                res.extend(curr_nums)
            else:
                if len(res) == k:
                    break
                else:
                    required_items = k - len(res)
                    res.extend(curr_nums[0:required_items])

        # print(f"--> freq_wise_values: {freq_wise_values}")
        # Total time complexity intal O(n) + O(n) + O(n) = O(n)
        
        return res


if __name__=="__main__":
    obj = Solution()
    print(obj.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print(obj.topKFrequent(nums=[-1,-1], k=1))
    print(obj.topKFrequent(nums=[1], k=1))
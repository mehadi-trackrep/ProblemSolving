
"""
    We can go in any one direction and fetch the biggest sequence
    
    # Approach 2:  (run two loops)
        input: nums = [1, 2, 3, 4, 5]
        1. num = 1
            a. curr_num = 1, curr_len = 1, while condition: True
            b. curr_num = 2, curr_len = 2, while condition: True
            c. curr_num = 3, curr_len = 3, while condition: True
            d. curr_num = 4, curr_len = 4, while condition: True
            e. curr_num = 5, curr_len = 5, while condition: False

        2. num = 2
            a. curr_num = 2, curr_len = 1, while condition: True
            b. curr_num = 3, curr_len = 2, while condition: True
            c. curr_num = 4, curr_len = 3, while condition: True
            d. curr_num = 5, curr_len = 4, while condition: False
        .
        .
        .
    # Approach 3: (run two loops but checking one direction with an elegant condition)
        [Super Optimized Brute-force + HashSet] V.V.I.
        
        Input: nums = [2, 3, 1, 4, 5]
        1. curr_num = 2
            1 is present -> Don't run the inner loop
        2. curr_num = 3
            2 is present -> Don't run the inner loop
        3. curr_num = 1
            0 is not present -> Run the inner loop
            a. curr_num = 1, curr_len = 1, while condition: True
            b. curr_num = 2, curr_len = 2, while condition: True
            c. curr_num = 3, curr_len = 3, while condition: True
            d. curr_num = 4, curr_len = 4, while condition: True
            e. curr_num = 5, curr_len = 5, while condition: False 
        4. curr_num = 4
            4-1(3) is present -> No need to run the inner loop
        5. curr_num = 5
            4 is present -> Don't run the inner loop
    
    So, here the inner loop will run only for the small item of a sub sequence. :) 
    Ultimately, while/inner loop will run n times in total. :D

    Another example:-
        Input: nums = [-8, 3, 1, -9, -10, 2, 4]

        So, here basically two sub-sequnences: [-10, -9, -8] & [1, 2, 3, 4]
        1. curr_num = -8:
            -9 exists in the set -> so, skip the inner loop
        2. curr_num = 3:
            2 exists in the set -> so, skip the inner loop
        3. curr_num = 1:
            0 not exists/presents in the set so, run the inner loop:-
            a. curr_num = 1 --> True
            b. curr_num = 2 --> True
            c. curr_num = 3 --> True
            d. curr_num = 4 --> True
            e. curr_num = 5 --> False
        4. curr_num = -9:
            -8 exists in the set -> so, skip the inner loop
        5. curr_num = -10:
            -11 not exist so, 
            a. curr_num = -10 --> True
            b. curr_num = -9 --> True
            c. curr_num = -8 --> True
            d. curr_num = -7 --> False
        6. ..
        7. ..

"""  

class Solution:  
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        best = 0
        for num in nums:
            if num - 1 not in nums_set:
                curr_num = num
                while curr_num+1 in nums_set:
                    curr_num += 1
                best = max(best, (curr_num - num + 1))

        return best

if __name__ == '__main__':      # AC
    solution = Solution()
    lcs = solution.longestConsecutive(nums=[100,4,200,1,3,2])
    lcs = solution.longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1])
    lcs = solution.longestConsecutive(nums=[0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999])
    print(lcs)
    
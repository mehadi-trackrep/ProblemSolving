from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            0.  1.  2. 3  4. 5 (indices)
            -4, -1, -1, 0, 1, 2 (vals)

            -1 (2th) + 2 (5th) = 1 + 0 (3th) == 0 ? if not then if the val is > 0 then r-=1 else l+=1

            -1, -1, 2 

            We can use two pointers & hashmap approaches.
            ## Two pointers approach:
                (1) simply iterate the list(/array) and try to find the triplet for each number
                    (1.1) if the number is > 0 then we don't need to search for any other next numbers
                        have to break.
                        cause the next numbers will be +ve and that will never generate sum 0 :D
                        only answer will be in this case - [0,0,0]
                    (1.2) to avoid duplicates, if the number & previous number is same then don't need
                        to execute the following steps
                    ** (1.1) & (1.2) are the base conditions
                (2) for each number, we have to find two numbers.
                    as we've sorted the list.. so, we will add a lower number (i+1) & a higher number (sz-1)
                    and then we'll look that is the sum > 0 OR sum < 0 OR the sum == 0
                    (2.1) if the sum > 0 means that we need more negative sum to turn it towards 0
                        that means we've to add as less as positive value
                        so, r--
                    (2.2) if the sum < 0 means that we need more postive sum
                        that means w've to add as less as negative values
                        so, l++             
                    (2.3) if the sum == 0 (this is one of the answers but we've to avoid duplicates)
                        (2.3.1) here, we have to ignore the same lower number towards the last (sz-1)
                        (2.3.2) and ignore the same upper number downwards the first position (0)
            Joss solution link: https://leetcode.com/problems/3sum/solutions/3186495/best-c-3-solution-two-pointers-sorting-hash-table-brute-force-optimize/                        
        """
        sz = len(nums)
        nums.sort()
        ans = []

        for i in range(sz):
            if nums[i] > 0: # getting +ve numbers
                break
            if i > 0 and nums[i] == nums[i-1]: # avoiding duplicates (already taken for the first one)
                continue
            # we will search the triplet in (i+1 to sz-1) by taking nums[i]
            l, r = i+1, sz-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: # -ve sum, so we need more positives
                    l += 1
                elif s > 0: # +ve sum, so we need more negatives
                    r -= 1
                else: # sum == 0
                    ans.append((nums[i], nums[l], nums[r]))
                    # now, we've to ignore the duplicates
                        # so, if any of the three numbers occur again then we will get duplicate
                        # check for both of the l & r
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    # এক ঘর শিফট for the same nums[l] & nums[r] othrwise will make an infinite loop
                    l += 1
                    r -= 1
        return [list(each_triplet) for each_triplet in ans]

    
if __name__ == '__main__':
    obj = Solution()
    print(obj.threeSum(
        nums = [-1,0,1,2,-1,-4]
    ))
    print(obj.threeSum(
        nums = [0,0,0]
    ))

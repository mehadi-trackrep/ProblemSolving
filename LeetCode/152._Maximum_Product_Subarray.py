
class Solution:
    def maxProduct(self, nums: list[int]) -> int: # Kadane's Algorithm (a bit modified)
        '''
            As it finds maximum product. So, negative integers will help or not.
            I mean even negatives might create maximum product & 
            odd number of negatives might create minimum product.
            So, here we have to modify the main algoritm a bit like - 
                1. so far minimum currentIndexProduct where the min(3 arguments)
                2. so far maximum currentIndexProduct where the max(3 arguments)
            N.B. To calculate the two above products we should not overwrite any of them. :) 
        '''
        currentIndexMinProduct = currentIndexMaxProduct = overallProduct = nums[0]
        sz = len(nums)
        for idx in range(1, sz):
            # print(f"==>idx: {idx}")
            # print("\tso far currentIndexMaxProduct: {}\n\tso far currentIndexMinProduct: {}".format(currentIndexMaxProduct, currentIndexMinProduct))
            temp =  max(nums[idx], 
                        currentIndexMinProduct*nums[idx], 
                        currentIndexMaxProduct*nums[idx]
                    )
            # print("\ttemp: ", temp)
            currentIndexMinProduct = min(nums[idx], 
                                         currentIndexMinProduct*nums[idx], 
                                         currentIndexMaxProduct*nums[idx]
                                    )
            currentIndexMaxProduct = temp
            overallProduct = max(overallProduct, currentIndexMaxProduct)
        return overallProduct

if __name__ == '__main__':
    obj = Solution()
    nums = [2,3,-2,4]
    # nums = [-2,0,-1]
    print(nums)
    print(obj.maxProduct(nums))
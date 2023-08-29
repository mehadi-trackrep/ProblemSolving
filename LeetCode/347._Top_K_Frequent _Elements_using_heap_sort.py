from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for key, val in d.items():
            arr.append((val, key))

        return self.heap_sort(arr, k)
    
    def heap_sort(self, arr, k) -> List[int]:

        def heapify(n, i):
            l = 2*i+1
            r = 2*i+2
            largest = i #initialize largest node as root
            
            # try:
            #     print("\n")
            #     print("i: ", i)
            #     print(f"arr: {arr}")
            #     print(f"arr[largest][0]: {arr[largest][0]}")
            #     print(f"arr[l][0]: {arr[l][0]}")
            #     print(f"arr[r][0]: {arr[r][0]}")
            # except Exception as e:
            #     ...
            # finally:
            #     print("\n")

            if l < n and arr[largest][0] < arr[l][0]:
                largest = l
            if r < n and arr[largest][0] < arr[r][0]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(n, largest)

        #step 1: build heap (max heap)
        n = len(arr)
        for i in range(n//2-1, -1, -1):
            heapify(n, i) #heapify the subtree rooted at index i

        #step 2: extract element one by one
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(i, 0) #heapify the reduced heap as the root element has been changed
        
        k *= (-1)
        return [x[1] for x in arr[k:]]

if __name__=="__main__":
    obj = Solution()
    print(obj.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print(obj.topKFrequent(nums=[-1,-1], k=1))
    print(obj.topKFrequent(nums=[1], k=1))

from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        hashmap = defaultdict(list) # key -> freq and value -> items of same freq
        freq = defaultdict(int) # key -> item & value -> freq
        h = []
        
        for word in words:
            freq[word] += 1
        
        for word, f in freq.items():
            hashmap[f].append(word)
        
        for f in hashmap.keys():
            heappush(h, (-1) * f) # need max heap
        
        ans = []
        while k:
            f = heappop(h) * (-1)
            l = hashmap[f] # associated list of words of this frequency - 'f'
            
            print(f"f: {f}, l: {l}")

            if k and  k - len(l) >= 0:
                if l:
                    ans.extend(sorted(l))
                k -= len(l)
            else:
                # print(f"---: {sorted(l)[0:k]}")
                ans.extend(sorted(l)[0:k])
                k = 0
        
        return ans
        
if __name__ == "__main__":
    obj = Solution()
    print(obj.topKFrequent(
        words=["i","love","leetcode","i","love","coding"], 
        k = 2
    ))
    print(obj.topKFrequent(
        words=["the","day","is","sunny","the","the","the","sunny","is","is"], 
        k = 4
    ))
    print(obj.topKFrequent(
        words=["i","love","leetcode","i","love","coding"], 
        k = 3
    ))
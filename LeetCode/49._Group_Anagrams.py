from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
            else:
                hash_map[sorted_word] = [word]
        return list(hash_map.values())

if __name__ == '__main__':
    obj = Solution()
    print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(obj.groupAnagrams([""]))
    print(obj.groupAnagrams(["a"]))
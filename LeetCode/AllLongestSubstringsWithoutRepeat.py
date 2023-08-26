
class Solution:
	def allLongestSubstringsWithoutRepeat(self, s: str) -> int:
		char_set = []
		max_len, substr_start_idx, curr_idx = 0, 0, -1
		all_max_substrings = [] #stack, tortoise & max_len is hare
		
		for char in s:
			if char in char_set:
				if max_len == (curr_idx - substr_start_idx):
					all_max_substrings.append(s[substr_start_idx:curr_idx])
				for each_substr in all_max_substrings:
					if len(each_substr) < max_len:
						all_max_substrings.pop()
					else:
						break

			while char in char_set:
				char_set.pop(0)
				substr_start_idx += 1
				
			char_set.append(char)
			max_len = max(
				 max_len
				,curr_idx - substr_start_idx
			)
			curr_idx += 1

		if max_len == (curr_idx - substr_start_idx): # if no duplicate char appears or for the last max substring
			all_max_substrings.append(s[substr_start_idx:curr_idx])
			for each_substr in all_max_substrings:
				if len(each_substr) < max_len:
					all_max_substrings.pop()
				else:
					break
		print("==> all_max_substrings: ", all_max_substrings)
		
		return max_len


if __name__=="__main__":
	obj = Solution()
	print(obj.allLongestSubstringsWithoutRepeat("workattech"))
	print(obj.allLongestSubstringsWithoutRepeat("mississippi"))
	print(obj.allLongestSubstringsWithoutRepeat("mehadi49"))
	print(obj.allLongestSubstringsWithoutRepeat("abcaaaaworkattech"))
    
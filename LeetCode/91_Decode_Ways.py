class Solution:
    def __init__(self):
        self.memory = [-1 for _ in range(0, 101)]
    def numDecodings(self, s: str) -> int:
        self.__init__()
        return self.rec(s, 0)
    def rec(self, s, current_pos) -> int:
        if current_pos > len(s):
            return 0
        if current_pos == len(s):
            return 1
        if s[current_pos] == '0':
            return 0
        if self.memory[current_pos] != -1:
            return self.memory[current_pos]

        next_call = False
        if current_pos + 1 < len(s):
            val = int(s[current_pos]) * 10 + int(s[current_pos + 1])
            # print("val: ", val)
            if val <= 26:
                next_call = True
        if next_call:
            self.memory[current_pos] = self.rec(s, current_pos+1) + self.rec(s, current_pos+2)
        else:
            self.memory[current_pos] = self.rec(s, current_pos+1)
        return self.memory[current_pos]

if __name__ == '__main__':  ## AC
    solution_obj = Solution()
    
    input_test_cases = ['27' ,'226', '012345', '101010', '10100', '111', '1203', '12',
                        "111111111111111111111111111111111111111111111"]
    
    for each_tc in input_test_cases:
        print(each_tc, " - ", solution_obj.numDecodings(s=each_tc))

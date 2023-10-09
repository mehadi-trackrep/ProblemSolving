class Solution:
    def minWindow(self, s: str, t: str) -> str:

        print("s: ", s)
        print("t: ", t)

        start , end, counter, sz = 0, 0, len(t), len(s)
        min_window_length = sz + 1
        minStart = 0, 0
        mp = dict()

        #1
        for c in t:
            mp[c] = mp.get(c, 0) + 1
        
        #2
        while end < sz:
            # 2.1
            print(f"---> end: {end},\tmp: {mp}")
            if mp.get(s[end], 0) > 0:
                counter -= 1 # got a char matched with t
            
            mp[s[end]] = mp.get(s[end], 0) - 1 # it will decrease the both chars count from s & t
                    # so, for those chars exist in s but in t the map count will be negative.
                    # and for those chars exist in both strings but more in s the the count might be
                    # negative also.
            print(f"===> end: {end},\tmp: {mp}\n")
            # 2.2
            while counter == 0:
                print("start: ", start)
                # 2.2.1
                if end - start + 1 < min_window_length:
                    min_window_length = end - start + 1
                    minStart = start
                    print("--> s[minStart:minStart+min_window_length]: ", s[minStart:minStart+min_window_length])
                # 2.2.2
                    # আগে mapping এ increment তারপর চেক করা যে, এই char টা আগে থেকেই আছে কিনা।
                mp[s[start]] = mp.get(s[start], 0) + 1 # this statement is v.v.i. important before the next line
                if mp[s[start]] > 0:
                    counter += 1
                start += 1

            end += 1
        
        return "" if min_window_length == sz + 1 else s[minStart:minStart+min_window_length]


if __name__ == '__main__':
    obj = Solution()
    assert obj.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    # assert obj.minWindow("a", "a") == "a"
    # assert obj.minWindow("a", "aa") == ""
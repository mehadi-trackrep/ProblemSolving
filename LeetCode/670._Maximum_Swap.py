class Solution:
    def maximumSwap(self, num: int) -> int:
        mp = {}
        s = str(num)
        is_swap_done = False
        ln = len(s)

        for i in range(ln):
            n = int(s[i])
            if n in mp:
                mp[n] = (mp[n][0] + 1, i)
            else: mp[n] = (1, i) # freq and last index
            
        print(mp)
        
        lpos, rpos = -1, -1
        
        for cur_pos in range(ln):
            n = int(s[cur_pos]) # cur val
            if is_swap_done: break
            if n != 9: # there is a change to get 9 / up to n+1, let's check
                for val in range(9, n, -1):
                    if val in mp and mp[val][0] > 0 and mp[val][1] > cur_pos:
                        # print(f"n: {n}, val: {val}, mp[val][0]: {mp[val][0]}")
                        last_pos = mp[val][1] # last pos of val
                        # backups the swap positions
                        lpos = cur_pos
                        rpos = last_pos
                        is_swap_done = True
                        break
            
            mp[n] = (mp[n][0] - 1, mp[n][1])
        
        if lpos == -1 or rpos == -1: 
            return int(s)
        else: 
            return int(s[0:lpos] + s[rpos] + s[lpos+1:rpos] + s[lpos] + s[rpos+1:])
    
if __name__=="__main__":
    obj = Solution()
    print(obj.maximumSwap(9987859391))
    
    print(obj.maximumSwap(9973))
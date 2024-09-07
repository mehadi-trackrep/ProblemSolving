class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        '''
            1. iterate through the numbers
            2. count if it's odd else make the cnt = 0
            3. if cnt == 3: return True
            4. otherwise after the loop return False
        '''
        cnt = 0
        for val in arr:
            if val&1: # odd
                cnt += 1
            else:
                cnt = 0
            if cnt >= 3:
                return True
        return False

        # single line solution:-
        # return '111' in ''.join(str(v&1) for v in a)
        # or:
        # return any(1&v&u&w for v,u,w in zip(a,a[1:],a[2:]))
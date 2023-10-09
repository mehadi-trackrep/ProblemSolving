class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            :type s: str
            :type t: str
            :rtype: str
        """
        
        '''
            Idea/Approach: Use "two pointers"; "counter" and "hash_map".
            -------------
            Two pointers:-
                    1) moving 'end' pointer forward to find a valid window by expanding the
                            current window,
                    2) moving 'start' pointer forward to find a smaller window 
                            when we have a valid window then.
            'counter' and 'hash_map' to determine whether the window is valid or not.

            V.V.I. ==> 'counter' means 'how many chars still left/required to be included' 
                        in the current window.
                        If all of them included (means counter = 0) then the window will be 
                        a valid one. [V.V.I. - MUST]
                
                When we have the counter == 0 that means now the current window is valid
                And this valid criteria is different for different problems.

                Suppose: two strings s and t, and we need to find the minimum window in s which have to
                contain all the characters in t.
                So, we have to initially declare the counter = t.size()
                and then we have to decrease the counter when we find a character in s which is also in t.
                And when the counter will be 0 (counter == 0) then we will get this current window is a 
                valid window.
                And then we have to try for finding a smaller window by moving the 'start' pointer forward.
        '''

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
            if mp.get(s[end], 0) > 0:
                counter -= 1 # got a char matched with t
            
            mp[s[end]] = mp.get(s[end], 0) - 1 # it will decrease the both chars count from s & t
                    # so, for those chars exist in s but in t the map count will be negative.
                    # and for those chars exist in both strings but more in s the the count might be
                    # negative also.
            
            # 2.2
            while counter == 0:
                # 2.2.1
                if end - start + 1 < min_window_length:
                    min_window_length = end - start + 1
                    minStart = start
                # 2.2.2
                mp[s[start]] = mp.get(s[start], 0) + 1 # this statement is v.v.i. important before the next line
                if mp[s[start]] > 0:
                    counter += 1
                start += 1

            end += 1
        
        return "" if min_window_length == sz + 1 else s[minStart:minStart+min_window_length]

    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        counter = 1 # "1" means still valid window; "0" means now the window has been invalid
        mx_length_window = 0
        mp = {}

        while end < len(s):
            mp[s[end]] = mp.get(s[end], 0) + 1
            if mp[s[end]] > 1:
                counter = 0
            
            while counter == 0:
                mp[s[start]] -= 1
                if mp[s[start]] == 1:
                    counter = 1
                start += 1

            mx_length_window = max(mx_length_window, end - start + 1)
            
            end += 1
        
        return mx_length_window
## ------------------------------------------------------------------------------------------

"""

Template:-

    int findSubstring(string s){
        vector<int> map(128,0);
        
        int counter; // check whether the substring is valid
        int begin=0, end=0; //two pointers, one point to tail and one  head
        int d; //the length of substring

        for() { /* initialize the hash map here */ }

        while(end<s.size()){

            if(map[s[end++]]-- ?){  /* modify counter here */ }

            while(/* counter condition */){ 
                 
                 /* update d here if finding minimum*/

                //increase begin to make it invalid/valid again
                
                if(map[s[begin++]]++ ?){ /*modify counter here*/ }
            }  

            /* update d here if finding maximum*/
        }
        return d;
  }

"""
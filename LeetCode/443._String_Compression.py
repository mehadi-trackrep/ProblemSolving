from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i, l, r = 0, 0, 0
        sz = len(chars)

        while i < sz:
            # print("==> i, l: ", i, l)

            while i < sz and l < sz and chars[i] == chars[l]:
                i += 1

            cnt = i - l
            l = i # it's pointing to the next unique char

            if cnt > 1:
                chars[r] = chars[l-1]
                r += 1
                digits = []
                while cnt:
                    d = cnt % 10
                    cnt //= 10
                    digits.append(str(d))
                for each_digit in digits[::-1]:
                    chars[r] = each_digit
                    r += 1
            else:
                chars[r] = chars[l-1]
                r += 1
        chars = chars[:r]
        print("==> chars: ", chars)
        print('==> r: ', r)

        return r

if __name__ == '__main__':
    obj = Solution()
    assert obj.compress(["a","a","b"]) == 3
    assert obj.compress(["a","a","b","b","c","c","c","a"]) == 7
    assert obj.compress(["a","a","b","b","c","c","c"]) == 6
    assert obj.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4
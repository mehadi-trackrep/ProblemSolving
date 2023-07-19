import math
from functools import reduce

def solution(n, coins):
    coins.sort(reverse=True)
    total_sum = reduce(lambda x, y: x+y, coins)
    avg = math.floor(total_sum / 2)
    ss = 0
    for i in range(n):
        ss += coins[i]
        if ss > avg:
            return i+1

if __name__ == '__main__':
    n = int(input())
    coins = [int(i) for i in input().strip().split()]
    ans = solution(n, coins)
    print(ans)
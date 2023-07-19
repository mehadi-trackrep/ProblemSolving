class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        sz = len(prices)
        mx_profit = 0
        min_price = prices[0]
        for i in range(sz):
            min_price = min(min_price, prices[i])
            mx_profit = max(mx_profit, (prices[i] - min_price))
        return mx_profit

if __name__ == '__main__':
    obj = Solution()
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    print(obj.maxProfit(prices))

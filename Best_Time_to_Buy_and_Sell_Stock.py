class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(0, len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                if max_profit < (prices[i]- min_price):
                    max_profit =  prices[i]- min_price
        return max_profit


sol = Solution()
prices = [7,1,5,3,6,4]

print(sol.maxProfit(prices))
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in reversed(range(1,len(prices))):
            min_val = min(prices[:i])
            min_idx = prices.index(min_val)
            max_val = max(prices[min_idx:])
            #print(i, min_idx, max_val)
            if (max_val - min_val) > result:
                # update the result if bigger
                result = max_val - min_val
        return result
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxs=0
        left=0
        for right in range(1,len(prices)):
            diff = prices[right]-prices[left]
            if prices[left]>prices[right]:
                left=right
            elif maxs<diff:
                maxs=diff
        return maxs
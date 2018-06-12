def maxProfit(self, prices):
        last=0
        
        for i in range (1,len(prices)):
            last+=max(0,prices[i]-prices[i-1])
        return last
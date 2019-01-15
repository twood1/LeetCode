# Dynamic programming bottom up solution. Recurrence: opt[Val] = min(opt[Val-C]+1) for all C in coins.

class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        opt = [0]*(amount+1)
        currVal = 1
        while currVal <= amount:
            if currVal in coins:
                opt[currVal] = 1
            minCount = float('Inf')
            for coin in coins:
                if currVal - coin < 0:
                    continue
                numcoins = opt[currVal-coin]+1
                if numcoins < minCount:
                    minCount = numcoins
            opt[currVal] = minCount
            currVal = currVal+1
        retval = opt[amount]
        if opt[amount] == float('inf'):
            retval = -1
        return retval

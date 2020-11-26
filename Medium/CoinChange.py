class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        coins = set(coins)
        if amount in coins:
            return 1
        opt = [0] + [float('inf')]*(amount)
        currVal = 1
        # Compute the best possible answer all the way up to the amount we need to reach.
        while currVal <= amount:
            # if our current value in cents is in our coins, we know we are done. It's 1 coin to reach this.
            if currVal in coins:
                opt[currVal] = 1
            else:
                currentMin = float('inf')
                # Check all possible coins we have. Look up our list[X - coin]. Put the minimum value we found in here,
                # plus 1.
                for coin in coins:
                    if coin < currVal:
                        if opt[currVal - coin] + 1 < currentMin:
                            currentMin = opt[currVal - coin] + 1
                opt[currVal] = currentMin
            currVal += 1
        # return -1 if there is no solution. Otherwise return the end of the list (where we computed our final answer..)
        return -1 if opt[amount] == float('inf') else opt[amount]

sol = Solution()
print(sol.coinChange([3,4,5], 995))
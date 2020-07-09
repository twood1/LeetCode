class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        coins = set(coins)
        if amount in coins:
            return 1
        opt = [0] + [float('inf')]*(amount)
        currVal = 1
        while currVal <= amount:
            if currVal in coins:
                opt[currVal] = 1
            else:
                currentMin = float('inf')
                for coin in coins:
                    if coin < currVal:
                        if opt[currVal - coin] + 1 < currentMin:
                            currentMin = opt[currVal - coin] + 1
                opt[currVal] = currentMin
            currVal += 1
        return -1 if opt[amount] == float('inf') else opt[amount]

sol = Solution()
print(sol.coinChange([2, 5, 7], 638))
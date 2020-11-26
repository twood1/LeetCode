class Solution(object):
    def candy(self, ratings):
        if not ratings:
            return 0

        if len(ratings) == 1:
            return 1

        candies = [1] * len(ratings)

        # fill in increasing sequences candy values
        candyCount = 1
        for i in range(len(candies) - 1):
            candies[i] = candyCount
            if ratings[i + 1] > ratings[i]:
                candyCount += 1
            else:
                candyCount = 1

        candies[len(candies) - 1] = candyCount

        # decreasing sequences. But for each candy value, we need to take the max.
        candyCount = 1
        for i in range(len(candies) - 1, 0, -1):
            candies[i] = max(candyCount, candies[i])
            if ratings[i - 1] > ratings[i]:
                candyCount += 1
            else:
                candyCount = 1

        candies[0] = max(candies[0], candyCount)
        return sum(candies)


ans = Solution().candy([1,0,2,4,5,2,3,6,3,4,3,2,1,2,0,4])
print(ans)
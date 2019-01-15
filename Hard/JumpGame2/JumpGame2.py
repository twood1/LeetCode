class Solution:
    def jump(self, nums):
        N = len(nums)
        opt = [0]
        [opt.append(float('inf')) for _ in range(N-1)]
        i = 0
        maxIdx = 0
        while i < N:
            currNum = nums[i]
            if currNum+i > maxIdx:
                stop = min((currNum+i+1)-maxIdx, N-maxIdx)
                for j in range(1, stop):
                    opt[maxIdx+j] = opt[i]+1
                maxIdx = currNum+i
                if maxIdx > N-1:
                    return opt[-1]
            i = i+1
        return opt[-1]

Sol = Solution()
print(Sol.jump([1,1,1,1]))


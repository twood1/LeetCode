class Solution(object):
    def canArrange(self, arr, k):
        modhash = {}
        for i in range(0, len(arr)):
            ele = arr[i]
            if ele % k not in modhash:
                modhash[ele % k] = [i]
            else:
                modhash[ele % k].append(i)

        retval = True
        for key in modhash:
            if key == 0:
                retval = retval & (len(modhash[key]) % 2 == 0)
            else:
                if k-key not in modhash:
                    retval = False
                    break
                retval = retval & (len(modhash[key]) == len(modhash[k-key]))
        return retval


sol = Solution()
print(sol.canArrange([1,2,3,4,5,6], 7))
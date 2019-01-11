class Solution:
    def numJewelsInStones(self, J, S):
        jewels = {}
        retval = 0
        for c in J:
            jewels[c] = True
        for s in S:
            if s in jewels:
                retval = retval+1
        return retval
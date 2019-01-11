class Solution:
    def repeatedNTimes(self, A):
        elements = {}
        for ele in A:
            if ele not in elements:
                elements[ele] = True
            else:
                return ele
# Upon first glance, this may seem like it doesn't have a clear answer. But, consider this:
# Any binary number B1 with a digit further than another binary number B2 means B1 > B2.
# So the most straightforward solution: Optimize rows to be largest first, then columns to be largest.
# Rows to be largest means simply looking at the first bit - if it's 0, flip it. If not, don't.
# Columns to be largest means the number of 1's should exceed the number of 0's.

class Solution(object):
    # helper method to flip a passed in row
    def fliprow(self, row):
        for i in range(0, len(row)):
            if row[i] == 0:
                row[i] = 1
            else:
                row[i] = 0
        return row

    # helper method to flip a column given an index 'col'
    def flipcolumn(self, A, col):
        for i in range(0, len(A)):
            if A[i][col] == 0:
                A[i][col] = 1
            else:
                A[i][col] = 0
        return A

    def matrixScore(self, A):
        for i in range(0, len(A)):
            if A[i][0] != 1:
                A[i] = self.fliprow(A[i])

        for j in range(0, len(A[0])):
            sum = 0
            for i in range(0, len(A)):
                sum = sum+A[i][j]
            if sum < len(A)/2:
                A = self.flipcolumn(A, j)
        retval = 0
        for arr in A:
            # Abuse pythons int(x,2) binary conversion of strings. Just join the array into a binary string then int it.
            retval += int("".join(str(x) for x in arr),2)
        return retval





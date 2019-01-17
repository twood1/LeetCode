
class Solution:
    def isMatch(self, s, p):
        # Takes care of the case where s and p both are empty string, and returns fast if they are just generally equal
        if s == p:
            return True

        mat = []
        [mat.append([False]*(len(s)+1)) for _ in range(len(p)+1)]
        # The emptry string always matches itself
        mat[0][0] = True
        # Fix the first column
        for i in range(0, len(p)):
            c = p[i]
            if c == "*":
                mat[i+1][0] = mat[i][0]


        for i in range(len(p)):
            for j in range(len(s)):
                c1 = s[j]
                c2 = p[i]
                # If the character is a star, we are free to match any path to this cell - top, top left, or left.
                if c2 == "*":
                    mat[i+1][j+1] = mat[i][j] or mat[i+1][j] or mat[i][j+1]
                # If the character is a ?, the value here is just simply the value from the previous match (top left)
                elif c2 == "?":
                    mat[i+1][j+1] = mat[i][j]
                # Otherwise, the character must be equal and the previous match (top left) must both match.
                else:
                    mat[i+1][j+1] = mat[i][j] and (c1 == c2)
        return mat[len(p)][len(s)]

class Solution:
    def longestPalindrome(self, s):
        # Initialize identity matrix. Set False to be None so we receive an error if we compute things out of order.
        bool_matrix = [[True if j == i else None for j in range(len(s))] for i in range(len(s))]

        # Current indicies for substring s[i:j+1]. Reminder string slicing is [inclusive:noninclusive] so
        # we need the +1 in s[i:j+1]


        bestStart = 0
        bestEnd = 0
        bestSize = 1

        j = 1
        while j < len(s):
            i = 0
            print(i, j)
            while i < j:
                # if s[i] does not equal s[j], there is no possible way the substring from i to j is a palindrome
                if s[i] != s[j]:
                    bool_matrix[i][j] = False
                # edge case of two characters next to each other being the same
                elif i == j-1:
                    if bestSize < 2 and s[i] == s[j]:
                        bestStart = i
                        bestEnd = j
                        bestSize = j - i + 1
                    bool_matrix[i][j] = (s[i] == s[j])
                # otherwise, the ends match, and we need to evaluate if the substring in-between is a palindrome.
                else:
                    is_substring_palindrome = (bool_matrix[i+1][j-1]) & (s[i] == s[j])
                    bool_matrix[i][j] = is_substring_palindrome

                    if is_substring_palindrome:
                        currSize = j - i + 1
                        if currSize > bestSize:
                            bestStart = i
                            bestEnd = j
                            bestSize = currSize

                i += 1
            j += 1
        return s[bestStart:bestEnd+1]

sol = Solution()
answer = sol.longestPalindrome('aaaa')
print(answer)
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"




class Solution:
    def checkPalindrome(self, s, startIdx, endIdx):
        start = startIdx
        end = endIdx
        while (start - 1) >= 0 and (end + 1) < len(s):
            if s[start - 1] == s[end + 1]:
                start = start - 1
                end = end + 1
            else:
                break
        return start, end

    def longestPalindrome(self, s):
        bestStart, bestEnd = 0, 0
        for idx in range(0, len(s)):
            # check for odd palindromes starting and ending at idx (one center character)
            startOdd, endOdd = self.checkPalindrome(s, idx, idx)
            evenSize = 0
            oddSize = endOdd - startOdd + 1
            # check for even palindromes starting at idx and ending at idx + 1 (two center character)
            if idx < len(s) - 1:
                if s[idx + 1] == s[idx]:
                    startEven, endEven = self.checkPalindrome(s, idx, idx+1)
                    evenSize = endEven - startEven + 1
            # only ever true if we computed evenSize, since we initialize it to 0 and oddSize will be at minimum 1.
            if evenSize > oddSize:
                start = startEven
                end = endEven
            else:
                start = startOdd
                end = endOdd
            if (end - start + 1) > (bestEnd - bestStart + 1):
                bestStart = start
                bestEnd = end
        return s[bestStart:(bestEnd+1)]

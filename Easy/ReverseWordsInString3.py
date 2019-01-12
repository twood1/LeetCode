# recursive
class SolutionRec(object):
    def reverseWords(self, s):
        if not s:
            return ""
        revWord = ""
        i = 0
        while i < len(s):
            if s[i] == " ":
                revWord = revWord+" "
                break
            revWord = s[i]+revWord
            i = i+1

        return revWord+self.reverseWords(s[(i+1):])

# without using str.split()
class SolutionNoStrSplit(object):
    def reverseWords(self, s):
        currWord = ""
        retval = ""
        lastchar = None
        for c in s:
            if c == " ":
                currWord = currWord[::-1]
                retval = retval+currWord+" "
                currWord = ""
                continue
            currWord = currWord + c
            lastchar = c

        if lastchar != " ":
            retval = retval+currWord[::-1]
        return retval

# built in .split function and using slicing to reverse
class Solution(object):
    def reverseWords(self, s):
        retString = ""
        myArr = s.split(" ")
        for i in range(0,len(myArr)):
            ele = myArr[i]
            rev = ele[::-1]
            if i != len(myArr)-1:
                retString += rev+" "
            else:
                retString += rev
        return retString
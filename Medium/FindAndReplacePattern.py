class Solution:
    def findAndReplacePattern(self, words, pattern):
        patternHash = {}
        length = (len(pattern))
        patternMap = []
        for i in range(length):
            if pattern[i] in patternHash:
                patternMap.append(patternHash[pattern[i]])
            else:
                patternHash[pattern[i]] = i
                patternMap.append(i)

        length = len(words)
        retval = []
        for i in range(length):
            word = words[i]
            length2 = len(words[i])
            wordHash = {}
            wordMap = []
            cont = False
            for j in range(length2):
                if word[j] in wordHash:
                    wordMap.append(wordHash[word[j]])
                else:
                    wordHash[word[j]] = j
                    wordMap.append(j)
                if wordMap[j] != patternMap[j]:
                    cont = True
                    break
            if cont:
                continue
            retval.append(word)
        return retval

Sol = Solution()
print(Sol.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))

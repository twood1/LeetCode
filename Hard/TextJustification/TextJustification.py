class Solution:
    def fullJustify(self, words, maxWidth):
        N = len(words)
        currLength = 0
        i, j = 0,0
        lines = []
        while j < N:
            if currLength == 0:
                val = len(words[j])
            else:
                val = currLength + 1 + len(words[j])
            if val < maxWidth:
                j = j+1
                currLength = val
            elif val == maxWidth:
                line = self.makeline(words[i:(j+1)], maxWidth, False)
                i, j = j+1, j+1
                currLength = 0
                lines.append(line)
            else:
                line = self.makeline(words[i:j], maxWidth, False)
                i, j = j, j
                currLength = 0
                lines.append(line)

        if words[i:j]:
            lastLine = self.makeline(words[i:j], maxWidth, True)
            lines.append(lastLine)
        return lines


    def makeline(self, words, maxWidth, lastline):
        retval = ""
        if lastline:
            for word in words:
                retval += word+" "
            retval = retval.rstrip()
            while len(retval) < maxWidth:
                retval = retval + " "
        else:
            spacePointers = []
            for word in words:
                retval += word+" "
                spacePointers.append(len(retval))

            retval = retval.rstrip()
            spacePointers.pop()

            if spacePointers:
                currentSpacePosition = 0
                N = len(spacePointers)
                while len(retval) < maxWidth:
                    idx = spacePointers[currentSpacePosition % N]
                    retval = retval[0:idx]+" "+retval[idx:]
                    for i in range(currentSpacePosition, len(spacePointers)):
                        spacePointers[i] += 1
                    currentSpacePosition += 1
            else:
                while len(retval) < maxWidth:
                    retval = retval + " "
        return retval
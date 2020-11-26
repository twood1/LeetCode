class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False

class Solution(object):
    def addWord(self, root, word):
        if not word:
            root.isWord = True
            return None

        nextChar = word[0]
        if nextChar in root.children:
            self.addWord(root.children[nextChar], word[1::])
        else:
            child = TrieNode(val=nextChar)
            root.children[nextChar] = child
            if len(word) > 1:
                self.addWord(root.children[nextChar], word[1::])
            else:
                child.isWord = True

    def searchBoard(self, node, board, i, j, currword, visited):
        foundWords = []
        if node.isWord:
            foundWords.append(currword)

        if node.children:
            neighbors = self.getNeighbors(board, i, j, visited)
            for neighbor in neighbors:
                if neighbor[0] in node.children:
                    for idx in neighbors[neighbor]:
                        newvisited = visited.copy()
                        newvisited.add((idx[0], idx[1]))
                        words = \
                            self.searchBoard(node.children[neighbor[0]], board, idx[0], idx[1],
                                             currword+neighbor, newvisited)
                        if words:
                            for ele in words:
                                foundWords.append(ele)
        return foundWords

    def getNeighbors(self, board, i, j, visited):
        neighbors = {}
        if i > 0:
            if (i - 1, j) not in visited:
                char = board[i - 1][j]
                if char in neighbors:
                    neighbors[char].append((i - 1, j))
                else:
                    neighbors[char] = [(i - 1, j)]
        if i < (len(board) - 1):
            if (i + 1, j) not in visited:
                char = board[i + 1][j]
                if char in neighbors:
                    neighbors[char].append((i + 1, j))
                else:
                    neighbors[char] = [(i + 1, j)]
        if j > 0:
            if (i, j - 1) not in visited:
                char = board[i][j - 1]
                if char in neighbors:
                    neighbors[char].append((i, j - 1))
                else:
                    neighbors[char] = [(i, j - 1)]
        if j < (len(board[0]) - 1):
            if (i, j + 1) not in visited:
                char = board[i][j + 1]
                if char in neighbors:
                    neighbors[char].append((i, j + 1))
                else:
                    neighbors[char] = [(i, j + 1)]
        return neighbors

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        # construct Trie with sorted words
        trieRoot = TrieNode('')
        startingChars = {}
        for w in words:
            if w == 'aaa':
                print('here')
            self.addWord(trieRoot, w)
            if w[0] not in startingChars:
                startingChars[w[0]] = 1
            else:
                startingChars[w[0]] += 1

        boardHash = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                cellchar = board[i][j]
                if cellchar not in boardHash:
                    boardHash[cellchar] = [(i,j)]
                else:
                    boardHash[cellchar].append((i,j))

        retval = []
        for c in startingChars.keys():
            if c not in boardHash:
                continue

            for idx in boardHash[c]:
                if startingChars[c] == 0:
                    break
                foundWords = self.searchBoard(trieRoot.children[c], board, idx[0], idx[1], c, {(idx[0], idx[1])})
                startingChars[c] -= len(foundWords)
                for w in foundWords:
                    retval.append(w)
        print(list(set(retval)))
        return list(set(retval))









sol = Solution()
sol.findWords(board = [["a","b"],["a","a"]],
words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"])
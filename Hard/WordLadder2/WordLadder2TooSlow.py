# we will build a graph that has nodes with words as values, and edges to nodes that are 1 distance away.
# Then, simply do DFS, and whenever we see the endWord, store that path in an array.
# At the end, clean the array for min length arrays only.

# We are told there are no duplicates in the list, and that endWord != beginWord, therefore there are no duplicates
# anywhere.

# This solution is actually too slow. It may be because of the overhead via classes, but it may also be that DFS is
# just simply to inefficient here. Things that might improve this script:
# 1) Terminate paths early if we cannot possibly reach the endWord before maxDepth is reached. I.e., if we find
# endWord with BFS to be 5 hops away, and we have a word that takes more than 5 transformations to reach endWord, then
# terminate.
# 2) Replace graph with hash table which is "word" : list of neighbors as strings.

class Solution:
    def __init__(self):
        self.graph = []

    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []


        for word in wordList:
            self.graph.append(self.Node(word))

        for i in range(0,len(self.graph)):
            for j in range(i+1, len(self.graph)):
                if self.distanceOne(self.graph[i].val, self.graph[j].val):
                    self.graph[i].neighbors.append(self.graph[j])
                    self.graph[j].neighbors.append(self.graph[i])

        startNode = self.Node(beginWord)
        for node in self.graph:
            if self.distanceOne(node.val, startNode.val):
                startNode.neighbors.append(node)

        # I like to declare before I return... Debugging!
        maxD = self.maxDepth([startNode], endWord, 0, [])
        paths = self.targetDFS(startNode, endWord, maxD, [], [])
        return paths


    def targetDFS(self, currNode, endWord, maxD, currentPath, visited):
        currentPath.append(currNode.val)
        visited.append(currNode.val)
        # if we've reached the endWord, stop doing dfs for this branch, immediately return the path
        if currNode.val == endWord:
            retval = currentPath.copy()
            currentPath.pop()
            return [retval]
        if len(currentPath) >= maxD:
            currentPath.pop()
            return []
        finalpaths = []
        for node in currNode.neighbors:
            if node.val in currentPath or node.val in visited:
                continue
            paths = self.targetDFS(node, endWord, maxD, currentPath, visited)
            for path in paths:
                finalpaths.append(path)
        currentPath.pop()
        return finalpaths

    # We don't really want to check EVERY possible path, we should terminate it if we know it has exceeded the
    # time it takes to find it with a BFS. If there exists 1 path via BFS from beginWord->endWord, then we shouldn't
    # count any paths that exceed that length.

    def maxDepth(self, currNodeSet, endWord, i, visited):
        for node in currNodeSet:
            visited.append(node.val)
        if endWord in visited:
            return i+1

        nextSet = []
        for node2 in currNodeSet:
            for neighbor in node2.neighbors:
                if neighbor.val not in visited:
                    nextSet.append(neighbor)

        if not nextSet:
            return -1

        return self.maxDepth(nextSet, endWord, i+1, visited)




    class Node:
        def __init__(self, x):
            self.val = x
            self.neighbors = []

    def distanceOne(self, s1, s2):
        diffs = 0
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                diffs = diffs+1
            if diffs > 1:
                return False
        return True

Sol = Solution()
print(Sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# Sol = Solution()
# print(Sol.findLadders("cet", "ism", ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]))

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visited=set(wordList)
        q=deque()
        q.append([beginWord,1])
        while q:
            word,steps=q.popleft()
            for i in range(len(word)):
                for ch in string.ascii_lowercase:
                    newword=word[:i]+ch+word[i+1:]

                    if newword==endWord:
                        return steps+1
                    
                    if newword in visited:
                        visited.remove(newword)
                        q.append([newword,steps+1])

        return 0
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visited_set=set()
        for i in wordList:
            visited_set.add(i)
        q=deque()
        q.append([beginWord,1])
        while q:
            word,steps=q.popleft()
            for i in range(len(word)):
                for ch in string.ascii_lowercase:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word == endWord:
                        return steps+1
                    if new_word in visited_set:
                        visited_set.remove(new_word)
                        q.append([new_word,steps+1])
                        
        return 0
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split()
        count=1
        for i in words:
            if(i.startswith(searchWord)):
                return count

            count+=1
        return -1
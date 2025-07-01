class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev=word[0]
        count=1
        n=len(word)
        for i in range(1,n):
            if word[i]==prev:
                count+=1
            else:
                prev=word[i]

        return count
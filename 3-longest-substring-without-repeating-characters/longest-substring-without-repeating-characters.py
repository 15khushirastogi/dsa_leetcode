class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        i=0
        hashmap={}
        n=len(s)
        for j in range(n):
            if s[j] in hashmap and hashmap[s[j]]>=i:
                i=hashmap[s[j]]+1
            hashmap[s[j]]=j
            maxlen=max(maxlen,j-i+1)

        return maxlen
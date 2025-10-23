class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        n=len(s)
        maxcount=0
        maxlen=0
        mp={}
        for j in range(n):
            if s[j] in mp:
                mp[s[j]]+=1
            else:
                mp[s[j]]=1

            maxcount=max(maxcount,mp[s[j]])
            while (j-i+1)-maxcount>k:
                mp[s[i]]-=1
                i+=1

            maxlen=max(maxlen,j-i+1)

        return maxlen
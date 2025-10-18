class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        n=len(s)
        max_len=0
        max_count=0
        mp={}
        for j in range(n):
            if s[j] in mp:
                mp[s[j]]+=1
            else:
                mp[s[j]]=1
            
            max_count=max(max_count,mp[s[j]])

            while (j-i+1)-max_count>k:
                mp[s[i]]-=1
                i+=1

            max_len=max(max_len,j-i+1)

        return max_len
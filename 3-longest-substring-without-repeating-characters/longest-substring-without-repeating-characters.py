class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count=1
        if(len(s)==0):
            return 0
        else:
            for i in range(0,len(s)-1):
                l1=[]
                for j in range(i,len(s)):
                    if(s[j] in l1):
                        break
                    else:
                        l1.append(s[j])
                        count=len(l1)
                if(count>max_count):
                    max_count=count
            return max_count



        


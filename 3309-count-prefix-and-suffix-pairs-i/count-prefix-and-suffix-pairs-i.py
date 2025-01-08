class Solution:
    def isPrefixAndSuffix(self, str1, str2):
        if(len(str1)>len(str2)):
            return False
        i=0
        while(i<len(str1)):
            if(str1[i]!=str2[i]):
                return False
            i+=1
        j=1
        while(j<=len(str1)):
            if(str1[-j]!=str2[-j]):
                return False
            j+=1
        return True
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(0,len(words)-1):
            for j in range(i+1,len(words)):
                if(self.isPrefixAndSuffix(words[i], words[j])):
                    count+=1
        return count
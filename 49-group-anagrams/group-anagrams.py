class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        d = {}
        for word in strs:
            sorted_word = tuple(sorted(word)) 
            if sorted_word not in d:
                d[sorted_word] = [word]
            else:
                d[sorted_word].append(word)

        for key in d:
            ans.append(d[key])
        
        return ans

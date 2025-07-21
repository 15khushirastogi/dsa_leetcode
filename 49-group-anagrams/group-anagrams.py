class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            if sortedword in hashmap:
                hashmap[sortedword].append(word)
            else:
                hashmap[sortedword] = [word]
        return list(hashmap.values())

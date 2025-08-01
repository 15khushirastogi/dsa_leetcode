class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            binary=bin(i)[2:]
            ans.append(binary.count('1'))

        return ans
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        stack=[] #[temp,index]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackIndex=stack.pop()
                result[stackIndex]=i-stackIndex

            stack.append([t,i])

        return result
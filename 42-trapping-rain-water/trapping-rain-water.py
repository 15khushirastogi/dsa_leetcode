class Solution:
    def trap(self, height: List[int]) -> int:
        #preprocessed array
        left=[0]*len(height)
        right=[0]*len(height)
        leftmax=height[0]
        rightmax=height[-1]
        amount=0
        for i in range(len(height)):
            leftmax=max(leftmax,height[i])
            left[i]=leftmax
        
        for j in range(len(height)-1,-1,-1):
            rightmax=max(rightmax,height[j])
            right[j]=rightmax
        
        for water in range(len(height)):
            amount+=min(left[water],right[water])-height[water]

        return amount
        